from flask import Flask, jsonify, request

import json

app = Flask(__name__)

import os
from anthropic import Anthropic
from dotenv import load_dotenv
import json

# Load environment variables from .env file
load_dotenv()

class WorkAssistant:
    def __init__(self):
        # Initialize Anthropic client
        self.anthropic = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
        
        # Initialize user profile
        self.user_profile = {
            "name": "",
            "role": "",
            "department": "",
            "work_preferences": [],
            "skills": [],
            "communication_style": "",
            "time_zone": ""
        }
        
        # System prompt to define Claude's role
        self.system_prompt = """You are a knowledgeable and supportive personal work assistant. 
        Your role is to provide personalized productivity advice, task management guidance, and work organization strategies. 
        Always prioritize efficiency and encourage sustainable work habits. 
        Help maintain work-life balance and suggest ways to optimize workflows while avoiding burnout."""
    
    def setup_profile(self):
        """Initial setup to gather user information"""
        print("Welcome to your AI Work Assistant! Let's set up your profile.")
        
        self.user_profile["name"] = input("What's your name? ")
        self.user_profile["role"] = input("What's your job role? ")
        self.user_profile["department"] = input("Which department do you work in? ")
        
        print("\nWhat are your work preferences? (e.g., 'early meetings', 'async communication') (Enter one per line, press Enter twice when done)")
        while True:
            preference = input()
            if preference == "":
                break
            self.user_profile["work_preferences"].append(preference)
        
        print("\nWhat are your key skills? (Enter one per line, press Enter twice when done)")
        while True:
            skill = input()
            if skill == "":
                break
            self.user_profile["skills"].append(skill)
        
        print("\nWhat's your preferred communication style?")
        print("1. Direct and concise")
        print("2. Detailed and thorough")
        print("3. Collaborative and discussion-based")
        print("4. Visual and example-driven")
        print("5. Mixed/Flexible")
        
        communication_styles = {
            "1": "Direct and concise",
            "2": "Detailed and thorough",
            "3": "Collaborative and discussion-based",
            "4": "Visual and example-driven",
            "5": "Mixed/Flexible"
        }
        
        choice = input("Choose (1-5): ")
        self.user_profile["communication_style"] = communication_styles.get(choice, "Mixed/Flexible")
        
        self.user_profile["time_zone"] = input("What's your time zone? (e.g., EST, PST, UTC): ")
        
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
            Role: {self.user_profile['role']}
            Department: {self.user_profile['department']}
            Work Preferences: {', '.join(self.user_profile['work_preferences'])}
            Skills: {', '.join(self.user_profile['skills'])}
            Communication Style: {self.user_profile['communication_style']}
            Time Zone: {self.user_profile['time_zone']}
            
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
        print("\nAI Assistant:", response)
        return response


'''
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "ask_work_assistant",
    "arguments": {
      "title": "User Has Question",
      "body": "How can I better organize my tasks?",
      "labels": ["productivity"]
    }
  }
}
'''

def log_json(data):
    with open('/shared/work-assistant.log', 'a') as f:
        f.write(json.dumps(data, indent=2)+'\n')

def log_text(txt):
    with open('/shared/work-assistant.log') as f:
        f.write(txt + '\n')

def load_work_assistant():
    assistant = WorkAssistant()
    assistant.user_profile = {
        "name": "Claude Ant",
        "role": "Software Engineer",
        "department": "Engineering",
        "work_preferences": ["async communication", "afternoon meetings"],
        "skills": ["Python", "Project Management", "Technical Writing"],
        "communication_style": "Direct and concise",
        "time_zone": "PST"
    }
    return assistant


def run_work_assistant(data):
    body = data.get('params',{}).get('arguments',{}).get('body',{}).strip()
    assert(body)
    assistant = load_work_assistant()
    res = assistant.start_session(body)
    return res

@app.route('/mcp/v1', methods=['POST'])
def work():
    data = request.get_json()
    log_text('\n\n======== INCOMING MCP RESPONSE ========\n\n')
    log_json(data)

    method_name = data.get('params',{}).get('name')
    if method_name == 'ask_work_assistant':
        res = run_work_assistant(data)
    resp = {
          "jsonrpc": "2.0",
          "id": 1,
          "result": {
            "content": [
              {
                "type": "text",
                "text": f"Work Assistant Says: {res}"
              }
            ]
          }
        }
    log_text('\n\n======= RESPONDING WITH MCP RESPONSE =======')
    log_json(resp)
    return jsonify()


if __name__ == '__main__':
    app.run(port=5001, host='0.0.0.0')
