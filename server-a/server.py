from flask import Flask, jsonify, request

import json

app = Flask(__name__)

import os
from anthropic import Anthropic
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

class HealthTrainer:
    def __init__(self):
        # Initialize Anthropic client
        self.anthropic = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
        
        # Initialize user profile
        self.user_profile = {
            "name": "",
            "age": 0,
            "weight": 0,
            "height": 0,
            "fitness_goals": [],
            "dietary_restrictions": [],
            "activity_level": ""
        }
        
        # System prompt to define Claude's role
        self.system_prompt = """You are a knowledgeable and supportive personal health trainer. 
        Your role is to provide personalized fitness advice, workout plans, and nutritional guidance. 
        Always prioritize safety and encourage sustainable healthy habits. 
        If a user mentions any concerning health symptoms, advise them to consult with a healthcare professional."""
    
    def setup_profile(self):
        """Initial setup to gather user information"""
        print("Welcome to your AI Health Trainer! Let's set up your profile.")
        
        self.user_profile["name"] = input("What's your name? ")
        self.user_profile["age"] = int(input("What's your age? "))
        self.user_profile["weight"] = float(input("What's your weight in kg? "))
        self.user_profile["height"] = float(input("What's your height in cm? "))
        
        print("\nWhat are your fitness goals? (Enter one per line, press Enter twice when done)")
        while True:
            goal = input()
            if goal == "":
                break
            self.user_profile["fitness_goals"].append(goal)
        
        print("\nDo you have any dietary restrictions? (Enter one per line, press Enter twice when done)")
        while True:
            restriction = input()
            if restriction == "":
                break
            self.user_profile["dietary_restrictions"].append(restriction)
        
        print("\nWhat's your activity level?")
        print("1. Sedentary (little or no exercise)")
        print("2. Lightly active (light exercise/sports 1-3 days/week)")
        print("3. Moderately active (moderate exercise/sports 3-5 days/week)")
        print("4. Very active (hard exercise/sports 6-7 days/week)")
        print("5. Super active (very hard exercise/sports & physical job or training twice per day)")
        
        activity_levels = {
            "1": "Sedentary",
            "2": "Lightly active",
            "3": "Moderately active",
            "4": "Very active",
            "5": "Super active"
        }
        
        choice = input("Choose (1-5): ")
        self.user_profile["activity_level"] = activity_levels.get(choice, "Moderately active")
        
        # Save profile to file
        with open("user_profile.json", "w") as f:
            json.dump(self.user_profile, f, indent=4)
        
        print("\nProfile setup complete!")

    def load_profile(self):
        """Load existing user profile"""
        try:
            with open("user_profile.json", "r") as f:
                self.user_profile = json.load(f)
            return True
        except FileNotFoundError:
            return False

    def get_ai_response(self, user_message):
        """Get response from Claude"""
        try:
            # Prepare the context with user profile
            context = f"""User Profile:
            Name: {self.user_profile['name']}
            Age: {self.user_profile['age']}
            Weight: {self.user_profile['weight']} kg
            Height: {self.user_profile['height']} cm
            Fitness Goals: {', '.join(self.user_profile['fitness_goals'])}
            Dietary Restrictions: {', '.join(self.user_profile['dietary_restrictions'])}
            Activity Level: {self.user_profile['activity_level']}
            
            User Question/Message: {user_message}"""

            # Get response from Claude
            message = self.anthropic.messages.create(
                model="claude-3-5-sonnet-20241022",
                max_tokens=1000,
                system=self.system_prompt,
                messages=[
                    {
                        "role": "user",
                        "content": context
                    }
                ]
            )
            
            return message.content[0].text
        
        except Exception as e:
            return f"Error getting response: {str(e)}"

    def start_session(self, user_input):
        response = self.get_ai_response(user_input)
        print("\nAI Trainer:", response)
        return response


'''
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "ask_personal_trainer",
    "arguments": {
      "title": "User Has Question",
      "body": "What should I do for my weight?",
      "labels": ["health"]
    }
  }
}
'''

def log_json(data):
    with open('/shared/personal-trainer.log', 'a') as f:
        f.write(json.dumps(data, indent=2)+'\n')

def log_text(txt):
    with open('/shared/personal-trainer.log', 'a') as f:
        f.write(txt + '\n')

def load_personal_trainer():
    trainer = HealthTrainer()
    trainer.user_profile = {
        "name": "Claude Ant",
        "age": 30,
        "weight": 70,
        "height": 175,
        "fitness_goals": ["Lose weight", "Build muscle"],
        "dietary_restrictions": ["Gluten-free", "Dairy-free"],
        "activity_level": "Moderately active"
    }
    return trainer


def run_personal_trainer(data):
    body = data.get('params',{}).get('arguments',{}).get('body',{}).strip()
    assert(body)
    trainer = load_personal_trainer()
    res = trainer.start_session(body)
    return res

@app.route('/mcp/v1', methods=['POST'])
def health():
    data = request.get_json()
    log_text('\n\n======== INCOMING MCP RESPONSE ========\n\n')
    log_json(data)

    method_name = data.get('params',{}).get('name')
    if method_name == 'ask_personal_trainer':
        res = run_personal_trainer(data)
    resp = {
          "jsonrpc": "2.0",
          "id": 1,
          "result": {
            "content": [
              {
                "type": "text",
                "text": f"Personal Trainer Says: {res}"
              }
            ]
          }
        }
    log_text('\n\n======= RESPONDING WITH MCP RESPONSE =======')
    log_json(resp)
    return jsonify()


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')



