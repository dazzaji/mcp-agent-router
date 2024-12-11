# MCP Multi-Agent Modular Awesomeness!

![alt text](image.png)

## Overview

This is a primative multi-agent modular initialization capability test prototype of Model Context Protocol.  My test project will have multiple servers and clients.  They will operate in a modular way, the first will create a markdown file based on adding user input text to a content template and saving the file to root directory.  The second will ingest that file and add more info to it then save the updated version to the root.  The alt A third will likewise ingest the output of the second and add still more content and export the third version of the file to the root.  The alt B third server alternatively could take another action.  Treat each of these three like back boxes in the sense that they will not share code or components but we will pretend they are running on different technologies to preserve the modular approach and we will for convenience be able to do things like share a virtual environment and requirements for this first test.  The second server will be a decider and will choose which is the best next server.

The notion of strict modularity such that different MCP interoperable system could be created and operated by totally different teams or even different companies is potentially a key unlock for MCP and for LLM based agents to take off and be scalable and more fully userful.  This is described more fully in the project overview for "Agent" here: [https://github.com/dazzaji/mcp-project/issues/1](https://github.com/dazzaji/mcp-project/issues/1). 

## Try it!

Let's get your MCP project running in VS Code with the Inspector and Claude Desktop.

**1. Running in VS Code with MCP Inspector**

Here's how to run your project in VS Code and inspect the communication using MCP Inspector:

* **Install the `mcp` package:**  In your project root (`mcp-project`), ensure you have installed the MCP package in your active virtual environment:

```bash
uv add mcp
```

* **Set up `launch.json`**: You'll need launch configurations for each of your MCP servers.  Since you're simulating "black boxes" that *might* run different underlying technologies, the launch configuration will vary for the Gemini server.  Create a `.vscode/launch.json` file in your project's root directory with the following configurations.  This assumes the gemini-server takes a `model` parameter, which specifies the model to use.

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Module 1 Server",
            "type": "python",
            "request": "launch",
            "module": "module1_server.server", // Use module mode for direct execution
            "console": "integratedTerminal"
        },
        {
            "name": "Gemini Server",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/gemini-server/server.py",
            "args": ["--model", "gemini-pro"], // Example model argument
            "console": "integratedTerminal"
        }
    ]
}
```

*   **Running the servers:**
    *   Open the `module1-server/server.py` file in VS Code.
    *   Start the debugger by pressing `F5` or selecting "Start Debugging" from the "Run" menu, and choose the `Module 1 Server` configuration. This will start the Module 1 server in the VS Code integrated terminal. In a similar way, start the `Gemini Server` in a separate terminal.
    *   In a new terminal at the root of your project, start the gateway agent with `uv run gateway_agent`.


*   **Start MCP Inspector:**
    *   Open a *new* terminal in the `gateway-agent` directory.
    *   Run the following command:

    ```bash
    npx @modelcontextprotocol/inspector python -m gateway_agent
    ```
    *   This starts the MCP Inspector, which automatically launches the gateway-agent server and the Inspector UI. A URL will be printed in the terminal. Open this URL in your browser to access the UI.

    *   In the Inspector UI, click on "Tools" to confirm the tools your gateway agent has registered.

Now you can interact with the servers through the MCP Inspector UI, sending requests and viewing responses and logs. The logging messages from your `service.py` file will appear in the Inspector's console, which can be useful for debugging.  You can test the routing functionality by calling the `route_task` tool with different inputs and observing which downstream server is called.



**2. Running with Claude Desktop**

To use your MCP servers with Claude Desktop:

*   **Install your servers** into your local environment or a Docker container. If you use Docker make sure both the gateway agent and servers A and B are all accessible on the same Docker network.
*   **Configure `claude_desktop_config.json`:**

    *   Locate your `claude_desktop_config.json` file (the path depends on your operating system; consult the MCP docs for details).

    *   Add configurations for your *gateway-agent* server under the `mcpServers` key. Since your gateway agent now uses HTTP/SSE, you will need to specify the URL accordingly.

        ```json
        {
          "mcpServers": {
            "gateway-agent": {
              "url": "http://localhost:8000/mcp/v1" // Replace with gateway agent url
            },
            "server-a": {
              "url": "http://localhost:5000/mcp/v1" // Replace with Server A url
            },
              "server-b": {
              "url": "http://localhost:5001/mcp/v1" // Replace with Server B url
            }
          }
        }
        ```

        Make sure the port numbers match the ports your servers are listening on.  Replace `/mcp/v1` with the actual endpoint if it's different.  Make sure to add server B analogous to server A, and start it on a different port. 

*   **Restart Claude Desktop:** For the changes in your `claude_desktop_config.json` file to take effect, you need to restart Claude Desktop.

Now you should be able to interact with your gateway agent via Claude's slash commands or other UI elements provided by Claude Desktop to use MCP tools. You can test the routing by entering queries that should be directed to different servers.

With these steps, you should be able to run your MCP project, inspect server communications with the Inspector, and integrate your gateway agent with Claude Desktop! Let me know if you encounter any issues, and I'll help troubleshoot.


------

# Use Inspector to See What is Happening Under the Hood

Okay, here's a step-by-step guide to run your project and inspect the MCP traffic using the Inspector. We'll use Docker Compose to simplify the process since you have Dockerfiles. This approach ensures consistent environment setup and easier management of multiple services.

**Prerequisites:**

1.  **Docker Desktop:** Make sure you have Docker Desktop installed and running.
2.  **Docker Compose:** Verify Docker Compose is installed. You can check with `docker compose version`. If not, install it according to the instructions for your OS.
3.  **MCP Inspector:** Ensure MCP Inspector is installed globally: `npm install -g @modelcontextprotocol/inspector`
4. **Anthropic API Key:** You'll need a valid Anthropic API key for both Server A and Server B (as they use Claude). Set this in an `.env` file in both the `server-a` and `server-b` directories. Note that your `.gitignore` is set up correctly to ignore `.env` files.
5. **Gemini API Key:** Similarly set up the `GEMINI_API_KEY` for the Gemini server in an `.env` file in the root of the project

**Steps:**

1. **Prepare Server A and Server B:**

* **User Profile Data:** Create a `user_profile.json` file in both `server-a` and `server-b` with the user profile information you provided for each (health and professional profiles, respectively). Format this data as JSON. 

Here's how those files should be structured: 

`server-a/user_profile.json`:

```json
{
  "name": "John Doey",
  "date_of_birth": "August 15, 1997",
  "gender": "Male",
  "height": "5'8\"",
  "weight": "150 lbs",
  "bmi": 22.7,
  "body_fat_percentage": 23.5,
  "muscle_mass": "64.6 lbs",
  "bone_mass": "7.1 lbs",
  "last_measured_body_composition": "December 1, 2024",
  "blood_pressure": "118/75 mmHg",
  "heart_rate": 68,
  "respiratory_rate": 14,
  "last_measured_vital_signs": "December 9, 2024",
  "weight_management_target": "150 lbs",
  "weight_management_deadline": "June 30, 2025",
  "weight_management_type": "Maintenance",
  "daily_steps": 8000,
  "weekly_exercise": "150 minutes",
  "weekly_workouts": 3,
  "daily_caloric_target": 2200,
  "macronutrient_breakdown": {
    "protein": "2.8 oz (80g)",
    "carbohydrates": "8.8 oz (250g)",
    "fats": "2.6 oz (73g)"
  },
  "current_conditions": [
    {
      "name": "Computer Vision Syndrome",
      "diagnosed": "September 15, 2023",
      "status": "Active",
      "medications": null
    },
    {
      "name": "Mild Anxiety",
      "diagnosed": "March 20, 2023",
      "status": "Active",
      "treatment": {
        "type": "Meditation App Subscription",
        "duration": "15 minutes",
        "frequency": "Daily",
        "started": "March 25, 2023",
        "ongoing": true
      }
    }
  ],
  "allergies": [
    {
      "name": "Tree Pollen",
      "severity": "Mild",
      "symptoms": ["Sneezing", "Itchy eyes"]
    }
  ],
  "family_history": {
    "type_2_diabetes": "Paternal grandfather",
    "hypertension": "Maternal grandmother"
  },
  "preferences": {
    "measurement_system": "Imperial",
    "dietary_restrictions": ["Vegetarian", "Low-caffeine"],
    "exercise_preferences": ["Yoga", "Running", "Home workouts"],
    "reminders": true,
    "progress_updates": true,
    "health_tips": true
  },
  "last_updated": "December 10, 2024"
}
```

`server-b/user_profile.json`:

```json
{
  "name": "John Doey",
  "user_id": "JP_AI_2024",
  "current_role": "Machine Learning Engineer II",
  "industry": "Artificial Intelligence",
  "years_of_experience": 2,
  "preferred_work_style": "Hybrid",
  "current_position": {
    "title": "Machine Learning Engineer II",
    "band": "IC2",
    "start_date": "January 15, 2024"
  },
  "technical_skills": [
    {
      "name": "PyTorch",
      "proficiency": "Advanced",
      "last_used": "December 9, 2024"
    },
    {
      "name": "LLM Fine-tuning",
      "proficiency": "Intermediate",
      "last_used": "December 9, 2024"
    },
    {
      "name": "MLOps",
      "proficiency": "Intermediate",
      "last_used": "December 8, 2024"
    }
  ],
  "soft_skills": [
    {
      "name": "Technical Communication",
      "self_assessment": 8,
      "last_assessed": "November 30, 2024"
    },
    {
      "name": "Project Management",
      "self_assessment": 7,
      "last_assessed": "November 30, 2024"
    }
  ],
  "time_management": {
    "preferred_hours": "9:30 AM - 6:30 PM (PST)",
    "focus_time_blocks": {
      "morning": "120-minute block"
    }
  },
  "meeting_preferences": {
    "maximum_daily_meetings": 4,
    "preferred_duration": "30 minutes",
    "buffer_time": "15 minutes"
  },
  "professional_goals": {
    "short_term_objectives": [
      {
        "name": "LLM Evaluation Framework Project",
        "role": "Project Lead",
        "target_date": "March 30, 2025",
        "status": "In Progress",
        "type": "Project"
      },
      {
        "name": "MLOps Certification",
        "target_date": "February 28, 2025",
        "status": "In Progress",
        "type": "Certification"
      }
    ],
    "long_term_objectives": {
      "primary_goal": "Senior ML Engineer Role",
      "target_year": 2026,
      "key_milestones": [
        "Lead 2 major technical initiatives (Due: December 31, 2025)",
        "Develop team mentorship experience",
        "Establish technical thought leadership"
      ]
    }
  },
    "development_activities": {
    "current_projects": [
      {
        "name": "LLM Evaluation Framework",
        "role": "Technical Lead",
        "skills": ["ML Architecture", "Team Leadership"],
        "visibility": "Company-wide"
      },
      {
        "name": "Model Optimization Initiative",
        "role": "Individual Contributor",
        "skills": ["Performance Tuning", "MLOps"],
        "visibility": "Department"
      }
    ],
    "training_programs": [
      {
        "name": "MLOps Certification Program",
        "provider": "Major Cloud Provider",
        "status": "In Progress",
        "expected_completion": "Q1 2025"
      },
      {
        "name": "Technical Leadership Workshop",
        "provider": "Internal L&D",
        "status": "Planned",
        "start_date": "January 2025"
      }
    ]
  },
  "learning_and_growth": {
    "areas_of_focus": {
      "technical": ["Large Language Models", "Distributed Systems", "ML Infrastructure"],
      "leadership": ["Team Management", "Technical Project Planning", "Stakeholder Communication"]
    },
    "resources": [
      "Internal ML Engineering Wiki",
      "Technical Conference Presentations",
      "Industry Research Papers",
      "Team Knowledge Sharing Sessions"
    ]
  },
  "professional_network_development": {
    "current_activities": [
      "Regular 1:1s with Senior Engineers",
      "Monthly ML Community Meetups",
      "Internal Tech Talks Participant",
      "Open Source Contributions"
    ],
    "mentorship": {
      "seeking_in": ["Technical Leadership", "Project Management"],
      "providing_in": ["PyTorch", "LLM Implementation"]
    }
  },
  "preferences": {
    "learning_style": ["Hands-on Implementation", "Documentation Creation", "Collaborative Problem-solving"],
    "growth_areas": ["System Architecture Design", "Team Leadership", "Technical Writing"],
    "goal_reminders": true,
    "networking_opportunities": true,
    "learning_recommendations": true
  },
  "last_updated": "December 10, 2024"
}
```



* **Install Dependencies:** Make sure all the servers have the needed dependencies:

  ```bash
  cd server-a
  pip install -r requirements.txt # Install dependencies for server-a
  cd ../server-b
  pip install -r requirements.txt # Install dependencies for server-b
  cd ../gateway-agent
  pip install -r requirements.txt # Install dependencies for gateway-agent
  cd ../gemini-server
  pip install -r requirements.txt # Install dependencies for gemini-server
  cd .. # Go back to root
  ```
  Make sure to create `requirements.txt` files in each directory, containing the libraries each uses. The root `requirements.txt` can include `mcp`.  A simple way to create these files is by activating the relevant virtual environment, then using `pip freeze > requirements.txt` in each project directory.

2. **Define the Docker Network (Optional but recommended):** If you're not using host network mode, you need to create the docker network in the `docker-compose.yaml` file, so that the gateway agent can discover and communicate with Server A and Server B. Here's how:

```yaml
services:
  # ... (your service definitions)

networks:
  mcp-network: # Give your network a name

```

Then add the network to each of the Docker container specifications:

```yaml
services:
  gateway-agent:
    # ... other settings
    networks:
      - mcp-network

  server-a:
    # ... other settings
    networks:
      - mcp-network

  server-b:  # Added server-b
    # ... similar to server-a
    networks:
      - mcp-network
```

3.  **Run with Docker Compose:** In your project root, run:

    ```bash
    docker compose up --build
    ```

    This builds and starts all servers in the background with appropriate port mapping and shared volume.  Now you should have all the components (servers, shared volume) set up in Docker containers. This is generally a more reliable approach for consistent execution since you also provided Dockerfiles.

4.  **Connect with MCP Inspector:** In a new terminal, run:

    ```bash
    npx @modelcontextprotocol/inspector http://gateway-agent:8000/mcp/v1 # Note the protocol is now http
    ```


-------------------

# Running the Project 

(replace paths with correct paths on your machine)

Certainly! Below is a comprehensive **cheat-sheet** capturing all the steps needed to set up and run the `mcp-agent-router` project successfully, taking into account everything we learned during troubleshooting:

---

# **MCP-Agent-Router Project Setup and Execution Cheat-Sheet**

## **1. Initial Setup**
### **Step 1: Clone the Repository**
If you haven’t already cloned the project:
```bash
git clone <repository-url>
cd mcp-agent-router
```

---

### **Step 2: Set Up the Python Virtual Environment**
1. Remove any conflicting virtual environments if they exist:
   ```bash
   rm -rf .venv venv
   ```

2. Create a new virtual environment using Python 3.11:
   ```bash
   /Library/Frameworks/Python.framework/Versions/3.11/bin/python3.11 -m venv ./venv
   ```

3. Link `venv` to `.venv` to satisfy tools like `uv`:
   ```bash
   ln -s venv .venv
   ```

4. Activate the virtual environment:
   ```bash
   source ./venv/bin/activate
   ```

5. Confirm the Python version:
   ```bash
   python --version
   ```
   The output should be:
   ```
   Python 3.11.1
   ```

6. Install the required dependencies:
   ```bash
   pip install flask anthropic requests python-dotenv uv mcp
   ```

---

### **Step 3: Configure `.python-version`**
If the project contains a `.python-version` file, ensure it matches Python 3.11:
```bash
echo "3.11" > .python-version
```

---

## **2. Running the Project**

### **Step 4: Start Server A**
1. Open a new terminal tab or window in VS Code.
2. Activate the virtual environment:
   ```bash
   source ./venv/bin/activate
   ```
3. Navigate to the `server-a` directory:
   ```bash
   cd server-a
   ```
4. Run the server:
   ```bash
   python server.py
   ```

---

### **Step 5: Start Server B**
1. Open another terminal tab or window.
2. Activate the virtual environment:
   ```bash
   source ./venv/bin/activate
   ```
3. Navigate to the `server-b` directory:
   ```bash
   cd server-b
   ```
4. Run the server:
   ```bash
   python server.py
   ```

---

### **Step 6: Start the Gateway**
1. Open another terminal tab or window.
2. Ensure the virtual environment is active:
   ```bash
   source ./venv/bin/activate
   ```
3. Run the gateway:
   ```bash
   uv run /Users/dazzagreenwood/mcp-agent-router/gateway-agent/service.py
   ```

---

## **3. Testing and Verification**

### **Step 7: Verify the Setup**
1. **Check Each Server**:
   - Confirm that `server-a`, `server-b`, and the gateway server are running without errors.
   - Each server should be displaying logs or listening for requests.

2. **Test with the Client (if applicable)**:
   If the project includes a client like **Claude Desktop**, connect it to the gateway:
   - Edit the `claude_desktop_config.json` file to include:
     ```json
     {
       "mcpServers": {
         "gateway": {
           "command": "uv",
           "args": ["run", "/Users/dazzagreenwood/mcp-agent-router/gateway-agent/service.py"]
         }
       }
     }
     ```
   - Restart Claude Desktop.
   - Test the client by interacting with the connected servers.

---

## **4. Troubleshooting Tips**
### **If `uv` Uses the Wrong Python Version:**
1. Ensure `.venv` is linked to `venv`:
   ```bash
   ln -s venv .venv
   ```
2. Ensure the `VIRTUAL_ENV` variable points to the correct environment:
   ```bash
   export VIRTUAL_ENV=$(pwd)/venv
   ```

---

### **If `mcp` Module is Not Found:**
1. Confirm `mcp` is installed:
   ```bash
   pip list | grep mcp
   ```
2. Reinstall it if necessary:
   ```bash
   pip install mcp
   ```

---

### **If VS Code is Misaligned:**
1. Open Command Palette (`Cmd + Shift + P`).
2. Select `Python: Select Interpreter` and choose `Python 3.11.1 ('venv')`.

---

### **If Gateway or Servers Fail to Start:**
1. Check the logs in the terminal for detailed error messages.
2. Ensure all dependencies are installed in the active virtual environment.
3. Manually run the failing script with Python to isolate issues:
   ```bash
   python /path/to/script.py
   ```

---

## **5. Cleanup and Restart**
To restart the entire project setup from scratch:
1. Stop all servers (`Ctrl+C` in each terminal).
2. Deactivate the virtual environment:
   ```bash
   deactivate
   ```
3. Delete existing virtual environments and recreate them following **Step 2**.

---

This cheat-sheet should serve as a reliable guide for running your `mcp-agent-router` project, including all the tricky steps we encountered during the setup. Let me know if there’s anything else you’d like added!
This will connect the inspector to the gateway-agent and present a URL for you to access the inspector UI. From the UI, you should be able to call tools exposed by gateway agent, which will in turn route requests to the appropriate downstream servers.  The debug=True parameters we set earlier will help to pinpoint where issues are arising.  Make sure that servers A and B are accessible on port 5000 and 5001 on your local machine, respectively.  If you use Docker and don't expose these ports on host network (via the `ports` configuration in docker-compose), you'll need to attach to the network the containers create with the following command so that the DNS entries for the services are present: `docker network connect <networkname> <containername>`
