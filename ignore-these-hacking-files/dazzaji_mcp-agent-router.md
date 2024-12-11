├── .gitignore
├── .python-version
├── GPT-4o.md
├── Gemini.md
├── LICENSE
├── README.md
├── clients
    └── claude-desktop
    │   ├── proxy.py
    │   └── readme.md
├── docker-compose.yaml
├── example-service
    ├── .dockerignore
    ├── .gitignore
    ├── Dockerfile
    ├── README.md
    ├── listen.sh
    ├── pyproject.toml
    ├── run.sh
    └── service.py
├── gateway-agent
    ├── .dockerignore
    ├── .gitignore
    ├── Dockerfile
    ├── README.md
    ├── listen.sh
    ├── pyproject.toml
    ├── run.sh
    └── service.py
├── hacking-files
    ├── .DS_Store
    ├── dazzaji_mcp-agent-router.md
    ├── mcp-full-docs.md
    └── scratch-pad-for-gateway-agent.md
├── hello.py
├── image.png
├── pyproject.toml
├── server-a
    ├── Dockerfile
    ├── server.py
    └── talk.py
├── server-b
    ├── Dockerfile
    ├── server.py
    └── talk.py
├── user-info-for-server-a.md
├── user-info-for-server-b.md
└── uv.lock


/.gitignore:
--------------------------------------------------------------------------------
  1 | # Byte-compiled / optimized / DLL files
  2 | __pycache__/
  3 | *.py[cod]
  4 | *$py.class
  5 | 
  6 | # C extensions
  7 | *.so
  8 | 
  9 | # Distribution / packaging
 10 | .Python
 11 | build/
 12 | develop-eggs/
 13 | dist/
 14 | downloads/
 15 | eggs/
 16 | .eggs/
 17 | lib/
 18 | lib64/
 19 | parts/
 20 | sdist/
 21 | var/
 22 | wheels/
 23 | share/python-wheels/
 24 | *.egg-info/
 25 | .installed.cfg
 26 | *.egg
 27 | MANIFEST
 28 | 
 29 | # PyInstaller
 30 | #  Usually these files are written by a python script from a template
 31 | #  before PyInstaller builds the exe, so as to inject date/other infos into it.
 32 | *.manifest
 33 | *.spec
 34 | 
 35 | # Installer logs
 36 | pip-log.txt
 37 | pip-delete-this-directory.txt
 38 | 
 39 | # Unit test / coverage reports
 40 | htmlcov/
 41 | .tox/
 42 | .nox/
 43 | .coverage
 44 | .coverage.*
 45 | .cache
 46 | nosetests.xml
 47 | coverage.xml
 48 | *.cover
 49 | *.py,cover
 50 | .hypothesis/
 51 | .pytest_cache/
 52 | cover/
 53 | 
 54 | # Translations
 55 | *.mo
 56 | *.pot
 57 | 
 58 | # Django stuff:
 59 | *.log
 60 | local_settings.py
 61 | db.sqlite3
 62 | db.sqlite3-journal
 63 | 
 64 | # Flask stuff:
 65 | instance/
 66 | .webassets-cache
 67 | 
 68 | # Scrapy stuff:
 69 | .scrapy
 70 | 
 71 | # Sphinx documentation
 72 | docs/_build/
 73 | 
 74 | # PyBuilder
 75 | .pybuilder/
 76 | target/
 77 | 
 78 | # Jupyter Notebook
 79 | .ipynb_checkpoints
 80 | 
 81 | # IPython
 82 | profile_default/
 83 | ipython_config.py
 84 | 
 85 | # pyenv
 86 | #   For a library or package, you might want to ignore these files since the code is
 87 | #   intended to run in multiple environments; otherwise, check them in:
 88 | # .python-version
 89 | 
 90 | # pipenv
 91 | #   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
 92 | #   However, in case of collaboration, if having platform-specific dependencies or dependencies
 93 | #   having no cross-platform support, pipenv may install dependencies that don't work, or not
 94 | #   install all needed dependencies.
 95 | #Pipfile.lock
 96 | 
 97 | # poetry
 98 | #   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
 99 | #   This is especially recommended for binary packages to ensure reproducibility, and is more
100 | #   commonly ignored for libraries.
101 | #   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
102 | #poetry.lock
103 | 
104 | # pdm
105 | #   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
106 | #pdm.lock
107 | #   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
108 | #   in version control.
109 | #   https://pdm.fming.dev/latest/usage/project/#working-with-version-control
110 | .pdm.toml
111 | .pdm-python
112 | .pdm-build/
113 | 
114 | # PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
115 | __pypackages__/
116 | 
117 | # Celery stuff
118 | celerybeat-schedule
119 | celerybeat.pid
120 | 
121 | # SageMath parsed files
122 | *.sage.py
123 | 
124 | # Environments
125 | .env
126 | .venv
127 | env/
128 | venv/
129 | ENV/
130 | env.bak/
131 | venv.bak/
132 | 
133 | # Spyder project settings
134 | .spyderproject
135 | .spyproject
136 | 
137 | # Rope project settings
138 | .ropeproject
139 | 
140 | # mkdocs documentation
141 | /site
142 | 
143 | # mypy
144 | .mypy_cache/
145 | .dmypy.json
146 | dmypy.json
147 | 
148 | # Pyre type checker
149 | .pyre/
150 | 
151 | # pytype static type analyzer
152 | .pytype/
153 | 
154 | # Cython debug symbols
155 | cython_debug/
156 | 
157 | # PyCharm
158 | #  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
159 | #  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
160 | #  and can be added to the global gitignore or merged into this file.  For a more nuclear
161 | #  option (not recommended) you can uncomment the following to ignore the entire idea folder.
162 | #.idea/
163 | 


--------------------------------------------------------------------------------
/.python-version:
--------------------------------------------------------------------------------
1 | 3.9
2 | 


--------------------------------------------------------------------------------
/GPT-4o.md:
--------------------------------------------------------------------------------
  1 | # OpenAI GPT-4o
  2 | 
  3 | I have reviewed the uploaded documentation and understand the Model Context Protocol (MCP) framework, as well as the provided tools and structure. We can proceed to create your modular test project with three independent "black box" components as described. Here's an outline of the steps we'll follow:
  4 | 
  5 | ### Step 1: Define the Test Project Structure
  6 | Each component will be a standalone module:
  7 | 1. **Module 1**: Creates a markdown file based on user input and saves it to the root directory.
  8 | 2. **Module 2**: Reads the file created by Module 1, adds more content, and saves the updated file.
  9 | 3. **Module 3**: Processes the output of Module 2, finalizes the content, and exports it.
 10 | 
 11 | We'll maintain modularity and simulate the modules running on different technologies while allowing them to share a virtual environment for this test.
 12 | 
 13 | ### Step 2: Use MCP for Communication
 14 | Each module will act as a server that provides endpoints for specific tasks. We'll use the `create-mcp-server` package to scaffold each server.
 15 | 
 16 | ### Step 3: Develop Each Module
 17 | - Implement unique logic for each module as per your requirements.
 18 | - Use MCP's server APIs to handle inputs and outputs.
 19 | 
 20 | ### Step 4: Test and Iterate
 21 | - Start the servers, interact with them via the MCP Inspector, and ensure they perform as intended.
 22 | - Validate the output after each module processes the file.
 23 | 
 24 | ### Step 5: Package and Document
 25 | - Provide documentation and clear usage instructions for all modules.
 26 | 
 27 | Would you like me to start scaffolding the Python project, or would you like to dive into a specific part of the process?
 28 | 
 29 | -----------
 30 | 
 31 | ### Outline and Initialization of the Modular Test Project
 32 | 
 33 | This project will consist of three independent MCP servers, each performing a specific task in a pipeline. We will use **MCP Inspector** for debugging and visualization, along with comprehensive logging for visibility.
 34 | 
 35 | ---
 36 | 
 37 | ### **Project Structure**
 38 | ```plaintext
 39 | test-mcp-project/
 40 | ├── module1/                # First module: Creates a markdown file
 41 | │   ├── src/
 42 | │   │   ├── create_markdown_server/
 43 | │   │   │   ├── __init__.py
 44 | │   │   │   ├── __main__.py
 45 | │   │   │   └── server.py
 46 | │   ├── pyproject.toml
 47 | ├── module2/                # Second module: Updates markdown file
 48 | │   ├── src/
 49 | │   │   ├── update_markdown_server/
 50 | │   │   │   ├── __init__.py
 51 | │   │   │   ├── __main__.py
 52 | │   │   │   └── server.py
 53 | │   ├── pyproject.toml
 54 | ├── module3/                # Third module: Finalizes markdown file
 55 | │   ├── src/
 56 | │   │   ├── finalize_markdown_server/
 57 | │   │   │   ├── __init__.py
 58 | │   │   │   ├── __main__.py
 59 | │   │   │   └── server.py
 60 | │   ├── pyproject.toml
 61 | ├── shared_logs/            # Shared logging directory for visibility
 62 | └── README.md               # Documentation
 63 | ```
 64 | 
 65 | ---
 66 | 
 67 | ### **Step 1: Set Up the Environment**
 68 | 1. **Install MCP tools**:
 69 |    ```bash
 70 |    pip install create-mcp-server
 71 |    ```
 72 | 2. **Set up `uv`** (as described in the documentation):
 73 |    ```bash
 74 |    pip install uv
 75 |    ```
 76 | 
 77 | 3. **Use the `create-mcp-server` command** to scaffold the modules:
 78 |    ```bash
 79 |    uvx create-mcp-server
 80 |    ```
 81 | 
 82 | ---
 83 | 
 84 | ### **Step 2: Define Module Functionality**
 85 | 1. **Module 1 (Create Markdown)**:
 86 |    - Receives user input text and a content template.
 87 |    - Creates a markdown file and saves it to the root directory.
 88 |    - Logs every user input and the generated file name.
 89 | 
 90 | 2. **Module 2 (Update Markdown)**:
 91 |    - Reads the file created by Module 1.
 92 |    - Appends additional data (e.g., metadata) to the markdown file.
 93 |    - Saves the updated file with a versioned filename.
 94 | 
 95 | 3. **Module 3 (Finalize Markdown)**:
 96 |    - Reads the file from Module 2.
 97 |    - Adds final content (e.g., a footer or summary).
 98 |    - Saves the final version of the file.
 99 | 
100 | ---
101 | 
102 | ### **Step 3: Logging**
103 | - Use Python’s `logging` module in each server.
104 | - Set up logs to a shared `shared_logs/` directory for cross-module visibility.
105 | - Example logging configuration:
106 |   ```python
107 |   import logging
108 |   import os
109 | 
110 |   LOG_DIR = "../shared_logs/"
111 |   os.makedirs(LOG_DIR, exist_ok=True)
112 | 
113 |   logging.basicConfig(
114 |       filename=os.path.join(LOG_DIR, "module1.log"),
115 |       level=logging.DEBUG,
116 |       format="%(asctime)s - %(levelname)s - %(message)s",
117 |   )
118 |   logger = logging.getLogger(__name__)
119 |   ```
120 | 
121 | ---
122 | 
123 | ### **Step 4: Debugging with MCP Inspector**
124 | 1. **Install MCP Inspector**:
125 |    ```bash
126 |    npm install -g @modelcontextprotocol/inspector
127 |    ```
128 | 
129 | 2. **Run each server with the Inspector**:
130 |    ```bash
131 |    npx @modelcontextprotocol/inspector uv --directory module1/src/create_markdown_server run create_markdown_server
132 |    ```
133 | 
134 | 3. **Use the generated URL to inspect communication logs and visualize interactions.**
135 | 
136 | ---
137 | 
138 | ### **Step 5: Initialize Modules**
139 | Each `server.py` will:
140 | - Include handlers for reading, processing, and saving markdown files.
141 | - Add comprehensive error handling for all operations.
142 | 
143 | ---
144 | 
145 | #### Example: **Module 1 Server (`server.py`)**
146 | ```python
147 | import os
148 | import logging
149 | from mcp.server import Server
150 | from pydantic import AnyUrl
151 | 
152 | LOG_DIR = "../shared_logs/"
153 | os.makedirs(LOG_DIR, exist_ok=True)
154 | 
155 | logging.basicConfig(
156 |     filename=os.path.join(LOG_DIR, "module1.log"),
157 |     level=logging.DEBUG,
158 |     format="%(asctime)s - %(levelname)s - %(message)s",
159 | )
160 | logger = logging.getLogger(__name__)
161 | 
162 | server = Server("MarkdownCreator")
163 | 
164 | @server.call_tool()
165 | async def create_markdown(arguments: dict):
166 |     """Creates a markdown file."""
167 |     try:
168 |         content = arguments.get("content", "")
169 |         filename = arguments.get("filename", "output.md")
170 |         filepath = os.path.join("../", filename)
171 | 
172 |         # Write to markdown file
173 |         with open(filepath, "w") as f:
174 |             f.write(content)
175 | 
176 |         logger.info(f"Created markdown file: {filename}")
177 |         return {"status": "success", "file": filename}
178 |     except Exception as e:
179 |         logger.error(f"Error creating markdown: {e}")
180 |         raise e
181 | 
182 | if __name__ == "__main__":
183 |     logger.info("Starting Markdown Creator Server...")
184 |     server.run()
185 | ```
186 | 
187 | ---
188 | 
189 | ### Next Steps
190 | 1. I will scaffold each module with its corresponding logic.
191 | 2. Implement the pipelines and test interactions.
192 | 3. Provide detailed documentation on running and testing the project.
193 | 
194 | Shall I proceed with initializing the project?
195 | 
196 | --------
197 | 
198 | NUDGE: Yes, please proceed but one update:  the project name and root directory are titled: mcp-hello so please reflect that in all further work and in your suggested VS Code commands to run code or get to directories and such.  Thanks, let's roll!
199 | 
200 | ----------
201 | 
202 | Got it! The project root directory will be named **`mcp-hello`**, and all references will reflect this change. I'll begin initializing the project structure and scaffolding the necessary modules. Here's how we'll proceed:
203 | 
204 | ---
205 | 
206 | ### **Updated Project Structure**
207 | ```plaintext
208 | mcp-hello/
209 | ├── module1/                # First module: Creates a markdown file
210 | │   ├── src/
211 | │   │   ├── create_markdown_server/
212 | │   │   │   ├── __init__.py
213 | │   │   │   ├── __main__.py
214 | │   │   │   └── server.py
215 | │   ├── pyproject.toml
216 | ├── module2/                # Second module: Updates markdown file
217 | │   ├── src/
218 | │   │   ├── update_markdown_server/
219 | │   │   │   ├── __init__.py
220 | │   │   │   ├── __main__.py
221 | │   │   │   └── server.py
222 | │   ├── pyproject.toml
223 | ├── module3/                # Third module: Finalizes markdown file
224 | │   ├── src/
225 | │   │   ├── finalize_markdown_server/
226 | │   │   │   ├── __init__.py
227 | │   │   │   ├── __main__.py
228 | │   │   │   └── server.py
229 | │   ├── pyproject.toml
230 | ├── shared_logs/            # Shared logging directory for visibility
231 | ├── README.md               # Documentation
232 | └── .vscode/                # VS Code configurations
233 |     ├── launch.json         # Debugging configurations
234 |     └── settings.json       # Project-specific settings
235 | ```
236 | 
237 | ---
238 | 
239 | ### **Step 1: Create the Root Directory**
240 | 1. Navigate to your desired location:
241 |    ```bash
242 |    cd ~/Projects
243 |    ```
244 | 2. Create the root directory and initialize the modules:
245 |    ```bash
246 |    mkdir mcp-hello
247 |    cd mcp-hello
248 |    ```
249 | 
250 | ---
251 | 
252 | ### **Step 2: Scaffold Each Module**
253 | I'll use `uv` commands to initialize each module. For each module:
254 | 1. **Navigate to the project root**:
255 |    ```bash
256 |    cd mcp-hello
257 |    ```
258 | 
259 | 2. **Create the server structure**:
260 |    ```bash
261 |    uvx create-mcp-server --name module1/src/create_markdown_server --description "Creates markdown files."
262 |    uvx create-mcp-server --name module2/src/update_markdown_server --description "Updates markdown files."
263 |    uvx create-mcp-server --name module3/src/finalize_markdown_server --description "Finalizes markdown files."
264 |    ```
265 | 
266 | ---
267 | 
268 | ### **Step 3: Shared Logging Directory**
269 | Create the shared logging directory for cross-module visibility:
270 | ```bash
271 | mkdir shared_logs
272 | ```
273 | 
274 | ---
275 | 
276 | ### **Step 4: Implement Module Logic**
277 | Each module will have its own `server.py` file for its specific task. I will populate these files with Python code, as outlined below.
278 | 
279 | #### **Module 1: Create Markdown**
280 | **File**: `module1/src/create_markdown_server/server.py`
281 | - Accepts user input for markdown content.
282 | - Saves the markdown file with a specified or default filename.
283 | - Logs all user inputs and actions.
284 | 
285 | #### **Module 2: Update Markdown**
286 | **File**: `module2/src/update_markdown_server/server.py`
287 | - Reads the markdown file created by Module 1.
288 | - Appends metadata to the file.
289 | - Saves the updated file and logs the operation.
290 | 
291 | #### **Module 3: Finalize Markdown**
292 | **File**: `module3/src/finalize_markdown_server/server.py`
293 | - Reads the file from Module 2.
294 | - Adds a footer or summary.
295 | - Saves the final version and logs the operation.
296 | 
297 | ---
298 | 
299 | ### **Step 5: Debugging with VS Code and MCP Inspector**
300 | #### **VS Code Configuration**
301 | 1. Create `.vscode/launch.json`:
302 |    ```json
303 |    {
304 |        "version": "0.2.0",
305 |        "configurations": [
306 |            {
307 |                "name": "Run Module 1",
308 |                "type": "python",
309 |                "request": "launch",
310 |                "program": "${workspaceFolder}/module1/src/create_markdown_server/__main__.py",
311 |                "console": "integratedTerminal"
312 |            },
313 |            {
314 |                "name": "Run Module 2",
315 |                "type": "python",
316 |                "request": "launch",
317 |                "program": "${workspaceFolder}/module2/src/update_markdown_server/__main__.py",
318 |                "console": "integratedTerminal"
319 |            },
320 |            {
321 |                "name": "Run Module 3",
322 |                "type": "python",
323 |                "request": "launch",
324 |                "program": "${workspaceFolder}/module3/src/finalize_markdown_server/__main__.py",
325 |                "console": "integratedTerminal"
326 |            }
327 |        ]
328 |    }
329 |    ```
330 | 
331 | 2. Use **MCP Inspector**:
332 |    - Start a server in the terminal:
333 |      ```bash
334 |      npx @modelcontextprotocol/inspector uv --directory module1/src/create_markdown_server run create_markdown_server
335 |      ```
336 |    - Repeat for Modules 2 and 3.
337 | 
338 | ---
339 | 
340 | ### **Step 6: Initialize and Test**
341 | I will now initialize the project structure with placeholder files for each module and create a test flow for user interaction across the pipeline. Let me scaffold and finalize the initial setup.
342 | 
343 | The project structure for **`mcp-hello`** has been successfully initialized with the following components:
344 | 
345 | ### Project Structure
346 | ```plaintext
347 | mcp-hello/
348 | ├── module1/                # First module: Creates a markdown file
349 | │   ├── src/
350 | │   │   ├── create_markdown_server/
351 | │   │       └── server.py   # Placeholder for Module 1 server logic
352 | ├── module2/                # Second module: Updates markdown file
353 | │   ├── src/
354 | │   │   ├── update_markdown_server/
355 | │   │       └── server.py   # Placeholder for Module 2 server logic
356 | ├── module3/                # Third module: Finalizes markdown file
357 | │   ├── src/
358 | │   │   ├── finalize_markdown_server/
359 | │   │       └── server.py   # Placeholder for Module 3 server logic
360 | ├── shared_logs/            # Shared logging directory for visibility
361 | ├── .vscode/                # VS Code configurations
362 | │   └── launch.json         # Debugging configurations for all modules
363 | └── README.md               # Documentation
364 | ```
365 | 
366 | ### Next Steps
367 | 1. Implement detailed logic in `server.py` for each module.
368 | 2. Configure `pyproject.toml` files for MCP server dependencies in each module.
369 | 3. Add comprehensive logging and test communication across modules using MCP Inspector.
370 | 
371 | Shall I proceed with implementing the server logic for **Module 1**?
372 | 
373 | ---------------
374 | 
375 | ````
376 | import os
377 | import logging
378 | from mcp.server import Server
379 | from pydantic import BaseModel
380 | 
381 | # Set up logging
382 | LOG_DIR = "../../shared_logs/"
383 | os.makedirs(LOG_DIR, exist_ok=True)
384 | 
385 | logging.basicConfig(
386 |     filename=os.path.join(LOG_DIR, "module1.log"),
387 |     level=logging.DEBUG,
388 |     format="%(asctime)s - %(levelname)s - %(message)s",
389 | )
390 | logger = logging.getLogger(__name__)
391 | 
392 | # Initialize the MCP server
393 | server = Server("MarkdownCreator")
394 | 
395 | # Define input model
396 | class MarkdownInput(BaseModel):
397 |     content: str
398 |     filename: str = "output.md"
399 | 
400 | @server.call_tool()
401 | async def create_markdown(arguments: dict):
402 |     """Creates a markdown file with the provided content."""
403 |     try:
404 |         # Parse arguments using the input model
405 |         input_data = MarkdownInput(**arguments)
406 |         filepath = os.path.join("../../", input_data.filename)
407 | 
408 |         # Write content to the markdown file
409 |         with open(filepath, "w") as file:
410 |             file.write(input_data.content)
411 | 
412 |         logger.info(f"Markdown file created: {filepath}")
413 |         return {"status": "success", "file": input_data.filename}
414 |     except Exception as e:
415 |         logger.error(f"Error creating markdown file: {e}")
416 |         raise e
417 | 
418 | if __name__ == "__main__":
419 |     logger.info("Starting Markdown Creator Server...")
420 |     server.run()
421 | ```
422 | 
423 | MESSAGE:
424 | 
425 | The server logic for **Module 1** has been implemented in `server.py`. Here's a summary of its functionality:
426 | 
427 | ---
428 | 
429 | ### **Features of Module 1: Markdown Creator**
430 | 1. **Receives User Input**:
431 |    - Accepts markdown `content` and optional `filename` (default: `output.md`).
432 |    
433 | 2. **Creates a Markdown File**:
434 |    - Writes the provided content to a markdown file in the project root directory.
435 | 
436 | 3. **Logs Operations**:
437 |    - Logs file creation and any errors to `module1.log` in the `shared_logs/` directory.
438 | 
439 | 4. **Returns Status**:
440 |    - Confirms successful file creation or raises an error if something goes wrong.
441 | 
442 | ---
443 | 
444 | ### **Next Steps**
445 | 1. Configure and test **Module 1** using MCP Inspector.
446 | 2. Proceed to implement **Module 2** logic for updating the markdown file.
447 | 
448 | Let me know if you’d like to proceed with testing or move on to **Module 2**.
449 | 
450 | ----------
451 | 
452 | Nuge: Please Configure and test Module 1 using MCP Inspector or tell me if you can not do that and give a recommendation for what to do instead.
453 | 
454 | 
455 | ----------
456 | 
457 | Unfortunately, I cannot directly run or test the server in your local environment using MCP Inspector. However, I can provide a detailed recommendation to help you configure and test Module 1 with MCP Inspector:
458 | 
459 | ---
460 | 
461 | ### **Steps to Test Module 1 Using MCP Inspector**
462 | 
463 | #### **1. Prerequisites**
464 | - Ensure you have **MCP Inspector** installed:
465 |   ```bash
466 |   npm install -g @modelcontextprotocol/inspector
467 |   ```
468 | 
469 | - Verify that all dependencies for Module 1 are installed:
470 |   ```bash
471 |   pip install create-mcp-server
472 |   pip install -r requirements.txt
473 |   ```
474 | 
475 | #### **2. Run the Server**
476 | Start the server for Module 1 in a terminal:
477 | ```bash
478 | cd mcp-hello/module1/src/create_markdown_server
479 | python server.py
480 | ```
481 | 
482 | Ensure that the server logs its startup message in `shared_logs/module1.log`.
483 | 
484 | ---
485 | 
486 | #### **3. Use MCP Inspector**
487 | Run MCP Inspector to inspect the server communication:
488 | ```bash
489 | npx @modelcontextprotocol/inspector uv --directory . run create_markdown_server
490 | ```
491 | 
492 | Once you start MCP Inspector, it will display a URL in the terminal (e.g., `http://localhost:3000`). Open this URL in a browser to visualize the interaction.
493 | 
494 | ---
495 | 
496 | #### **4. Test the Server**
497 | 1. Use the MCP Inspector interface to send a test request to the server:
498 |    - **Tool Name**: `create_markdown`
499 |    - **Arguments**:
500 |      ```json
501 |      {
502 |        "content": "## Sample Markdown Content",
503 |        "filename": "test.md"
504 |      }
505 |      ```
506 | 
507 | 2. Inspect the server response and verify the output:
508 |    - A success message in the Inspector.
509 |    - A new file `test.md` created in the `mcp-hello` root directory.
510 | 
511 | 3. Check the logs for detailed information about the request:
512 |    ```bash
513 |    cat ../../shared_logs/module1.log
514 |    ```
515 | 
516 | ---
517 | 
518 | #### **5. Troubleshooting**
519 | - **Server not starting?** Ensure all dependencies are installed and the server script path is correct.
520 | - **Inspector not connecting?** Verify that the MCP Inspector command points to the correct directory and server.
521 | - **File not created?** Check file permissions and ensure the `LOG_DIR` path is correct.
522 | 
523 | ---
524 | 
525 | If you encounter any specific issues during setup or testing, let me know, and I can guide you further!
526 | 
527 | ---------
528 | 
529 | The server logic for **Module 2** has been implemented in `server.py`. Here's a summary of its functionality:
530 | 
531 | ---
532 | 
533 | ### **Features of Module 2: Markdown Updater**
534 | 1. **Receives Input**:
535 |    - Accepts `filename` (the markdown file to update) and `additional_content` (text to append).
536 | 
537 | 2. **Updates Markdown File**:
538 |    - Checks if the specified file exists.
539 |    - Appends the provided content to the file.
540 | 
541 | 3. **Logs Operations**:
542 |    - Logs file updates and any errors to `module2.log` in the `shared_logs/` directory.
543 | 
544 | 4. **Returns Status**:
545 |    - Confirms successful file updates or raises an error if something goes wrong.
546 | 
547 | ---
548 | 
549 | ### **Next Steps**
550 | 1. Configure and test **Module 2** using MCP Inspector.
551 | 2. Proceed to implement **Module 3** logic for finalizing the markdown file.
552 | 
553 | Let me know if you’d like to proceed with testing or move on to **Module 3**.
554 | 
555 | ----------
556 | 
557 | --------------------------------
558 | 
559 | import os
560 | import logging
561 | from mcp.server import Server
562 | from pydantic import BaseModel
563 | 
564 | # Set up logging
565 | LOG_DIR = "../../shared_logs/"
566 | os.makedirs(LOG_DIR, exist_ok=True)
567 | 
568 | logging.basicConfig(
569 |     filename=os.path.join(LOG_DIR, "module3.log"),
570 |     level=logging.DEBUG,
571 |     format="%(asctime)s - %(levelname)s - %(message)s",
572 | )
573 | logger = logging.getLogger(__name__)
574 | 
575 | # Initialize the MCP server
576 | server = Server("MarkdownFinalizer")
577 | 
578 | # Define input model
579 | class MarkdownFinalizeInput(BaseModel):
580 |     filename: str
581 |     footer: str
582 | 
583 | @server.call_tool()
584 | async def finalize_markdown(arguments: dict):
585 |     """Finalizes a markdown file by adding a footer."""
586 |     try:
587 |         # Parse arguments using the input model
588 |         input_data = MarkdownFinalizeInput(**arguments)
589 |         filepath = os.path.join("../../", input_data.filename)
590 | 
591 |         # Check if the file exists
592 |         if not os.path.exists(filepath):
593 |             raise FileNotFoundError(f"File not found: {input_data.filename}")
594 | 
595 |         # Append the footer to the file
596 |         with open(filepath, "a") as file:
597 |             file.write(f"\n\n{input_data.footer}")
598 | 
599 |         logger.info(f"Markdown file finalized: {filepath}")
600 |         return {"status": "success", "file": input_data.filename}
601 |     except Exception as e:
602 |         logger.error(f"Error finalizing markdown file: {e}")
603 |         raise e
604 | 
605 | if __name__ == "__main__":
606 |     logger.info("Starting Markdown Finalizer Server...")
607 |     server.run()
608 | 
609 | 
610 |  The server logic for **Module 3** has been implemented in `server.py`. Here's a summary of its functionality:
611 | 
612 | ---
613 | 
614 | ### **Features of Module 3: Markdown Finalizer**
615 | 1. **Receives Input**:
616 |    - Accepts `filename` (the markdown file to finalize) and `footer` (text to append as the footer).
617 | 
618 | 2. **Finalizes Markdown File**:
619 |    - Checks if the specified file exists.
620 |    - Appends the provided footer at the end of the file, separated by two newlines.
621 | 
622 | 3. **Logs Operations**:
623 |    - Logs file finalization and any errors to `module3.log` in the `shared_logs/` directory.
624 | 
625 | 4. **Returns Status**:
626 |    - Confirms successful file finalization or raises an error if something goes wrong.
627 | 
628 | ---
629 | 
630 | ### **Next Steps**
631 | 1. **Testing**:
632 |    - Use MCP Inspector or manual requests to test the server.
633 |    - Simulate the complete workflow by running all three modules in sequence.
634 | 
635 | 2. **Integration**:
636 |    - Link Module 3 with the output of Module 2 to form the complete processing pipeline.
637 | 
638 | 3. **Refinements**:
639 |    - Add more error handling, if necessary.
640 |    - Optimize logging or expand logging detail based on initial test results.
641 | 
642 | Let me know if you’d like to proceed with testing, integration, or further refinements!
643 | 


--------------------------------------------------------------------------------
/Gemini.md:
--------------------------------------------------------------------------------
  1 | # Gemini 1.5 Experimental 1206
  2 | 
  3 | Okay, I understand the structure of the Model Context Protocol documentation and files provided. I can see that `create-mcp-server` is a tool for scaffolding new MCP server projects in Python. I also understand the basic folder structure and the purpose of the various configuration files.
  4 | 
  5 | The test project you described with three servers (markdown file creation, file modification, and file export) sounds like a good starting point to test the core functionality of MCP in a modular way, demonstrating resource creation, updates, and content retrieval across different "services".
  6 | 
  7 | Here's a breakdown of how I understand the proposed test project and how we can implement it using `create-mcp-server`:
  8 | 
  9 | **Project Structure**
 10 | 
 11 | We'll create a project directory containing three subdirectories, one for each server. Each server will be a separate, independent MCP server.
 12 | 
 13 | ```
 14 | mcp_test_project/
 15 | ├── server_1/  # Creates markdown files
 16 | ├── server_2/  # Modifies markdown files
 17 | └── server_3/  # Further modifies markdown files
 18 | ```
 19 | 
 20 | **Server 1: Markdown File Creation**
 21 | 
 22 | *   **Functionality:** This server will take user input text, add it to a content template, and save the result as a markdown file (e.g., `output_1.md`) in the root directory.
 23 | *   **Implementation:**
 24 |     *   We'll use `create-mcp-server` to generate the basic structure.
 25 |     *   The server will expose a `create-markdown` tool that accepts the user input and a content template.
 26 |     *   The tool will use the template and input to generate the markdown content.
 27 |     *   The content will be saved to a new markdown file (e.g. `output_1.md`) in the root directory.
 28 | 
 29 | **Server 2: Markdown File Modification**
 30 | 
 31 | *   **Functionality:** This server will read an existing markdown file (e.g., `output_1.md`), add more information to it, and save the updated version (e.g., `output_2.md`) to the root directory.
 32 | *   **Implementation:**
 33 |     *   We'll use `create-mcp-server` to generate the basic structure.
 34 |     *   The server will expose a `modify-markdown` tool that accepts a file path and additional information.
 35 |     *   The tool will read the specified markdown file.
 36 |     *   It will append the new information to the existing content.
 37 |     *   The modified content will be saved to a new markdown file (e.g. `output_2.md`) in the root directory.
 38 | 
 39 | **Server 3: Further Markdown File Modification**
 40 | 
 41 | *   **Functionality:** This server will likewise read an existing markdown file (e.g., `output_2.md`), add still more information to it, and save the updated version (e.g., `output_3.md`) to the root directory.
 42 | *   **Implementation:**
 43 |     *   We'll use `create-mcp-server` to generate the basic structure.
 44 |     *   The server will expose a `modify-markdown` tool that accepts a file path and additional information.
 45 |     *   The tool will read the specified markdown file.
 46 |     *   It will append the new information to the existing content.
 47 |     *   The modified content will be saved to a new markdown file (e.g. `output_3.md`) in the root directory.
 48 | 
 49 | **Shared Environment**
 50 | 
 51 | *   For this test, we can use a single virtual environment to manage dependencies for all three servers. This simplifies setup for this initial test but still preserves the modularity of each server.
 52 | *   We can install `create-mcp-server` and `mcp` within this environment.
 53 | 
 54 | **VS Code and macOS**
 55 | 
 56 | *   We'll use VS Code as the development environment on your macOS system.
 57 | *   We'll configure each server to run using the `uv` command within VS Code.
 58 | 
 59 | **Next Steps**
 60 | 
 61 | 1. **Set up the environment:** I'll guide you on creating the virtual environment and installing the necessary packages.
 62 | 2. **Generate server stubs:** We'll use `create-mcp-server` to generate the basic structure for each server.
 63 | 3. **Implement server logic:** We'll implement the specific tool logic for each server, including file I/O and markdown manipulation.
 64 | 4. **Test the setup:** We'll manually test each server using a tool like `mcp-inspector` and then try interacting with them using the Claude desktop app.
 65 | 
 66 | I'm ready to help you implement this test project. Please let me know when you're ready to proceed with the setup and implementation, and I'll provide you with the specific commands and code snippets.
 67 | 
 68 | ------------------
 69 | 
 70 | Nudge: Ready!  Let us do this and please  include info on using inspector to see what is happening and include lots of good logging for visibility.
 71 | 
 72 | 
 73 | ------------------
 74 | 
 75 | Okay, let's get started! Here's a step-by-step guide to set up the environment, create the servers, implement the logic, and test them using `mcp-inspector` with detailed logging.
 76 | 
 77 | **Step 1: Environment Setup**
 78 | 
 79 | 1. **Create Project Directory:**
 80 |     ```bash
 81 |     mkdir mcp_test_project
 82 |     cd mcp_test_project
 83 |     ```
 84 | 
 85 | 2. **Create Virtual Environment:**
 86 |     ```bash
 87 |     uv venv
 88 |     ```
 89 |     This creates a virtual environment in a hidden directory named `.venv`
 90 | 
 91 | 3. **Activate Virtual Environment:**
 92 |     *   **macOS:**
 93 |         ```bash
 94 |         source .venv/bin/activate
 95 |         ```
 96 |    You'll see `(.venv)` prepended to your terminal prompt, indicating the virtual environment is active.
 97 | 
 98 | 4. **Install `create-mcp-server`:**
 99 |     ```bash
100 |     uv pip install create-mcp-server mcp
101 |     ```
102 |    This installs the `create-mcp-server` package along with the `mcp` library into your virtual environment.
103 | 
104 | **Step 2: Create Server Projects**
105 | 
106 | We'll generate the basic structure for each server using `create-mcp-server`. Run these commands from the `mcp_test_project` directory:
107 | 
108 | 1. **Server 1 (Markdown Creator):**
109 | 
110 |     ```bash
111 |     uvx create-mcp-server server_1
112 |     ```
113 | 
114 |     When prompted, provide the following:
115 |     *   Project Name: `markdown-creator`
116 |     *   Project Description: `Creates markdown files from user input`
117 |     *   Server Version: (Leave default: `0.1.0`)
118 |     *   Enable Claude.app integration?: `y`
119 | 
120 | 2. **Server 2 (Markdown Modifier):**
121 | 
122 |     ```bash
123 |     uvx create-mcp-server server_2
124 |     ```
125 | 
126 |     When prompted, provide the following:
127 |     *   Project Name: `markdown-modifier`
128 |     *   Project Description: `Modifies existing markdown files`
129 |     *   Server Version: (Leave default: `0.1.0`)
130 |     *   Enable Claude.app integration?: `y`
131 | 
132 | 3. **Server 3 (Markdown Modifier):**
133 | 
134 |     ```bash
135 |     uvx create-mcp-server server_3
136 |     ```
137 | 
138 |     When prompted, provide the following:
139 |     *   Project Name: `markdown-modifier2`
140 |     *   Project Description: `Modifies existing markdown files`
141 |     *   Server Version: (Leave default: `0.1.0`)
142 |     *   Enable Claude.app integration?: `y`
143 | 
144 | Now your project structure should look like this:
145 | 
146 | ```
147 | mcp_test_project/
148 | ├── server_1/
149 | │   ├── pyproject.toml
150 | │   └── src/
151 | │       └── markdown_creator/
152 | │           ├── __init__.py
153 | │           ├── __main__.py
154 | │           └── server.py
155 | ├── server_2/
156 | │   ├── pyproject.toml
157 | │   └── src/
158 | │       └── markdown_modifier/
159 | │           ├── __init__.py
160 | │           ├── __main__.py
161 | │           └── server.py
162 | └── server_3/
163 |     ├── pyproject.toml
164 |     └── src/
165 |         └── markdown_modifier2/
166 |             ├── __init__.py
167 |             ├── __main__.py
168 |             └── server.py
169 | ```
170 | 
171 | **Step 3: Implement Server Logic**
172 | 
173 | We will replace the contents of `server.py` in each of the server directories with the following code:
174 | 
175 | **server_1/src/markdown_creator/server.py:**
176 | 
177 | ```python
178 | import logging
179 | import os
180 | from pathlib import Path
181 | 
182 | import anyio
183 | import mcp.types as types
184 | from mcp.server import Server
185 | from pydantic import BaseModel, Field
186 | 
187 | # Server setup
188 | server = Server("markdown-creator")
189 | logger = logging.getLogger(__name__)
190 | 
191 | # Ensure the output directory exists
192 | OUTPUT_DIR = Path("./")
193 | OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
194 | 
195 | class CreateMarkdownArgs(BaseModel):
196 |     content: str = Field(..., description="The main content of the markdown file.")
197 |     template: str = Field(..., description="A content template for the markdown file.")
198 | 
199 | @server.tool()
200 | async def create_markdown(arguments: CreateMarkdownArgs) -> list[types.TextContent]:
201 |     """
202 |     Creates a markdown file based on a template and adds content to it.
203 |     """
204 |     logger.info(f"Creating markdown file with content: {arguments.content}")
205 | 
206 |     # Generate the content using the template
207 |     markdown_content = f"{arguments.template}\n\n{arguments.content}"
208 | 
209 |     # Determine the next file number
210 |     existing_files = [f for f in OUTPUT_DIR.glob("output_*.md") if f.is_file()]
211 |     next_number = len(existing_files) + 1
212 |     file_path = OUTPUT_DIR / f"output_{next_number}.md"
213 | 
214 |     # Write to the file
215 |     try:
216 |         file_path.write_text(markdown_content, encoding="utf-8")
217 |         return [
218 |             types.TextContent(
219 |                 type="text", text=f"Created file: {file_path.name}"
220 |             )
221 |         ]
222 |     except Exception as e:
223 |         logger.error(f"Error creating file: {e}")
224 |         return [
225 |             types.TextContent(type="text", text=f"Error creating file: {e}")
226 |         ]
227 | 
228 | async def run():
229 |     # Run the server using stdio
230 |     async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
231 |         await server.run(
232 |             read_stream,
233 |             write_stream,
234 |             server.create_initialization_options(),
235 |         )
236 | 
237 | def main():
238 |     # Set up logging
239 |     logging.basicConfig(level=logging.INFO)
240 | 
241 |     # Run the async event loop
242 |     anyio.run(run)
243 | 
244 | if __name__ == "__main__":
245 |     main()
246 | ```
247 | 
248 | **server_2/src/markdown_modifier/server.py:**
249 | 
250 | ```python
251 | import logging
252 | import os
253 | from pathlib import Path
254 | 
255 | import anyio
256 | import mcp.types as types
257 | from mcp.server import Server
258 | from pydantic import BaseModel, Field
259 | 
260 | # Server setup
261 | server = Server("markdown-modifier")
262 | logger = logging.getLogger(__name__)
263 | 
264 | # Ensure the output directory exists
265 | OUTPUT_DIR = Path("./")
266 | OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
267 | 
268 | class ModifyMarkdownArgs(BaseModel):
269 |     file_path: str = Field(..., description="Path to the markdown file to modify.")
270 |     additional_info: str = Field(..., description="Additional information to add to the file.")
271 | 
272 | @server.tool()
273 | async def modify_markdown(arguments: ModifyMarkdownArgs) -> list[types.TextContent]:
274 |     """
275 |     Modifies an existing markdown file by appending additional information.
276 |     """
277 |     logger.info(f"Modifying markdown file: {arguments.file_path}")
278 | 
279 |     file_path = OUTPUT_DIR / arguments.file_path
280 | 
281 |     # Check if the file exists
282 |     if not file_path.exists():
283 |         return [
284 |             types.TextContent(type="text", text=f"Error: File not found: {arguments.file_path}")
285 |         ]
286 | 
287 |     try:
288 |         # Read existing content
289 |         existing_content = file_path.read_text(encoding="utf-8")
290 | 
291 |         # Append additional information
292 |         updated_content = f"{existing_content}\n\n{arguments.additional_info}"
293 | 
294 |         # Determine the next file number for the modified file
295 |         existing_files = [f for f in OUTPUT_DIR.glob("output_*.md") if f.is_file()]
296 |         next_number = len(existing_files) + 1
297 |         new_file_path = OUTPUT_DIR / f"output_{next_number}.md"
298 | 
299 |         # Write updated content to a new file
300 |         new_file_path.write_text(updated_content, encoding="utf-8")
301 | 
302 |         return [
303 |             types.TextContent(
304 |                 type="text", text=f"Modified file saved as: {new_file_path.name}"
305 |             )
306 |         ]
307 |     except Exception as e:
308 |         logger.error(f"Error modifying file: {e}")
309 |         return [
310 |             types.TextContent(type="text", text=f"Error modifying file: {e}")
311 |         ]
312 | 
313 | async def run():
314 |     # Run the server using stdio
315 |     async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
316 |         await server.run(
317 |             read_stream,
318 |             write_stream,
319 |             server.create_initialization_options(),
320 |         )
321 | 
322 | def main():
323 |     # Set up logging
324 |     logging.basicConfig(level=logging.INFO)
325 | 
326 |     # Run the async event loop
327 |     anyio.run(run)
328 | 
329 | if __name__ == "__main__":
330 |     main()
331 | ```
332 | 
333 | **server_3/src/markdown_modifier2/server.py:**
334 | 
335 | ```python
336 | import logging
337 | import os
338 | from pathlib import Path
339 | 
340 | import anyio
341 | import mcp.types as types
342 | from mcp.server import Server
343 | from pydantic import BaseModel, Field
344 | 
345 | # Server setup
346 | server = Server("markdown-modifier2")
347 | logger = logging.getLogger(__name__)
348 | 
349 | # Ensure the output directory exists
350 | OUTPUT_DIR = Path("./")
351 | OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
352 | 
353 | class ModifyMarkdown2Args(BaseModel):
354 |     file_path: str = Field(..., description="Path to the markdown file to modify.")
355 |     additional_info: str = Field(..., description="Additional information to add to the file.")
356 | 
357 | @server.tool()
358 | async def modify_markdown_2(arguments: ModifyMarkdown2Args) -> list[types.TextContent]:
359 |     """
360 |     Modifies an existing markdown file by appending even more additional information.
361 |     """
362 |     logger.info(f"Modifying markdown file: {arguments.file_path}")
363 | 
364 |     file_path = OUTPUT_DIR / arguments.file_path
365 | 
366 |     # Check if the file exists
367 |     if not file_path.exists():
368 |         return [
369 |             types.TextContent(type="text", text=f"Error: File not found: {arguments.file_path}")
370 |         ]
371 | 
372 |     try:
373 |         # Read existing content
374 |         existing_content = file_path.read_text(encoding="utf-8")
375 | 
376 |         # Append additional information
377 |         updated_content = f"{existing_content}\n\n{arguments.additional_info}"
378 | 
379 |         # Determine the next file number for the modified file
380 |         existing_files = [f for f in OUTPUT_DIR.glob("output_*.md") if f.is_file()]
381 |         next_number = len(existing_files) + 1
382 |         new_file_path = OUTPUT_DIR / f"output_{next_number}.md"
383 | 
384 |         # Write updated content to a new file
385 |         new_file_path.write_text(updated_content, encoding="utf-8")
386 | 
387 |         return [
388 |             types.TextContent(
389 |                 type="text", text=f"Modified file saved as: {new_file_path.name}"
390 |             )
391 |         ]
392 |     except Exception as e:
393 |         logger.error(f"Error modifying file: {e}")
394 |         return [
395 |             types.TextContent(type="text", text=f"Error modifying file: {e}")
396 |         ]
397 | 
398 | async def run():
399 |     # Run the server using stdio
400 |     async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
401 |         await server.run(
402 |             read_stream,
403 |             write_stream,
404 |             server.create_initialization_options(),
405 |         )
406 | 
407 | def main():
408 |     # Set up logging
409 |     logging.basicConfig(level=logging.INFO)
410 | 
411 |     # Run the async event loop
412 |     anyio.run(run)
413 | 
414 | if __name__ == "__main__":
415 |     main()
416 | ```
417 | 
418 | **Explanation of Changes:**
419 | 
420 | *   **File I/O:** The `create_markdown` function now saves the generated markdown content to a file in the root directory. The `modify_markdown` function reads and updates an existing file.
421 | *   **Error Handling:** Basic error handling is included to catch file I/O issues.
422 | *   **Logging:** The `logger` is used to provide info and error messages.
423 | 
424 | **Step 4: Test with MCP Inspector**
425 | 
426 | 1. **Launch MCP Inspector:**
427 |     ```bash
428 |     npx @modelcontextprotocol/inspector
429 |     ```
430 |     This will open the MCP Inspector in your browser (usually at `http://localhost:5173`).
431 | 
432 | 2. **Connect to the Servers:**
433 |     *   In the Inspector, you will see three fields: `Command`, `Arguments`, and `Environment Variables`.
434 | 
435 |     *   **For `server_1`:**
436 |         *   **Command:** `uv`
437 |         *   **Arguments:**  `run mcp-simple-prompt`
438 |         *   **Environment Variables:** Leave empty
439 | 
440 |     *   **For `server_2`:**
441 |         *   **Command:** `uv`
442 |         *   **Arguments:**  `run mcp-simple-resource`
443 |         *   **Environment Variables:** Leave empty
444 |     *   **For `server_3`:**
445 |         *   **Command:** `uv`
446 |         *   **Arguments:**  `run mcp-simple-tool`
447 |         *   **Environment Variables:** Leave empty
448 | 
449 |     *   For each server's entry, click "Connect". The status should change to "connected". You will need to hit the `Format` button in the `Commands` box to get each server to connect.
450 | 
451 | 3. **Interact with the Servers:**
452 |     *   Go to the "Tools" tab. You should see the tool `create-markdown` listed for `server_1` and `modify-markdown` listed for `server_2`, and `modify_markdown_2` listed for `server_3`.
453 |     *   Select the `create-markdown` tool.
454 |     *   Enter values for the `content` and `template` fields.
455 |     *   Click "Call Tool".
456 |     *   You should see a response in the "Response" area indicating that the file was created.
457 |     *   Select the `modify-markdown` tool.
458 |     *   Enter a value for the `file_path` argument (e.g. `output_1.md`).
459 |     *   Enter a value for the `additional_info` argument.
460 |     *   Click "Call Tool".
461 |     *   You should see a response in the "Response" area indicating that the file was modified.
462 |     *   Repeat the prior two steps but with the `modify_markdown_2` tool and the `output_2.md` file.
463 |     *   Open the `output_3.md` file in the root directory to verify the contents.
464 | 
465 | **Step 5: Test with Claude Desktop**
466 | 
467 | 1. **Configure Claude Desktop:**
468 |     *   Go to your Claude Desktop configuration file (`claude_desktop_config.json`).
469 |     *   Add entries for each server under `mcpServers` :
470 | 
471 |     ```json
472 |     "mcpServers": {
473 |         "markdown-creator": {
474 |           "command": "uv",
475 |           "args": ["--directory", "server_1", "run", "mcp-simple-prompt"],
476 |           "env": {}
477 |         },
478 |         "markdown-modifier": {
479 |           "command": "uv",
480 |           "args": ["--directory", "server_2", "run", "mcp-simple-resource"],
481 |           "env": {}
482 |         },
483 |         "markdown-modifier2": {
484 |           "command": "uv",
485 |           "args": ["--directory", "server_3", "run", "mcp-simple-tool"],
486 |           "env": {}
487 |         }
488 |     }
489 |     ```
490 | 
491 |     Make sure to replace `"server_1"`, `"server_2"`, and `"server_3"` with the correct paths to your server directories.
492 | 
493 | 2. **Restart Claude Desktop:**
494 |     *   Completely quit and restart the Claude Desktop application.
495 | 
496 | 3. **Interact with the Servers:**
497 |     *   In a new conversation, use the 🔌 icon to select a server and see its tools.
498 |     *   Invoke the tools using their names and providing necessary arguments.
499 | 
500 | **Example Claude Conversation:**
501 | 
502 | > **User:** /tools
503 | 
504 | *Claude will show the available tools. You can select `create-markdown`.*
505 | 
506 | > **Claude:** (Provides inputs for `content` and `template`)
507 | >
508 | > **User:**
509 | >
510 | > ```json
511 | > {
512 | >   "content": "This is the initial content.",
513 | >   "template": "# My Document\n\n{content}"
514 | > }
515 | > ```
516 | 
517 | *Claude should respond, indicating that `output_1.md` was created.*
518 | 
519 | > **User:** /tools
520 | 
521 | *Claude will show the available tools. You can select `modify-markdown`.*
522 | 
523 | > **Claude:** (Provides inputs for `file_path` and `additional_info`)
524 | >
525 | > **User:**
526 | >
527 | > ```json
528 | > {
529 | >   "file_path": "output_1.md",
530 | >   "additional_info": "This is additional information appended to the file."
531 | > }
532 | > ```
533 | 
534 | *Claude should respond, indicating that `output_2.md` was created.*
535 | 
536 | > **User:** /tools
537 | 
538 | *Claude will show the available tools. You can select `modify_markdown_2`.*
539 | 
540 | > **Claude:** (Provides inputs for `file_path` and `additional_info`)
541 | >
542 | > **User:**
543 | >
544 | > ```json
545 | > {
546 | >   "file_path": "output_2.md",
547 | >   "additional_info": "This is even more additional information appended to the file."
548 | > }
549 | > ```
550 | 
551 | *Claude should respond, indicating that `output_3.md` was created.*
552 | 
553 | You have now successfully set up and tested a modular MCP project with three servers! You can expand on this by adding more complex tools and interactions. Remember to consult the MCP documentation for details on the protocol's features and capabilities. Let me know if you want to make changes to the project or explore more advanced MCP features.
554 | 


--------------------------------------------------------------------------------
/LICENSE:
--------------------------------------------------------------------------------
  1 |                                  Apache License
  2 |                            Version 2.0, January 2004
  3 |                         http://www.apache.org/licenses/
  4 | 
  5 |    TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION
  6 | 
  7 |    1. Definitions.
  8 | 
  9 |       "License" shall mean the terms and conditions for use, reproduction,
 10 |       and distribution as defined by Sections 1 through 9 of this document.
 11 | 
 12 |       "Licensor" shall mean the copyright owner or entity authorized by
 13 |       the copyright owner that is granting the License.
 14 | 
 15 |       "Legal Entity" shall mean the union of the acting entity and all
 16 |       other entities that control, are controlled by, or are under common
 17 |       control with that entity. For the purposes of this definition,
 18 |       "control" means (i) the power, direct or indirect, to cause the
 19 |       direction or management of such entity, whether by contract or
 20 |       otherwise, or (ii) ownership of fifty percent (50%) or more of the
 21 |       outstanding shares, or (iii) beneficial ownership of such entity.
 22 | 
 23 |       "You" (or "Your") shall mean an individual or Legal Entity
 24 |       exercising permissions granted by this License.
 25 | 
 26 |       "Source" form shall mean the preferred form for making modifications,
 27 |       including but not limited to software source code, documentation
 28 |       source, and configuration files.
 29 | 
 30 |       "Object" form shall mean any form resulting from mechanical
 31 |       transformation or translation of a Source form, including but
 32 |       not limited to compiled object code, generated documentation,
 33 |       and conversions to other media types.
 34 | 
 35 |       "Work" shall mean the work of authorship, whether in Source or
 36 |       Object form, made available under the License, as indicated by a
 37 |       copyright notice that is included in or attached to the work
 38 |       (an example is provided in the Appendix below).
 39 | 
 40 |       "Derivative Works" shall mean any work, whether in Source or Object
 41 |       form, that is based on (or derived from) the Work and for which the
 42 |       editorial revisions, annotations, elaborations, or other modifications
 43 |       represent, as a whole, an original work of authorship. For the purposes
 44 |       of this License, Derivative Works shall not include works that remain
 45 |       separable from, or merely link (or bind by name) to the interfaces of,
 46 |       the Work and Derivative Works thereof.
 47 | 
 48 |       "Contribution" shall mean any work of authorship, including
 49 |       the original version of the Work and any modifications or additions
 50 |       to that Work or Derivative Works thereof, that is intentionally
 51 |       submitted to Licensor for inclusion in the Work by the copyright owner
 52 |       or by an individual or Legal Entity authorized to submit on behalf of
 53 |       the copyright owner. For the purposes of this definition, "submitted"
 54 |       means any form of electronic, verbal, or written communication sent
 55 |       to the Licensor or its representatives, including but not limited to
 56 |       communication on electronic mailing lists, source code control systems,
 57 |       and issue tracking systems that are managed by, or on behalf of, the
 58 |       Licensor for the purpose of discussing and improving the Work, but
 59 |       excluding communication that is conspicuously marked or otherwise
 60 |       designated in writing by the copyright owner as "Not a Contribution."
 61 | 
 62 |       "Contributor" shall mean Licensor and any individual or Legal Entity
 63 |       on behalf of whom a Contribution has been received by Licensor and
 64 |       subsequently incorporated within the Work.
 65 | 
 66 |    2. Grant of Copyright License. Subject to the terms and conditions of
 67 |       this License, each Contributor hereby grants to You a perpetual,
 68 |       worldwide, non-exclusive, no-charge, royalty-free, irrevocable
 69 |       copyright license to reproduce, prepare Derivative Works of,
 70 |       publicly display, publicly perform, sublicense, and distribute the
 71 |       Work and such Derivative Works in Source or Object form.
 72 | 
 73 |    3. Grant of Patent License. Subject to the terms and conditions of
 74 |       this License, each Contributor hereby grants to You a perpetual,
 75 |       worldwide, non-exclusive, no-charge, royalty-free, irrevocable
 76 |       (except as stated in this section) patent license to make, have made,
 77 |       use, offer to sell, sell, import, and otherwise transfer the Work,
 78 |       where such license applies only to those patent claims licensable
 79 |       by such Contributor that are necessarily infringed by their
 80 |       Contribution(s) alone or by combination of their Contribution(s)
 81 |       with the Work to which such Contribution(s) was submitted. If You
 82 |       institute patent litigation against any entity (including a
 83 |       cross-claim or counterclaim in a lawsuit) alleging that the Work
 84 |       or a Contribution incorporated within the Work constitutes direct
 85 |       or contributory patent infringement, then any patent licenses
 86 |       granted to You under this License for that Work shall terminate
 87 |       as of the date such litigation is filed.
 88 | 
 89 |    4. Redistribution. You may reproduce and distribute copies of the
 90 |       Work or Derivative Works thereof in any medium, with or without
 91 |       modifications, and in Source or Object form, provided that You
 92 |       meet the following conditions:
 93 | 
 94 |       (a) You must give any other recipients of the Work or
 95 |           Derivative Works a copy of this License; and
 96 | 
 97 |       (b) You must cause any modified files to carry prominent notices
 98 |           stating that You changed the files; and
 99 | 
100 |       (c) You must retain, in the Source form of any Derivative Works
101 |           that You distribute, all copyright, patent, trademark, and
102 |           attribution notices from the Source form of the Work,
103 |           excluding those notices that do not pertain to any part of
104 |           the Derivative Works; and
105 | 
106 |       (d) If the Work includes a "NOTICE" text file as part of its
107 |           distribution, then any Derivative Works that You distribute must
108 |           include a readable copy of the attribution notices contained
109 |           within such NOTICE file, excluding those notices that do not
110 |           pertain to any part of the Derivative Works, in at least one
111 |           of the following places: within a NOTICE text file distributed
112 |           as part of the Derivative Works; within the Source form or
113 |           documentation, if provided along with the Derivative Works; or,
114 |           within a display generated by the Derivative Works, if and
115 |           wherever such third-party notices normally appear. The contents
116 |           of the NOTICE file are for informational purposes only and
117 |           do not modify the License. You may add Your own attribution
118 |           notices within Derivative Works that You distribute, alongside
119 |           or as an addendum to the NOTICE text from the Work, provided
120 |           that such additional attribution notices cannot be construed
121 |           as modifying the License.
122 | 
123 |       You may add Your own copyright statement to Your modifications and
124 |       may provide additional or different license terms and conditions
125 |       for use, reproduction, or distribution of Your modifications, or
126 |       for any such Derivative Works as a whole, provided Your use,
127 |       reproduction, and distribution of the Work otherwise complies with
128 |       the conditions stated in this License.
129 | 
130 |    5. Submission of Contributions. Unless You explicitly state otherwise,
131 |       any Contribution intentionally submitted for inclusion in the Work
132 |       by You to the Licensor shall be under the terms and conditions of
133 |       this License, without any additional terms or conditions.
134 |       Notwithstanding the above, nothing herein shall supersede or modify
135 |       the terms of any separate license agreement you may have executed
136 |       with Licensor regarding such Contributions.
137 | 
138 |    6. Trademarks. This License does not grant permission to use the trade
139 |       names, trademarks, service marks, or product names of the Licensor,
140 |       except as required for reasonable and customary use in describing the
141 |       origin of the Work and reproducing the content of the NOTICE file.
142 | 
143 |    7. Disclaimer of Warranty. Unless required by applicable law or
144 |       agreed to in writing, Licensor provides the Work (and each
145 |       Contributor provides its Contributions) on an "AS IS" BASIS,
146 |       WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
147 |       implied, including, without limitation, any warranties or conditions
148 |       of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
149 |       PARTICULAR PURPOSE. You are solely responsible for determining the
150 |       appropriateness of using or redistributing the Work and assume any
151 |       risks associated with Your exercise of permissions under this License.
152 | 
153 |    8. Limitation of Liability. In no event and under no legal theory,
154 |       whether in tort (including negligence), contract, or otherwise,
155 |       unless required by applicable law (such as deliberate and grossly
156 |       negligent acts) or agreed to in writing, shall any Contributor be
157 |       liable to You for damages, including any direct, indirect, special,
158 |       incidental, or consequential damages of any character arising as a
159 |       result of this License or out of the use or inability to use the
160 |       Work (including but not limited to damages for loss of goodwill,
161 |       work stoppage, computer failure or malfunction, or any and all
162 |       other commercial damages or losses), even if such Contributor
163 |       has been advised of the possibility of such damages.
164 | 
165 |    9. Accepting Warranty or Additional Liability. While redistributing
166 |       the Work or Derivative Works thereof, You may choose to offer,
167 |       and charge a fee for, acceptance of support, warranty, indemnity,
168 |       or other liability obligations and/or rights consistent with this
169 |       License. However, in accepting such obligations, You may act only
170 |       on Your own behalf and on Your sole responsibility, not on behalf
171 |       of any other Contributor, and only if You agree to indemnify,
172 |       defend, and hold each Contributor harmless for any liability
173 |       incurred by, or claims asserted against, such Contributor by reason
174 |       of your accepting any such warranty or additional liability.
175 | 
176 |    END OF TERMS AND CONDITIONS
177 | 
178 |    APPENDIX: How to apply the Apache License to your work.
179 | 
180 |       To apply the Apache License to your work, attach the following
181 |       boilerplate notice, with the fields enclosed by brackets "[]"
182 |       replaced with your own identifying information. (Don't include
183 |       the brackets!)  The text should be enclosed in the appropriate
184 |       comment syntax for the file format. We also recommend that a
185 |       file or class name and description of purpose be included on the
186 |       same "printed page" as the copyright notice for easier
187 |       identification within third-party archives.
188 | 
189 |    Copyright [yyyy] [name of copyright owner]
190 | 
191 |    Licensed under the Apache License, Version 2.0 (the "License");
192 |    you may not use this file except in compliance with the License.
193 |    You may obtain a copy of the License at
194 | 
195 |        http://www.apache.org/licenses/LICENSE-2.0
196 | 
197 |    Unless required by applicable law or agreed to in writing, software
198 |    distributed under the License is distributed on an "AS IS" BASIS,
199 |    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
200 |    See the License for the specific language governing permissions and
201 |    limitations under the License.
202 | 


--------------------------------------------------------------------------------
/README.md:
--------------------------------------------------------------------------------
  1 | # MCP Multi-Agent Modular Awesomeness!
  2 | 
  3 | ![alt text](image.png)
  4 | 
  5 | ## Overview
  6 | 
  7 | This is a primative multi-agent modular initialization capability test prototype of Model Context Protocol.  My test project will have multiple servers and clients.  They will operate in a modular way, the first will create a markdown file based on adding user input text to a content template and saving the file to root directory.  The second will ingest that file and add more info to it then save the updated version to the root.  The alt A third will likewise ingest the output of the second and add still more content and export the third version of the file to the root.  The alt B third server alternatively could take another action.  Treat each of these three like back boxes in the sense that they will not share code or components but we will pretend they are running on different technologies to preserve the modular approach and we will for convenience be able to do things like share a virtual environment and requirements for this first test.  The second server will be a decider and will choose which is the best next server.
  8 | 
  9 | The notion of strict modularity such that different MCP interoperable system could be created and operated by totally different teams or even different companies is potentially a key unlock for MCP and for LLM based agents to take off and be scalable and more fully userful.  This is described more fully in the project overview for "Agent" here: [https://github.com/dazzaji/mcp-project/issues/1](https://github.com/dazzaji/mcp-project/issues/1). 
 10 | 
 11 | ## Try it!
 12 | 
 13 | Let's get your MCP project running in VS Code with the Inspector and Claude Desktop.
 14 | 
 15 | **1. Running in VS Code with MCP Inspector**
 16 | 
 17 | Here's how to run your project in VS Code and inspect the communication using MCP Inspector:
 18 | 
 19 | * **Install the `mcp` package:**  In your project root (`mcp-project`), ensure you have installed the MCP package in your active virtual environment:
 20 | 
 21 | ```bash
 22 | uv add mcp
 23 | ```
 24 | 
 25 | * **Set up `launch.json`**: You'll need launch configurations for each of your MCP servers.  Since you're simulating "black boxes" that *might* run different underlying technologies, the launch configuration will vary for the Gemini server.  Create a `.vscode/launch.json` file in your project's root directory with the following configurations.  This assumes the gemini-server takes a `model` parameter, which specifies the model to use.
 26 | 
 27 | ```json
 28 | {
 29 |     "version": "0.2.0",
 30 |     "configurations": [
 31 |         {
 32 |             "name": "Module 1 Server",
 33 |             "type": "python",
 34 |             "request": "launch",
 35 |             "module": "module1_server.server", // Use module mode for direct execution
 36 |             "console": "integratedTerminal"
 37 |         },
 38 |         {
 39 |             "name": "Gemini Server",
 40 |             "type": "python",
 41 |             "request": "launch",
 42 |             "program": "${workspaceFolder}/gemini-server/server.py",
 43 |             "args": ["--model", "gemini-pro"], // Example model argument
 44 |             "console": "integratedTerminal"
 45 |         }
 46 |     ]
 47 | }
 48 | ```
 49 | 
 50 | *   **Running the servers:**
 51 |     *   Open the `module1-server/server.py` file in VS Code.
 52 |     *   Start the debugger by pressing `F5` or selecting "Start Debugging" from the "Run" menu, and choose the `Module 1 Server` configuration. This will start the Module 1 server in the VS Code integrated terminal. In a similar way, start the `Gemini Server` in a separate terminal.
 53 |     *   In a new terminal at the root of your project, start the gateway agent with `uv run gateway_agent`.
 54 | 
 55 | 
 56 | *   **Start MCP Inspector:**
 57 |     *   Open a *new* terminal in the `gateway-agent` directory.
 58 |     *   Run the following command:
 59 | 
 60 |     ```bash
 61 |     npx @modelcontextprotocol/inspector python -m gateway_agent
 62 |     ```
 63 |     *   This starts the MCP Inspector, which automatically launches the gateway-agent server and the Inspector UI. A URL will be printed in the terminal. Open this URL in your browser to access the UI.
 64 | 
 65 |     *   In the Inspector UI, click on "Tools" to confirm the tools your gateway agent has registered.
 66 | 
 67 | Now you can interact with the servers through the MCP Inspector UI, sending requests and viewing responses and logs. The logging messages from your `service.py` file will appear in the Inspector's console, which can be useful for debugging.  You can test the routing functionality by calling the `route_task` tool with different inputs and observing which downstream server is called.
 68 | 
 69 | 
 70 | 
 71 | **2. Running with Claude Desktop**
 72 | 
 73 | To use your MCP servers with Claude Desktop:
 74 | 
 75 | *   **Install your servers** into your local environment or a Docker container. If you use Docker make sure both the gateway agent and servers A and B are all accessible on the same Docker network.
 76 | *   **Configure `claude_desktop_config.json`:**
 77 | 
 78 |     *   Locate your `claude_desktop_config.json` file (the path depends on your operating system; consult the MCP docs for details).
 79 | 
 80 |     *   Add configurations for your *gateway-agent* server under the `mcpServers` key. Since your gateway agent now uses HTTP/SSE, you will need to specify the URL accordingly.
 81 | 
 82 |         ```json
 83 |         {
 84 |           "mcpServers": {
 85 |             "gateway-agent": {
 86 |               "url": "http://localhost:8000/mcp/v1" // Replace with gateway agent url
 87 |             },
 88 |             "server-a": {
 89 |               "url": "http://localhost:5000/mcp/v1" // Replace with Server A url
 90 |             },
 91 |               "server-b": {
 92 |               "url": "http://localhost:5001/mcp/v1" // Replace with Server B url
 93 |             }
 94 |           }
 95 |         }
 96 |         ```
 97 | 
 98 |         Make sure the port numbers match the ports your servers are listening on.  Replace `/mcp/v1` with the actual endpoint if it's different.  Make sure to add server B analogous to server A, and start it on a different port. 
 99 | 
100 | *   **Restart Claude Desktop:** For the changes in your `claude_desktop_config.json` file to take effect, you need to restart Claude Desktop.
101 | 
102 | Now you should be able to interact with your gateway agent via Claude's slash commands or other UI elements provided by Claude Desktop to use MCP tools. You can test the routing by entering queries that should be directed to different servers.
103 | 
104 | With these steps, you should be able to run your MCP project, inspect server communications with the Inspector, and integrate your gateway agent with Claude Desktop! Let me know if you encounter any issues, and I'll help troubleshoot.
105 | 
106 | 
107 | ------
108 | 
109 | # Use Inspector to See What is Happening Under the Hood
110 | 
111 | Okay, here's a step-by-step guide to run your project and inspect the MCP traffic using the Inspector. We'll use Docker Compose to simplify the process since you have Dockerfiles. This approach ensures consistent environment setup and easier management of multiple services.
112 | 
113 | **Prerequisites:**
114 | 
115 | 1.  **Docker Desktop:** Make sure you have Docker Desktop installed and running.
116 | 2.  **Docker Compose:** Verify Docker Compose is installed. You can check with `docker compose version`. If not, install it according to the instructions for your OS.
117 | 3.  **MCP Inspector:** Ensure MCP Inspector is installed globally: `npm install -g @modelcontextprotocol/inspector`
118 | 4. **Anthropic API Key:** You'll need a valid Anthropic API key for both Server A and Server B (as they use Claude). Set this in an `.env` file in both the `server-a` and `server-b` directories. Note that your `.gitignore` is set up correctly to ignore `.env` files.
119 | 5. **Gemini API Key:** Similarly set up the `GEMINI_API_KEY` for the Gemini server in an `.env` file in the root of the project
120 | 
121 | **Steps:**
122 | 
123 | 1. **Prepare Server A and Server B:**
124 | 
125 | * **User Profile Data:** Create a `user_profile.json` file in both `server-a` and `server-b` with the user profile information you provided for each (health and professional profiles, respectively). Format this data as JSON. 
126 | 
127 | Here's how those files should be structured: 
128 | 
129 | `server-a/user_profile.json`:
130 | 
131 | ```json
132 | {
133 |   "name": "John Doey",
134 |   "date_of_birth": "August 15, 1997",
135 |   "gender": "Male",
136 |   "height": "5'8\"",
137 |   "weight": "150 lbs",
138 |   "bmi": 22.7,
139 |   "body_fat_percentage": 23.5,
140 |   "muscle_mass": "64.6 lbs",
141 |   "bone_mass": "7.1 lbs",
142 |   "last_measured_body_composition": "December 1, 2024",
143 |   "blood_pressure": "118/75 mmHg",
144 |   "heart_rate": 68,
145 |   "respiratory_rate": 14,
146 |   "last_measured_vital_signs": "December 9, 2024",
147 |   "weight_management_target": "150 lbs",
148 |   "weight_management_deadline": "June 30, 2025",
149 |   "weight_management_type": "Maintenance",
150 |   "daily_steps": 8000,
151 |   "weekly_exercise": "150 minutes",
152 |   "weekly_workouts": 3,
153 |   "daily_caloric_target": 2200,
154 |   "macronutrient_breakdown": {
155 |     "protein": "2.8 oz (80g)",
156 |     "carbohydrates": "8.8 oz (250g)",
157 |     "fats": "2.6 oz (73g)"
158 |   },
159 |   "current_conditions": [
160 |     {
161 |       "name": "Computer Vision Syndrome",
162 |       "diagnosed": "September 15, 2023",
163 |       "status": "Active",
164 |       "medications": null
165 |     },
166 |     {
167 |       "name": "Mild Anxiety",
168 |       "diagnosed": "March 20, 2023",
169 |       "status": "Active",
170 |       "treatment": {
171 |         "type": "Meditation App Subscription",
172 |         "duration": "15 minutes",
173 |         "frequency": "Daily",
174 |         "started": "March 25, 2023",
175 |         "ongoing": true
176 |       }
177 |     }
178 |   ],
179 |   "allergies": [
180 |     {
181 |       "name": "Tree Pollen",
182 |       "severity": "Mild",
183 |       "symptoms": ["Sneezing", "Itchy eyes"]
184 |     }
185 |   ],
186 |   "family_history": {
187 |     "type_2_diabetes": "Paternal grandfather",
188 |     "hypertension": "Maternal grandmother"
189 |   },
190 |   "preferences": {
191 |     "measurement_system": "Imperial",
192 |     "dietary_restrictions": ["Vegetarian", "Low-caffeine"],
193 |     "exercise_preferences": ["Yoga", "Running", "Home workouts"],
194 |     "reminders": true,
195 |     "progress_updates": true,
196 |     "health_tips": true
197 |   },
198 |   "last_updated": "December 10, 2024"
199 | }
200 | ```
201 | 
202 | `server-b/user_profile.json`:
203 | 
204 | ```json
205 | {
206 |   "name": "John Doey",
207 |   "user_id": "JP_AI_2024",
208 |   "current_role": "Machine Learning Engineer II",
209 |   "industry": "Artificial Intelligence",
210 |   "years_of_experience": 2,
211 |   "preferred_work_style": "Hybrid",
212 |   "current_position": {
213 |     "title": "Machine Learning Engineer II",
214 |     "band": "IC2",
215 |     "start_date": "January 15, 2024"
216 |   },
217 |   "technical_skills": [
218 |     {
219 |       "name": "PyTorch",
220 |       "proficiency": "Advanced",
221 |       "last_used": "December 9, 2024"
222 |     },
223 |     {
224 |       "name": "LLM Fine-tuning",
225 |       "proficiency": "Intermediate",
226 |       "last_used": "December 9, 2024"
227 |     },
228 |     {
229 |       "name": "MLOps",
230 |       "proficiency": "Intermediate",
231 |       "last_used": "December 8, 2024"
232 |     }
233 |   ],
234 |   "soft_skills": [
235 |     {
236 |       "name": "Technical Communication",
237 |       "self_assessment": 8,
238 |       "last_assessed": "November 30, 2024"
239 |     },
240 |     {
241 |       "name": "Project Management",
242 |       "self_assessment": 7,
243 |       "last_assessed": "November 30, 2024"
244 |     }
245 |   ],
246 |   "time_management": {
247 |     "preferred_hours": "9:30 AM - 6:30 PM (PST)",
248 |     "focus_time_blocks": {
249 |       "morning": "120-minute block"
250 |     }
251 |   },
252 |   "meeting_preferences": {
253 |     "maximum_daily_meetings": 4,
254 |     "preferred_duration": "30 minutes",
255 |     "buffer_time": "15 minutes"
256 |   },
257 |   "professional_goals": {
258 |     "short_term_objectives": [
259 |       {
260 |         "name": "LLM Evaluation Framework Project",
261 |         "role": "Project Lead",
262 |         "target_date": "March 30, 2025",
263 |         "status": "In Progress",
264 |         "type": "Project"
265 |       },
266 |       {
267 |         "name": "MLOps Certification",
268 |         "target_date": "February 28, 2025",
269 |         "status": "In Progress",
270 |         "type": "Certification"
271 |       }
272 |     ],
273 |     "long_term_objectives": {
274 |       "primary_goal": "Senior ML Engineer Role",
275 |       "target_year": 2026,
276 |       "key_milestones": [
277 |         "Lead 2 major technical initiatives (Due: December 31, 2025)",
278 |         "Develop team mentorship experience",
279 |         "Establish technical thought leadership"
280 |       ]
281 |     }
282 |   },
283 |     "development_activities": {
284 |     "current_projects": [
285 |       {
286 |         "name": "LLM Evaluation Framework",
287 |         "role": "Technical Lead",
288 |         "skills": ["ML Architecture", "Team Leadership"],
289 |         "visibility": "Company-wide"
290 |       },
291 |       {
292 |         "name": "Model Optimization Initiative",
293 |         "role": "Individual Contributor",
294 |         "skills": ["Performance Tuning", "MLOps"],
295 |         "visibility": "Department"
296 |       }
297 |     ],
298 |     "training_programs": [
299 |       {
300 |         "name": "MLOps Certification Program",
301 |         "provider": "Major Cloud Provider",
302 |         "status": "In Progress",
303 |         "expected_completion": "Q1 2025"
304 |       },
305 |       {
306 |         "name": "Technical Leadership Workshop",
307 |         "provider": "Internal L&D",
308 |         "status": "Planned",
309 |         "start_date": "January 2025"
310 |       }
311 |     ]
312 |   },
313 |   "learning_and_growth": {
314 |     "areas_of_focus": {
315 |       "technical": ["Large Language Models", "Distributed Systems", "ML Infrastructure"],
316 |       "leadership": ["Team Management", "Technical Project Planning", "Stakeholder Communication"]
317 |     },
318 |     "resources": [
319 |       "Internal ML Engineering Wiki",
320 |       "Technical Conference Presentations",
321 |       "Industry Research Papers",
322 |       "Team Knowledge Sharing Sessions"
323 |     ]
324 |   },
325 |   "professional_network_development": {
326 |     "current_activities": [
327 |       "Regular 1:1s with Senior Engineers",
328 |       "Monthly ML Community Meetups",
329 |       "Internal Tech Talks Participant",
330 |       "Open Source Contributions"
331 |     ],
332 |     "mentorship": {
333 |       "seeking_in": ["Technical Leadership", "Project Management"],
334 |       "providing_in": ["PyTorch", "LLM Implementation"]
335 |     }
336 |   },
337 |   "preferences": {
338 |     "learning_style": ["Hands-on Implementation", "Documentation Creation", "Collaborative Problem-solving"],
339 |     "growth_areas": ["System Architecture Design", "Team Leadership", "Technical Writing"],
340 |     "goal_reminders": true,
341 |     "networking_opportunities": true,
342 |     "learning_recommendations": true
343 |   },
344 |   "last_updated": "December 10, 2024"
345 | }
346 | ```
347 | 
348 | 
349 | 
350 | * **Install Dependencies:** Make sure all the servers have the needed dependencies:
351 | 
352 |   ```bash
353 |   cd server-a
354 |   pip install -r requirements.txt # Install dependencies for server-a
355 |   cd ../server-b
356 |   pip install -r requirements.txt # Install dependencies for server-b
357 |   cd ../gateway-agent
358 |   pip install -r requirements.txt # Install dependencies for gateway-agent
359 |   cd ../gemini-server
360 |   pip install -r requirements.txt # Install dependencies for gemini-server
361 |   cd .. # Go back to root
362 |   ```
363 |   Make sure to create `requirements.txt` files in each directory, containing the libraries each uses. The root `requirements.txt` can include `mcp`.  A simple way to create these files is by activating the relevant virtual environment, then using `pip freeze > requirements.txt` in each project directory.
364 | 
365 | 2. **Define the Docker Network (Optional but recommended):** If you're not using host network mode, you need to create the docker network in the `docker-compose.yaml` file, so that the gateway agent can discover and communicate with Server A and Server B. Here's how:
366 | 
367 | ```yaml
368 | services:
369 |   # ... (your service definitions)
370 | 
371 | networks:
372 |   mcp-network: # Give your network a name
373 | 
374 | ```
375 | 
376 | Then add the network to each of the Docker container specifications:
377 | 
378 | ```yaml
379 | services:
380 |   gateway-agent:
381 |     # ... other settings
382 |     networks:
383 |       - mcp-network
384 | 
385 |   server-a:
386 |     # ... other settings
387 |     networks:
388 |       - mcp-network
389 | 
390 |   server-b:  # Added server-b
391 |     # ... similar to server-a
392 |     networks:
393 |       - mcp-network
394 | ```
395 | 
396 | 3.  **Run with Docker Compose:** In your project root, run:
397 | 
398 |     ```bash
399 |     docker compose up --build
400 |     ```
401 | 
402 |     This builds and starts all servers in the background with appropriate port mapping and shared volume.  Now you should have all the components (servers, shared volume) set up in Docker containers. This is generally a more reliable approach for consistent execution since you also provided Dockerfiles.
403 | 
404 | 4.  **Connect with MCP Inspector:** In a new terminal, run:
405 | 
406 |     ```bash
407 |     npx @modelcontextprotocol/inspector http://gateway-agent:8000/mcp/v1 # Note the protocol is now http
408 |     ```
409 | 
410 | This will connect the inspector to the gateway-agent and present a URL for you to access the inspector UI. From the UI, you should be able to call tools exposed by gateway agent, which will in turn route requests to the appropriate downstream servers.  The debug=True parameters we set earlier will help to pinpoint where issues are arising.  Make sure that servers A and B are accessible on port 5000 and 5001 on your local machine, respectively.  If you use Docker and don't expose these ports on host network (via the `ports` configuration in docker-compose), you'll need to attach to the network the containers create with the following command so that the DNS entries for the services are present: `docker network connect <networkname> <containername>`
411 | 


--------------------------------------------------------------------------------
/clients/claude-desktop/proxy.py:
--------------------------------------------------------------------------------
 1 | import socket
 2 | import sys
 3 | import threading
 4 | import argparse
 5 | import os
 6 | 
 7 | def log(message):
 8 |     with open(r'C:\Users\amanda\mcp\proxy.log', 'a') as f:
 9 |         f.write(f'{message}\n')
10 | 
11 | def create_parser():
12 |     parser = argparse.ArgumentParser(description='Proxy stdin/stdout over TCP')
13 |     parser.add_argument('host', help='Remote host to connect to')
14 |     parser.add_argument('port', type=int, help='Remote port to connect to')
15 |     return parser
16 | 
17 | def forward_stdin(sock):
18 |     """Forward stdin to socket"""
19 |     try:
20 |         while True:
21 |             data = sys.stdin.buffer.read1(4096)
22 |             if not data:
23 |                 break
24 |             sock.sendall(data)
25 |     except (socket.error, IOError) as e:
26 |         log(f"Error forwarding stdin: {e}")
27 |     finally:
28 |         try:
29 |             sock.shutdown(socket.SHUT_WR)
30 |         except socket.error:
31 |             pass
32 | 
33 | def forward_socket(sock):
34 |     """Forward socket data to stdout"""
35 |     try:
36 |         while True:
37 |             data = sock.recv(4096)
38 |             log(f'Received data: {data}')
39 |             if not data:
40 |                 break
41 |             sys.stdout.buffer.write(data)
42 |             sys.stdout.buffer.flush()
43 |     except (socket.error, IOError) as e:
44 |         log(f"Error forwarding socket: {e}")
45 | 
46 | def main():
47 |     log(f'Running proxy.py with arguments: {sys.argv}')
48 |     parser = create_parser()
49 |     args = parser.parse_args()
50 | 
51 |     try:
52 |         # Create TCP socket
53 |         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
54 |         sock.connect((args.host, args.port))
55 |         log(f'Connected to {args.host}:{args.port}')
56 |         
57 |         # Set up threads for bidirectional forwarding
58 |         stdin_thread = threading.Thread(target=forward_stdin, args=(sock,))
59 |         socket_thread = threading.Thread(target=forward_socket, args=(sock,))
60 | 
61 |         # Start forwarding threads
62 |         stdin_thread.start()
63 |         socket_thread.start()
64 | 
65 |         # Wait for threads to complete
66 |         stdin_thread.join()
67 |         socket_thread.join()
68 | 
69 |     except socket.error as e:
70 |         log(f"Socket error: {e}")
71 |         sys.exit(1)
72 |     except KeyboardInterrupt:
73 |         log("\nExiting due to user interrupt")
74 |     finally:
75 |         try:
76 |             sock.close()
77 |         except NameError:
78 |             pass
79 | 
80 | if __name__ == "__main__":
81 |     main()
82 | 


--------------------------------------------------------------------------------
/clients/claude-desktop/readme.md:
--------------------------------------------------------------------------------
1 | {
2 |     "mcpServers": {
3 |         "my-server": {
4 |             "command": "python3",
5 |             "args": ["C:\\Users\\amanda\\mcp\\proxy.py", "box", "11015"]
6 |         }
7 |     }
8 | }
9 | 


--------------------------------------------------------------------------------
/docker-compose.yaml:
--------------------------------------------------------------------------------
 1 | services:
 2 | 
 3 |   personal-trainer:
 4 |     build: server-a
 5 |     ports:
 6 |       - "5000:5000"
 7 |     volumes:
 8 |       - ./shared:/shared
 9 |     network_mode: "host"
10 |     environment:
11 |       - "ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}"
12 | 
13 |   work-assistant:
14 |     build: server-b
15 |     ports:
16 |       - "5001:5001"
17 |     volumes:
18 |       - ./shared:/shared
19 |     network_mode: "host"
20 |     environment:
21 |       - "ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}"
22 | 
23 |   gateway-agent:
24 |     build: gateway-agent
25 |     command:
26 |       - /app/listen.sh
27 |     volumes:
28 |       - ./shared:/shared
29 |     network_mode: "host"
30 |     environment:
31 |       - "ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}"
32 | 
33 | 
34 | 
35 | 


--------------------------------------------------------------------------------
1 | Dockerfile
2 | 


--------------------------------------------------------------------------------
/example-service/.gitignore:
--------------------------------------------------------------------------------
 1 | # Python-generated files
 2 | __pycache__/
 3 | *.py[oc]
 4 | build/
 5 | dist/
 6 | wheels/
 7 | *.egg-info
 8 | 
 9 | # Virtual environments
10 | .venv
11 | 


--------------------------------------------------------------------------------
/example-service/Dockerfile:
--------------------------------------------------------------------------------
 1 | FROM ubuntu:22.04
 2 | 
 3 | # Feel free to add other dependencies or packages
 4 | # however, `socat` MUST be installed for the server to work
 5 | RUN apt-get update -y && apt-get install -y \
 6 |     python3 python3-dev socat curl wget
 7 | 
 8 | # Use uv instead of pip
 9 | RUN curl -LsSf https://astral.sh/uv/install.sh | sh
10 | ENV PATH="/home/claude/.local/bin:${PATH}"
11 | 
12 | WORKDIR /app
13 | ADD . /app
14 | 
15 | # You can add more uv packages here or in the pyproject.toml file
16 | RUN uv add mcp && uv sync
17 | 
18 | 
19 | 


--------------------------------------------------------------------------------
/example-service/README.md:
--------------------------------------------------------------------------------
1 | This is an MCP starter kit for creating new MCP projects easily
2 | 


--------------------------------------------------------------------------------
/example-service/listen.sh:
--------------------------------------------------------------------------------
1 | #!/bin/bash
2 | 
3 | MYDIR=$(dirname $0)
4 | 
5 | socat TCP-LISTEN:11020,fork,reuseaddr,bind=192.168.13.37 EXEC:$MYDIR/run.sh
6 | 


--------------------------------------------------------------------------------
/example-service/pyproject.toml:
--------------------------------------------------------------------------------
1 | [project]
2 | name = "my-mcp-server"
3 | version = "0.1.0"
4 | description = "Add your description here"
5 | readme = "README.md"
6 | requires-python = ">=3.12"
7 | dependencies = ["mcp"]
8 | 


--------------------------------------------------------------------------------
/example-service/run.sh:
--------------------------------------------------------------------------------
1 | #!/bin/bash
2 | 
3 | uv run service.py
4 | 


--------------------------------------------------------------------------------
/example-service/service.py:
--------------------------------------------------------------------------------
 1 | #!/usr/bin/env python3
 2 | 
 3 | import asyncio
 4 | import subprocess
 5 | from typing import Dict, List
 6 | 
 7 | from mcp.server import Server, NotificationOptions
 8 | from mcp.server.models import InitializationOptions
 9 | import mcp.server.stdio
10 | import mcp.types as types
11 | 
12 | 
13 | 


--------------------------------------------------------------------------------
1 | Dockerfile
2 | 


--------------------------------------------------------------------------------
/gateway-agent/.gitignore:
--------------------------------------------------------------------------------
 1 | # Python-generated files
 2 | __pycache__/
 3 | *.py[oc]
 4 | build/
 5 | dist/
 6 | wheels/
 7 | *.egg-info
 8 | 
 9 | # Virtual environments
10 | .venv
11 | 


--------------------------------------------------------------------------------
/gateway-agent/Dockerfile:
--------------------------------------------------------------------------------
 1 | FROM ubuntu:22.04
 2 | 
 3 | # Feel free to add other dependencies or packages
 4 | # however, `socat` MUST be installed for the server to work
 5 | RUN apt-get update -y && apt-get install -y \
 6 |     python3 python3-dev socat curl wget
 7 | 
 8 | # Use uv instead of pip
 9 | RUN curl -LsSf https://astral.sh/uv/install.sh | sh
10 | ENV PATH="/root/.local/bin:${PATH}"
11 | 
12 | WORKDIR /app
13 | ADD . /app
14 | 
15 | # You can add more uv packages here or in the pyproject.toml file
16 | RUN uv add mcp && uv sync
17 | 
18 | 
19 | 


--------------------------------------------------------------------------------
/gateway-agent/README.md:
--------------------------------------------------------------------------------
1 | This is an MCP starter kit for creating new MCP projects easily
2 | 


--------------------------------------------------------------------------------
/gateway-agent/listen.sh:
--------------------------------------------------------------------------------
1 | #!/bin/bash
2 | 
3 | MYDIR=$(dirname $0)
4 | 
5 | socat TCP-LISTEN:11020,fork,reuseaddr,bind=192.168.13.37 EXEC:$MYDIR/run.sh
6 | 


--------------------------------------------------------------------------------
/gateway-agent/pyproject.toml:
--------------------------------------------------------------------------------
1 | [project]
2 | name = "my-mcp-server"
3 | version = "0.1.0"
4 | description = "Add your description here"
5 | readme = "README.md"
6 | requires-python = ">=3.12"
7 | dependencies = ["mcp", "requests"]
8 | 


--------------------------------------------------------------------------------
/gateway-agent/run.sh:
--------------------------------------------------------------------------------
1 | #!/bin/bash
2 | 
3 | uv run service.py
4 | 


--------------------------------------------------------------------------------
/gateway-agent/service.py:
--------------------------------------------------------------------------------
  1 | import asyncio
  2 | import json
  3 | import logging
  4 | import os
  5 | import sys
  6 | from typing import Any, Dict, Sequence
  7 | 
  8 | import requests  # Import requests
  9 | from typing import Any, Dict, Sequence, List
 10 | from mcp.server import NotificationOptions, Server
 11 | from mcp.server.models import InitializationOptions
 12 | from mcp.server.stdio import stdio_server
 13 | from mcp.types import (
 14 |     CallToolRequestParams,
 15 |     CallToolRequest,
 16 |     CallToolResult,
 17 |     ClientCapabilities,
 18 |     EmbeddedResource,
 19 |     ImageContent,
 20 |     ListToolsRequest,
 21 |     ListToolsResult,
 22 |     Prompt,
 23 |     PromptArgument,
 24 |     PromptMessage,
 25 |     RootsCapability,
 26 |     ServerCapabilities,
 27 |     TextContent,
 28 |     Tool,
 29 | )
 30 | from pydantic import BaseModel, Field, AnyUrl
 31 | from mcp.shared.exceptions import McpError
 32 | 
 33 | 
 34 | # Configuration for Server A and Server B (using URLs for HTTP communication)
 35 | SERVER_A = {
 36 |     "url": "http://localhost:5010/mcp/v1", # URL of Server A
 37 |     "tool_name": "ask_personal_trainer", # Tool name on Server A
 38 | }
 39 | SERVER_B = {
 40 |     "url": "http://localhost:5001/mcp/v1",  # Replace with actual URL for Server B
 41 |     "tool_name": "handle_professional_task",  # Replace with actual tool name on Server B
 42 | }
 43 | 
 44 | # Set up logging
 45 | logging.basicConfig(level=logging.INFO, stream=sys.stderr)
 46 | logger = logging.getLogger(__name__)
 47 | 
 48 | # Initialize the MCP server
 49 | server = Server("gateway-agent")
 50 | 
 51 | 
 52 | @server.list_tools()
 53 | async def list_tools() -> List[Tool]:
 54 |     """Lists available tools for the gateway agent."""
 55 |     return [
 56 |         Tool(
 57 |             name="route_task",
 58 |             description="Routes a user's productivity-related query or task to the appropriate agent.",
 59 |             inputSchema={
 60 |                 "type": "object",
 61 |                 "properties": {
 62 |                     "user_input": {
 63 |                         "type": "string",
 64 |                         "description": "User's productivity-related query or task.",
 65 |                     },
 66 |                 },
 67 |                 "required": ["user_input"],
 68 |             },
 69 |         )
 70 |     ]
 71 | 
 72 | 
 73 | 
 74 | def ask_mcp_server(server_url: str, tool_call: str, data: str) -> str: # Add type hints
 75 |     """Sends an MCP tool call request to the specified server."""
 76 |     body = {
 77 |         "jsonrpc": "2.0",
 78 |         "id": 1,  # Using a static ID for simplicity in this example. In a real application, you should manage IDs.
 79 |         "method": "tools/call",
 80 |         "params": {
 81 |             "name": tool_call,
 82 |             "arguments": {"body": data}, # Correct tool call (no nested title, labels, etc.)
 83 |         },
 84 |     }
 85 |     try:
 86 |         print("Now sending request to", server_url, file=sys.stderr)
 87 |         response = requests.post(server_url, json=body)
 88 |         print(response, file=sys.stderr)
 89 |         print(response.text, file=sys.stderr)
 90 |         data = response.json()
 91 |         print('got data', data, file=sys.stderr)
 92 |         final = data.get("result",{}).get("content",[])[0].get('text')
 93 |         print('final',final,file=sys.stderr)
 94 |         return final
 95 | 
 96 |     except requests.exceptions.RequestException as e:
 97 |         raise McpError(INTERNAL_ERROR, f"Error communicating with server: {e}")
 98 |     except (KeyError, IndexError) as e:
 99 |          raise McpError(INTERNAL_ERROR, f"Unexpected response format: {e}")
100 | 
101 | @server.call_tool()
102 | async def call_tool(
103 |     name: str, arguments: dict
104 | ) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
105 |     """Routes the task to the appropriate server and tool."""
106 | 
107 |     if name != "route_task":
108 |         raise ValueError(f"Unknown tool: {name}")
109 | 
110 | 
111 |     user_input = arguments.get("user_input")
112 |     if not user_input:
113 |         raise ValueError("Missing 'user_input' argument.")
114 | 
115 | 
116 | 
117 |     # Routing logic (can be improved with NLP or more sophisticated methods)
118 |     if any(keyword in user_input.lower() for keyword in ["weight", "sleep", "exercise", "health"]):
119 |         target_server = SERVER_A
120 |     else:
121 |         target_server = SERVER_B  # Default server (you'll need to implement server B)
122 | 
123 | 
124 |     try:
125 |         # Use the ask_mcp_server function to make the tool call
126 |         result = ask_mcp_server(target_server["url"], target_server["tool_name"], user_input)
127 |         return [TextContent(type="text", text=result)]
128 | 
129 |     except McpError as e:
130 |         raise
131 |     except Exception as e:
132 |         logger.error(f"Error routing task to server: {e}")
133 |         raise McpError(f"Error routing task: {e}")
134 | 
135 | async def run_server() -> None:
136 |     """Runs the gateway agent server."""
137 |     try:
138 |         async with stdio_server() as (read_stream, write_stream):
139 |             await server.run(
140 |                 read_stream,
141 |                 write_stream,
142 |                 InitializationOptions(
143 |                     server_name="gateway_agent",
144 |                     server_version="0.1.0",
145 |                     capabilities=server.get_capabilities(
146 |                         notification_options=NotificationOptions(),
147 |                         experimental_capabilities={},
148 |                     ),
149 |                 ),
150 |             )
151 |     except Exception as e:
152 |         logger.error(f"Server error: {e}")
153 |         raise
154 | 
155 | def main() -> None:
156 |     """Main entry point for the gateway agent service."""
157 |     try:
158 |         asyncio.run(run_server())
159 |     except KeyboardInterrupt:
160 |         logger.info("Server shutdown requested")
161 |     except Exception as e:
162 |         logger.error(f"Fatal error: {e}")
163 |         sys.exit(1)
164 | 
165 | 
166 | if __name__ == "__main__":
167 |     main()
168 | 


--------------------------------------------------------------------------------
/hacking-files/.DS_Store:
--------------------------------------------------------------------------------
https://raw.githubusercontent.com/dazzaji/mcp-agent-router/5b73d15417af330e5fa03df7a062d2a8069f7ac2/hacking-files/.DS_Store


--------------------------------------------------------------------------------
/hacking-files/scratch-pad-for-gateway-agent.md:
--------------------------------------------------------------------------------
  1 | # Below is the assumptions, reasoning, and approach for initial gateway agent:
  2 | 
  3 | ## Prompt:
  4 | 
  5 | Hi!  We are at a hackathon to work with the Model Context Protocol (MCP) and are making a simple multi-agent system.  All MCP repo's and docs are attached as a file.  The project idea at high level is in readme in attached repo file "dazzaji_mcp-agent-router.md".  I am working on the agent that will decide which other agent to rout a task to.  I want help developing the service.py code for the gateway agent in our repo.  The agent, among other things, needs a great prompt to decide which other agent (A or B) to route the task to.  It will be for personal productivity.  A will be physical stuff (like weight, strength, sleep, etc) and B will be professional or work oriented productivity (focus, time management, etc, etc).  So we need our gateway agent to take the user input and decide where to route it and then to actually send the task to the right server A or B.  
  6 | 
  7 | ASK QUESTIONS if you need more info, but for now just a scaffold of the code for service.py woudl be great.
  8 | 
  9 | [attached full repos for all MCP python related and general info and also repo for our current state hack project]
 10 | 
 11 | ## Reponse (Gemini 1.5 Pro Experimental 1206)
 12 | 
 13 | ```python
 14 | import asyncio
 15 | import json
 16 | import logging
 17 | import os
 18 | import sys
 19 | from typing import Any, Dict, Sequence
 20 | 
 21 | from mcp.server import NotificationOptions, Server
 22 | from mcp.server.models import InitializationOptions
 23 | from mcp.server.stdio import stdio_server
 24 | from mcp.types import (
 25 |     CallToolRequestParams,
 26 |     CallToolRequest,
 27 |     CallToolResult,
 28 |     ClientCapabilities,
 29 |     EmbeddedResource,
 30 |     ImageContent,
 31 |     ListToolsRequest,
 32 |     ListToolsResult,
 33 |     Prompt,
 34 |     PromptArgument,
 35 |     PromptMessage,
 36 |     RootsCapability,
 37 |     ServerCapabilities,
 38 |     TextContent,
 39 |     Tool,
 40 | )
 41 | 
 42 | 
 43 | # Configuration for Server A and Server B
 44 | SERVER_A_CONFIG = {
 45 |     "command": "python",
 46 |     "args": ["-m", "physical_productivity_agent"],  # Replace with actual module name
 47 | }
 48 | SERVER_B_CONFIG = {
 49 |     "command": "python",
 50 |     "args": ["-m", "professional_productivity_agent"],  # Replace with actual module name
 51 | }
 52 | 
 53 | # Set up logging
 54 | logging.basicConfig(level=logging.INFO, stream=sys.stderr)
 55 | logger = logging.getLogger(__name__)
 56 | 
 57 | # Initialize the MCP server
 58 | server = Server("gateway-agent")
 59 | 
 60 | class RouteArgs(BaseModel):
 61 |     user_input: str = Field(..., description="User's productivity-related query or task.")
 62 | 
 63 | @server.list_prompts()
 64 | async def list_prompts() -> list[Prompt]:
 65 |     return [
 66 |         Prompt(
 67 |             name="route",
 68 |             description="Route a productivity task to the appropriate agent.",
 69 |             arguments=[
 70 |                 PromptArgument(
 71 |                     name="user_input",
 72 |                     description="The user's input or query related to productivity.",
 73 |                     required=True,
 74 |                 ),
 75 |             ],
 76 |         )
 77 |     ]
 78 | 
 79 | 
 80 | @server.get_prompt()
 81 | async def get_prompt(name: str, arguments: dict | None) -> types.GetPromptResult:
 82 |     if name != "route":
 83 |         raise ValueError(f"Unknown prompt: {name}")
 84 | 
 85 |     user_input = (arguments or {}).get("user_input")
 86 |     if not user_input:
 87 |         raise ValueError("Missing 'user_input' argument.")
 88 | 
 89 | 
 90 |     return types.GetPromptResult(
 91 |         description=f"Routing prompt for user input: {user_input}",
 92 |         messages=[
 93 |             types.PromptMessage(
 94 |                 role="user",
 95 |                 content=types.TextContent(
 96 |                     type="text",
 97 |                     text=f"""Decide whether the following user input relates to physical productivity (Server A) or professional/work productivity (Server B):
 98 |                     
 99 |                     User Input: "{user_input}"
100 |                     
101 |                     Respond with either "Server A" or "Server B".
102 |                     """,
103 |                 ),
104 |             )
105 |         ],
106 |     )
107 | 
108 | 
109 | 
110 | 
111 | @server.list_tools()
112 | async def list_tools() -> ListToolsResult:
113 |     return ListToolsResult(
114 |         tools=[
115 |             Tool(
116 |                 name="route_task",
117 |                 description="""Routes a user's productivity-related query or task to the appropriate agent (Server A or Server B).""",
118 |                 inputSchema=RouteArgs.model_json_schema(),
119 |             ),
120 |         ]
121 |     )
122 | 
123 | 
124 | async def _run_tool_on_server(server_config: Dict[str, Any], tool_name: str, arguments: Dict[str, Any]):
125 |     from mcp.client import ClientSession, stdio_client, StdioServerParameters
126 |     
127 |     server_params = StdioServerParameters(command=server_config["command"], args=server_config["args"])
128 |     async with stdio_client(server_params) as (read, write):
129 |         async with ClientSession(read, write) as session:
130 |             await session.initialize()
131 |             return await session.call_tool(tool_name, arguments)
132 |             
133 | 
134 | @server.call_tool()
135 | async def call_tool(
136 |     name: str, arguments: dict
137 | ) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
138 | 
139 |     if name != "route_task":
140 |         raise ValueError(f"Unknown tool: {name}")
141 | 
142 |     user_input = arguments.get("user_input")
143 |     if not user_input:
144 |         raise ValueError("Missing 'user_input' argument.")
145 | 
146 |     # Basic routing logic (replace with your actual routing criteria)
147 |     if any(keyword in user_input.lower() for keyword in ["weight", "sleep", "exercise", "health"]):
148 |         target_server = SERVER_A_CONFIG
149 |         tool_to_call = "handle_physical_task"  # Tool name on server A
150 |     elif any(keyword in user_input.lower() for keyword in ["work", "meeting", "deadline", "project"]):
151 |         target_server = SERVER_B_CONFIG
152 |         tool_to_call = "handle_professional_task"  # Tool name on server B
153 |     else:
154 |         # Default to server B if no specific keywords are found
155 |         target_server = SERVER_B_CONFIG
156 |         tool_to_call = "handle_professional_task"
157 | 
158 |     try:
159 |         result = await _run_tool_on_server(target_server, tool_to_call, {"user_input": user_input})
160 |         return result.content
161 |     except Exception as e:
162 |         logger.error(f"Error routing task to server: {e}")
163 |         raise McpError(f"Error routing task: {e}")
164 | 
165 | 
166 | async def run():
167 |     """Run the gateway agent server."""
168 |     async with stdio_server() as (read_stream, write_stream):
169 |         await server.run(
170 |             read_stream,
171 |             write_stream,
172 |             InitializationOptions(
173 |                 server_name="gateway_agent",
174 |                 server_version="0.1.0",  # Replace with your version
175 |                 capabilities=server.get_capabilities(
176 |                     notification_options=NotificationOptions(),
177 |                     experimental_capabilities={},
178 |                 ),
179 |             ),
180 |         )
181 | 
182 | 
183 | def main():
184 |     anyio.run(run)
185 | 
186 | 
187 | if __name__ == "__main__":
188 |     main()
189 | 
190 | ```
191 | 
192 | **Key improvements and explanations:**
193 | 
194 | * **Routing Prompt:** The prompt now explicitly asks the LLM to respond with either "Server A" or "Server B", making the routing decision clear and unambiguous.  This prompt is exposed as an MCP prompt so it can be easily used and customized by clients.
195 | * **Routing Logic:**  The `route_task` tool implements a basic routing logic based on keywords. You should refine this logic to match your specific routing criteria.  The code includes a fallback to Server B if no specific keywords are found in the user input.
196 | * **Tool Execution on Target Server:** The `_run_tool_on_server` function handles the execution of tools on the selected target server (A or B). This function abstracts away the details of connecting to and interacting with the other servers, allowing the `route_task` tool to focus solely on routing logic.
197 | * **Error Handling:** The `call_tool` function now includes error handling for cases where the routing fails or the target server is unavailable.
198 | * **Logging:** The code uses the logging module to provide visibility into the server's operations. Log messages are written to the standard error stream, which can be captured and displayed by the client application.
199 | * **Type Hinting:** Includes comprehensive type hints for better readability and maintainability.
200 | 
201 | **Testing with MCP Inspector**
202 | 
203 | 1.  Start the `gateway-agent` server in one terminal.
204 | 2.  In another terminal, run:
205 | 
206 | ```bash
207 | npx @modelcontextprotocol/inspector python -m gateway_agent
208 | ```
209 | 
210 | 1.  Use the MCP Inspector UI in your browser to send test requests to the server.  You'll be able to interact with the `route_task` tool and observe its behavior.  The logging messages from the `gateway-agent` server will be displayed in the inspector's console.
211 | 
212 | 
213 | This scaffold should provide a good starting point for developing your gateway agent. You will likely need to customize the routing logic, implement the actual physical and professional productivity agents, and add more sophisticated error handling.  Remember to consult the full MCP documentation for guidance on more advanced features.
214 | 
215 | 
216 | -----
217 | 
218 | # PROMPT
219 | 
220 | Good start!  Ok, now we have an initial code and strucrture for Server A (the one that will be physical productivity and help).  I think we need to incorporate this into the code for the gateway agent so that it knows what info to send, right?
221 | 
222 | Attached is updated repo for our project.  Can you help with this?
223 | 
224 | -----
225 | 
226 | # OUTPUT
227 | 
228 | You're right, the gateway agent needs to know how to interact with Server A (and Server B, which you'll presumably create similarly). It also needs to determine *when* to use Server A vs. Server B. This involves a couple of things:
229 | 
230 | 1.  **Routing Logic:** The gateway agent needs a way to decide, based on user input, whether a task should go to Server A or Server B. This might involve keyword analysis, regular expressions, or even calling an LLM to classify the intent.
231 | 2.  **Inter-server Communication:** The gateway agent needs a mechanism to communicate with the other servers. Since all servers are MCP servers, the gateway agent will act as an MCP *client* when talking to Server A or B. It will need to send requests and receive responses according to the MCP specification.
232 | 
233 | Here's an updated `service.py` for the gateway agent that incorporates these changes, along with some other improvements. Note that I'm making some assumptions about the tools exposed by Server A and B; you'll need to adjust these if they differ in your actual implementation.  This code requires the `httpx` library, which you can install with `uv add httpx`:
234 | 
235 | ```python
236 | import asyncio
237 | import json
238 | import logging
239 | import os
240 | import sys
241 | from typing import Any, Dict, Sequence
242 | 
243 | from mcp.server import NotificationOptions, Server
244 | from mcp.server.models import InitializationOptions
245 | from mcp.server.stdio import stdio_server
246 | from mcp.types import (
247 |     CallToolRequestParams,
248 |     CallToolRequest,
249 |     CallToolResult,
250 |     ClientCapabilities,
251 |     EmbeddedResource,
252 |     ImageContent,
253 |     ListToolsRequest,
254 |     ListToolsResult,
255 |     Prompt,
256 |     PromptArgument,
257 |     PromptMessage,
258 |     RootsCapability,
259 |     ServerCapabilities,
260 |     TextContent,
261 |     Tool,
262 | )
263 | from pydantic import BaseModel, Field, AnyUrl
264 | from mcp.shared.exceptions import McpError
265 | 
266 | # Configuration for Server A and Server B
267 | SERVER_A = {
268 |     "url": "http://localhost:5000/mcp/v1",  # URL for Server A's MCP endpoint
269 |     "tool_name": "ask_personal_trainer",      # Tool name on Server A
270 | }
271 | SERVER_B = {
272 |     "url": "http://localhost:5001/mcp/v1", # URL for Server B's MCP endpoint (replace with actual if different)
273 |     "tool_name": "handle_professional_task",  # Tool name on Server B (replace with actual)
274 | }
275 | 
276 | # Set up logging
277 | logging.basicConfig(level=logging.INFO, stream=sys.stderr)
278 | logger = logging.getLogger(__name__)
279 | 
280 | # Initialize the MCP server
281 | server = Server("gateway-agent")
282 | 
283 | 
284 | @server.list_tools()
285 | async def list_tools() -> ListToolsResult:
286 |     return ListToolsResult(
287 |         tools=[
288 |             Tool(
289 |                 name="route_task",
290 |                 description="""Routes a user's productivity-related query or task to the appropriate agent (Server A or Server B).""",
291 |                 inputSchema={
292 |                     "type": "object",
293 |                     "properties": {
294 |                         "user_input": {
295 |                             "type": "string",
296 |                             "description": "User's productivity-related query or task.",
297 |                         },
298 |                     },
299 |                     "required": ["user_input"],
300 |                 },
301 |             ),
302 |         ]
303 |     )
304 | 
305 | 
306 | async def _run_tool_on_server(server_config: Dict[str, Any], user_input: str) -> CallToolResult:
307 |     """Runs the specified tool on the given server with the provided user input."""
308 | 
309 |     from mcp.client import ClientSession, sse_client
310 |     
311 |     async with sse_client(server_config["url"]) as (read, write):
312 |         async with ClientSession(read, write) as session:
313 |             await session.initialize()
314 | 
315 |             try:
316 |                 result = await session.call_tool(
317 |                     server_config["tool_name"], {"body": user_input}
318 |                 )
319 |                 return result
320 |             except McpError as e:
321 |                 return e.error
322 |             except Exception as e:
323 |                 logger.error(f"Error running tool on server: {e}")
324 |                 raise McpError(f"Error running tool on server: {e}")
325 | 
326 | 
327 | 
328 | @server.call_tool()
329 | async def call_tool(
330 |     name: str, arguments: dict
331 | ) -> Sequence[TextContent | ImageContent | EmbeddedResource]:
332 |     """Routes the task to the appropriate server and tool."""
333 | 
334 |     if name != "route_task":
335 |         raise ValueError(f"Unknown tool: {name}")
336 | 
337 | 
338 |     user_input = arguments.get("user_input")
339 |     if not user_input:
340 |         raise ValueError("Missing 'user_input' argument.")
341 | 
342 |     # Routing logic based on keywords (customize as needed)
343 |     if any(keyword in user_input.lower() for keyword in ["weight", "sleep", "exercise", "health"]):
344 |         target_server = SERVER_A
345 |     elif any(keyword in user_input.lower() for keyword in ["work", "meeting", "deadline", "project"]):
346 |         target_server = SERVER_B
347 |     else:
348 |         target_server = SERVER_B  # Default server
349 | 
350 |     result = await _run_tool_on_server(target_server, user_input)
351 |     
352 |     return [TextContent(type="text", text = result.content[0].text)]
353 | 
354 | async def run():
355 |     """Run the gateway agent server."""
356 |     async with stdio_server() as (read_stream, write_stream):
357 |         await server.run(
358 |             read_stream,
359 |             write_stream,
360 |             InitializationOptions(
361 |                 server_name="gateway_agent",
362 |                 server_version="0.1.0",  # Replace with your version
363 |                 capabilities=server.get_capabilities(
364 |                     notification_options=NotificationOptions(),
365 |                     experimental_capabilities={},
366 |                 ),
367 |             ),
368 |         )
369 | 
370 | 
371 | def main():
372 |     anyio.run(run)
373 | 
374 | 
375 | if __name__ == "__main__":
376 |     main()
377 | ```
378 | 
379 | 
380 | 
381 | **Changes and Explanations:**
382 | 
383 | *   **Server Configuration:** The `SERVER_A` and `SERVER_B` configuration now includes the full URL of the respective servers' MCP endpoints and the name of the expected tool to call, using HTTP/SSE for communication.
384 | *   **`_run_tool_on_server()` function:** This function now handles all of the complexity of connecting to the other servers as a client:
385 |     *   It uses the `httpx` library to make requests to other MCP servers over HTTP.
386 |     *   Creates a proper MCP ClientSession to handle communication.
387 |     *   Sends a `tools/call` request to the downstream server.
388 |     *   Returns the `CallToolResult` object received.
389 | 
390 | *   **`call_tool()` Function (Gateway Agent):**
391 |     *   Calls `_run_tool_on_server` to interact with the chosen server.
392 |     *   Handles potential errors from downstream server.
393 | 
394 | 
395 | 
396 | This revised code provides a more robust and functional gateway agent that can route tasks and interact with other MCP servers.  Remember to adjust the URLs and tool names to match your specific server implementations for A and B.  Also, create a `server_b` directory analogous to `server_a`, but with the appropriate tools for professional productivity.  You can still use the testing instructions from the previous response to interact with the agent and downstream servers.


--------------------------------------------------------------------------------
/hello.py:
--------------------------------------------------------------------------------
1 | def main():
2 |     print("Hello from mcp-agent-router!")
3 | 
4 | 
5 | if __name__ == "__main__":
6 |     main()
7 | 


--------------------------------------------------------------------------------
https://raw.githubusercontent.com/dazzaji/mcp-agent-router/5b73d15417af330e5fa03df7a062d2a8069f7ac2/image.png


--------------------------------------------------------------------------------
/pyproject.toml:
--------------------------------------------------------------------------------
 1 | [project]
 2 | name = "mcp-agent-router"
 3 | version = "0.1.0"
 4 | description = "Add your description here"
 5 | readme = "README.md"
 6 | requires-python = ">=3.9"
 7 | dependencies = [
 8 |     "requests>=2.32.3",
 9 | ]
10 | 


--------------------------------------------------------------------------------
/server-a/Dockerfile:
--------------------------------------------------------------------------------
 1 | FROM ubuntu:22.04
 2 | 
 3 | # Feel free to add other dependencies or packages
 4 | # however, `socat` MUST be installed for the server to work
 5 | RUN apt-get update -y && apt-get install -y \
 6 |     python3 python3-dev socat curl wget python3-pip
 7 | 
 8 | RUN pip install flask anthropic requests python-dotenv
 9 | 
10 | WORKDIR /app
11 | ADD . /app
12 | 
13 | CMD ["python3", "/app/server.py"]
14 | 
15 | 


--------------------------------------------------------------------------------
/server-a/server.py:
--------------------------------------------------------------------------------
  1 | from flask import Flask, jsonify, request
  2 | import sys
  3 | 
  4 | import json
  5 | 
  6 | app = Flask(__name__)
  7 | 
  8 | import os
  9 | from anthropic import Anthropic
 10 | from dotenv import load_dotenv
 11 | import json
 12 | 
 13 | # Load environment variables from .env file
 14 | load_dotenv()
 15 | 
 16 | class HealthTrainer:
 17 |     def __init__(self):
 18 |         # Initialize Anthropic client
 19 |         self.anthropic = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
 20 |         
 21 |         # Initialize user profile
 22 |         self.user_profile = {
 23 |             "name": "",
 24 |             "age": 0,
 25 |             "weight": 0,
 26 |             "height": 0,
 27 |             "fitness_goals": [],
 28 |             "dietary_restrictions": [],
 29 |             "activity_level": ""
 30 |         }
 31 |         
 32 |         # System prompt to define Claude's role
 33 |         self.system_prompt = """You are a knowledgeable and supportive personal health trainer. 
 34 |         Your role is to provide personalized fitness advice, workout plans, and nutritional guidance. 
 35 |         Always prioritize safety and encourage sustainable healthy habits. 
 36 |         If a user mentions any concerning health symptoms, advise them to consult with a healthcare professional."""
 37 |     
 38 |     def setup_profile(self):
 39 |         """Initial setup to gather user information"""
 40 |         print("Welcome to your AI Health Trainer! Let's set up your profile.")
 41 |         
 42 |         self.user_profile["name"] = input("What's your name? ")
 43 |         self.user_profile["age"] = int(input("What's your age? "))
 44 |         self.user_profile["weight"] = float(input("What's your weight in kg? "))
 45 |         self.user_profile["height"] = float(input("What's your height in cm? "))
 46 |         
 47 |         print("\nWhat are your fitness goals? (Enter one per line, press Enter twice when done)")
 48 |         while True:
 49 |             goal = input()
 50 |             if goal == "":
 51 |                 break
 52 |             self.user_profile["fitness_goals"].append(goal)
 53 |         
 54 |         print("\nDo you have any dietary restrictions? (Enter one per line, press Enter twice when done)")
 55 |         while True:
 56 |             restriction = input()
 57 |             if restriction == "":
 58 |                 break
 59 |             self.user_profile["dietary_restrictions"].append(restriction)
 60 |         
 61 |         print("\nWhat's your activity level?")
 62 |         print("1. Sedentary (little or no exercise)")
 63 |         print("2. Lightly active (light exercise/sports 1-3 days/week)")
 64 |         print("3. Moderately active (moderate exercise/sports 3-5 days/week)")
 65 |         print("4. Very active (hard exercise/sports 6-7 days/week)")
 66 |         print("5. Super active (very hard exercise/sports & physical job or training twice per day)")
 67 |         
 68 |         activity_levels = {
 69 |             "1": "Sedentary",
 70 |             "2": "Lightly active",
 71 |             "3": "Moderately active",
 72 |             "4": "Very active",
 73 |             "5": "Super active"
 74 |         }
 75 |         
 76 |         choice = input("Choose (1-5): ")
 77 |         self.user_profile["activity_level"] = activity_levels.get(choice, "Moderately active")
 78 |         
 79 |         # Save profile to file
 80 |         with open("user_profile.json", "w") as f:
 81 |             json.dump(self.user_profile, f, indent=4)
 82 |         
 83 |         print("\nProfile setup complete!")
 84 | 
 85 |     def load_profile(self):
 86 |         """Load existing user profile"""
 87 |         try:
 88 |             with open("user_profile.json", "r") as f:
 89 |                 self.user_profile = json.load(f)
 90 |             return True
 91 |         except FileNotFoundError:
 92 |             return False
 93 | 
 94 |     def get_ai_response(self, user_message):
 95 |         """Get response from Claude"""
 96 |         try:
 97 |             # Prepare the context with user profile
 98 |             context = f"""User Profile:
 99 |             Name: {self.user_profile['name']}
100 |             Age: {self.user_profile['age']}
101 |             Weight: {self.user_profile['weight']} kg
102 |             Height: {self.user_profile['height']} cm
103 |             Fitness Goals: {', '.join(self.user_profile['fitness_goals'])}
104 |             Dietary Restrictions: {', '.join(self.user_profile['dietary_restrictions'])}
105 |             Activity Level: {self.user_profile['activity_level']}
106 |             
107 |             User Question/Message: {user_message}"""
108 | 
109 |             # Get response from Claude
110 |             message = self.anthropic.messages.create(
111 |                 model="claude-3-5-sonnet-20241022",
112 |                 max_tokens=1000,
113 |                 system=self.system_prompt,
114 |                 messages=[
115 |                     {
116 |                         "role": "user",
117 |                         "content": context
118 |                     }
119 |                 ]
120 |             )
121 |             
122 |             return message.content[0].text
123 |         
124 |         except Exception as e:
125 |             return f"Error getting response: {str(e)}"
126 | 
127 |     def start_session(self, user_input):
128 |         response = self.get_ai_response(user_input)
129 |         print("\nAI Trainer:", response, file=sys.stderr)
130 |         return response
131 | 
132 | 
133 | '''
134 | {
135 |   "jsonrpc": "2.0",
136 |   "id": 1,
137 |   "method": "tools/call",
138 |   "params": {
139 |     "name": "ask_personal_trainer",
140 |     "arguments": {
141 |       "title": "User Has Question",
142 |       "body": "What should I do for my weight?",
143 |       "labels": ["health"]
144 |     }
145 |   }
146 | }
147 | '''
148 | 
149 | def log_json(data):
150 |     with open('/shared/personal-trainer.log', 'a') as f:
151 |         f.write(json.dumps(data, indent=2)+'\n')
152 |     print(json.dumps(data, indent=2), file=sys.stderr)
153 | 
154 | def log_text(txt):
155 |     with open('/shared/personal-trainer.log', 'a') as f:
156 |         f.write(txt + '\n')
157 |     print(txt, file=sys.stderr)
158 | 
159 | def load_personal_trainer():
160 |     trainer = HealthTrainer()
161 |     trainer.user_profile = {
162 |         "name": "Claude Ant",
163 |         "age": 30,
164 |         "weight": 70,
165 |         "height": 175,
166 |         "fitness_goals": ["Lose weight", "Build muscle"],
167 |         "dietary_restrictions": ["Gluten-free", "Dairy-free"],
168 |         "activity_level": "Moderately active"
169 |     }
170 |     return trainer
171 | 
172 | 
173 | def run_personal_trainer(data):
174 |     body = data.get('params',{}).get('arguments',{}).get('body',{}).strip()
175 |     assert(body)
176 |     trainer = load_personal_trainer()
177 |     res = trainer.start_session(body)
178 |     return res
179 | 
180 | @app.route('/mcp/v1', methods=['POST'])
181 | def health():
182 |     data = request.get_json()
183 |     log_text('\n\n======== INCOMING MCP RESPONSE ========\n\n')
184 |     log_json(data)
185 | 
186 |     method_name = data.get('params',{}).get('name')
187 |     if method_name == 'ask_personal_trainer':
188 |         res = run_personal_trainer(data)
189 |     resp = {
190 |           "jsonrpc": "2.0",
191 |           "id": 1,
192 |           "result": {
193 |             "content": [
194 |               {
195 |                 "type": "text",
196 |                 "text": f"Personal Trainer Says: {res}"
197 |               }
198 |             ]
199 |           }
200 |         }
201 |     log_text('\n\n======= RESPONDING WITH MCP RESPONSE =======')
202 |     log_json(resp)
203 |     return jsonify(resp)
204 | 
205 | 
206 | if __name__ == '__main__':
207 |     app.run(port=5010, host='0.0.0.0')
208 | 
209 | 
210 | 
211 | 


--------------------------------------------------------------------------------
/server-a/talk.py:
--------------------------------------------------------------------------------
 1 | import requests
 2 | 
 3 | '''
 4 | {
 5 |   "jsonrpc": "2.0",
 6 |   "id": 1,
 7 |   "result": {
 8 |     "content": [
 9 |       {
10 |         "type": "text",
11 |         "text": "Successfully created issue #123"
12 |       }
13 |     ]
14 |   }
15 | }
16 | '''
17 | 
18 | def ask_mcp_server(server_url, tool_call, data):
19 |     # Create the MCP protocol blob to request a given toolcall
20 |     body = {
21 |       "jsonrpc": "2.0",
22 |       "id": 1,
23 |       "method": "tools/call",
24 |       "params": {
25 |         "name": tool_call,
26 |         "arguments": {
27 |           "title": "User Has Question",
28 |           "body": data,
29 |           "labels": ["health"]
30 |         }
31 |       }
32 |     }
33 |     # Makes the http request
34 |     res = requests.post(f'{server_url}', json=body) 
35 |     print(res.text)
36 |     data = res.json()
37 | 
38 |     # Extract the data from the response
39 |     return data.get('result',{}).get('content',[])[0].get('text')
40 | 
41 | 
42 | 
43 | if __name__ == '__main__':
44 |     ask_mcp_server("http://localhost:5000", "ask_personal_trainer", "What should I do for my weight?")
45 | 


--------------------------------------------------------------------------------
/server-b/Dockerfile:
--------------------------------------------------------------------------------
 1 | FROM ubuntu:22.04
 2 | 
 3 | # Feel free to add other dependencies or packages
 4 | # however, `socat` MUST be installed for the server to work
 5 | RUN apt-get update -y && apt-get install -y \
 6 |     python3 python3-dev socat curl wget python3-pip
 7 | 
 8 | RUN pip install flask anthropic requests python-dotenv
 9 | 
10 | WORKDIR /app
11 | ADD . /app
12 | 
13 | CMD ["python3", "/app/server.py"]
14 | 
15 | 


--------------------------------------------------------------------------------
/server-b/server.py:
--------------------------------------------------------------------------------
  1 | from flask import Flask, jsonify, request
  2 | 
  3 | import json
  4 | 
  5 | app = Flask(__name__)
  6 | 
  7 | import os
  8 | from anthropic import Anthropic
  9 | from dotenv import load_dotenv
 10 | import json
 11 | 
 12 | # Load environment variables from .env file
 13 | load_dotenv()
 14 | 
 15 | class WorkAssistant:
 16 |     def __init__(self):
 17 |         # Initialize Anthropic client
 18 |         self.anthropic = Anthropic(api_key=os.getenv('ANTHROPIC_API_KEY'))
 19 |         
 20 |         # Initialize user profile
 21 |         self.user_profile = {
 22 |             "name": "",
 23 |             "role": "",
 24 |             "department": "",
 25 |             "work_preferences": [],
 26 |             "skills": [],
 27 |             "communication_style": "",
 28 |             "time_zone": ""
 29 |         }
 30 |         
 31 |         # System prompt to define Claude's role
 32 |         self.system_prompt = """You are a knowledgeable and supportive personal work assistant. 
 33 |         Your role is to provide personalized productivity advice, task management guidance, and work organization strategies. 
 34 |         Always prioritize efficiency and encourage sustainable work habits. 
 35 |         Help maintain work-life balance and suggest ways to optimize workflows while avoiding burnout."""
 36 |     
 37 |     def setup_profile(self):
 38 |         """Initial setup to gather user information"""
 39 |         print("Welcome to your AI Work Assistant! Let's set up your profile.")
 40 |         
 41 |         self.user_profile["name"] = input("What's your name? ")
 42 |         self.user_profile["role"] = input("What's your job role? ")
 43 |         self.user_profile["department"] = input("Which department do you work in? ")
 44 |         
 45 |         print("\nWhat are your work preferences? (e.g., 'early meetings', 'async communication') (Enter one per line, press Enter twice when done)")
 46 |         while True:
 47 |             preference = input()
 48 |             if preference == "":
 49 |                 break
 50 |             self.user_profile["work_preferences"].append(preference)
 51 |         
 52 |         print("\nWhat are your key skills? (Enter one per line, press Enter twice when done)")
 53 |         while True:
 54 |             skill = input()
 55 |             if skill == "":
 56 |                 break
 57 |             self.user_profile["skills"].append(skill)
 58 |         
 59 |         print("\nWhat's your preferred communication style?")
 60 |         print("1. Direct and concise")
 61 |         print("2. Detailed and thorough")
 62 |         print("3. Collaborative and discussion-based")
 63 |         print("4. Visual and example-driven")
 64 |         print("5. Mixed/Flexible")
 65 |         
 66 |         communication_styles = {
 67 |             "1": "Direct and concise",
 68 |             "2": "Detailed and thorough",
 69 |             "3": "Collaborative and discussion-based",
 70 |             "4": "Visual and example-driven",
 71 |             "5": "Mixed/Flexible"
 72 |         }
 73 |         
 74 |         choice = input("Choose (1-5): ")
 75 |         self.user_profile["communication_style"] = communication_styles.get(choice, "Mixed/Flexible")
 76 |         
 77 |         self.user_profile["time_zone"] = input("What's your time zone? (e.g., EST, PST, UTC): ")
 78 |         
 79 |         # Save profile to file
 80 |         with open("user_profile.json", "w") as f:
 81 |             json.dump(self.user_profile, f, indent=4)
 82 |         
 83 |         print("\nProfile setup complete!")
 84 | 
 85 |     def load_profile(self):
 86 |         """Load existing user profile"""
 87 |         try:
 88 |             with open("user_profile.json", "r") as f:
 89 |                 self.user_profile = json.load(f)
 90 |             return True
 91 |         except FileNotFoundError:
 92 |             return False
 93 | 
 94 |     def get_ai_response(self, user_message):
 95 |         """Get response from Claude"""
 96 |         try:
 97 |             # Prepare the context with user profile
 98 |             context = f"""User Profile:
 99 |             Name: {self.user_profile['name']}
100 |             Role: {self.user_profile['role']}
101 |             Department: {self.user_profile['department']}
102 |             Work Preferences: {', '.join(self.user_profile['work_preferences'])}
103 |             Skills: {', '.join(self.user_profile['skills'])}
104 |             Communication Style: {self.user_profile['communication_style']}
105 |             Time Zone: {self.user_profile['time_zone']}
106 |             
107 |             User Question/Message: {user_message}"""
108 | 
109 |             # Get response from Claude
110 |             message = self.anthropic.messages.create(
111 |                 model="claude-3-5-sonnet-20241022",
112 |                 max_tokens=1000,
113 |                 system=self.system_prompt,
114 |                 messages=[
115 |                     {
116 |                         "role": "user",
117 |                         "content": context
118 |                     }
119 |                 ]
120 |             )
121 |             
122 |             return message.content[0].text
123 |         
124 |         except Exception as e:
125 |             return f"Error getting response: {str(e)}"
126 | 
127 |     def start_session(self, user_input):
128 |         response = self.get_ai_response(user_input)
129 |         print("\nAI Assistant:", response)
130 |         return response
131 | 
132 | 
133 | '''
134 | {
135 |   "jsonrpc": "2.0",
136 |   "id": 1,
137 |   "method": "tools/call",
138 |   "params": {
139 |     "name": "ask_work_assistant",
140 |     "arguments": {
141 |       "title": "User Has Question",
142 |       "body": "How can I better organize my tasks?",
143 |       "labels": ["productivity"]
144 |     }
145 |   }
146 | }
147 | '''
148 | 
149 | def log_json(data):
150 |     with open('/shared/work-assistant.log', 'a') as f:
151 |         f.write(json.dumps(data, indent=2)+'\n')
152 | 
153 | def log_text(txt):
154 |     with open('/shared/work-assistant.log', 'a') as f:
155 |         f.write(txt + '\n')
156 | 
157 | def load_work_assistant():
158 |     assistant = WorkAssistant()
159 |     assistant.user_profile = {
160 |         "name": "Claude Ant",
161 |         "role": "Software Engineer",
162 |         "department": "Engineering",
163 |         "work_preferences": ["async communication", "afternoon meetings"],
164 |         "skills": ["Python", "Project Management", "Technical Writing"],
165 |         "communication_style": "Direct and concise",
166 |         "time_zone": "PST"
167 |     }
168 |     return assistant
169 | 
170 | 
171 | def run_work_assistant(data):
172 |     body = data.get('params',{}).get('arguments',{}).get('body',{}).strip()
173 |     assert(body)
174 |     assistant = load_work_assistant()
175 |     res = assistant.start_session(body)
176 |     return res
177 | 
178 | @app.route('/mcp/v1', methods=['POST'])
179 | def work():
180 |     data = request.get_json()
181 |     log_text('\n\n======== INCOMING MCP RESPONSE ========\n\n')
182 |     log_json(data)
183 | 
184 |     method_name = data.get('params',{}).get('name')
185 |     res = run_work_assistant(data)
186 |     resp = {
187 |           "jsonrpc": "2.0",
188 |           "id": 1,
189 |           "result": {
190 |             "content": [
191 |               {
192 |                 "type": "text",
193 |                 "text": f"Work Assistant Says: {res}"
194 |               }
195 |             ]
196 |           }
197 |         }
198 |     log_text('\n\n======= RESPONDING WITH MCP RESPONSE =======')
199 |     log_json(resp)
200 |     return jsonify(resp)
201 | 
202 | 
203 | if __name__ == '__main__':
204 |     app.run(port=5001, host='0.0.0.0')
205 | 


--------------------------------------------------------------------------------
/server-b/talk.py:
--------------------------------------------------------------------------------
 1 | import requests
 2 | 
 3 | '''
 4 | {
 5 |   "jsonrpc": "2.0",
 6 |   "id": 1,
 7 |   "result": {
 8 |     "content": [
 9 |       {
10 |         "type": "text",
11 |         "text": "Successfully created issue #123"
12 |       }
13 |     ]
14 |   }
15 | }
16 | '''
17 | 
18 | def ask_mcp_server(server_url, tool_call, data):
19 |     # Create the MCP protocol blob to request a given toolcall
20 |     body = {
21 |       "jsonrpc": "2.0",
22 |       "id": 1,
23 |       "method": "tools/call",
24 |       "params": {
25 |         "name": tool_call,
26 |         "arguments": {
27 |           "title": "User Has Question",
28 |           "body": data,
29 |           "labels": ["health"]
30 |         }
31 |       }
32 |     }
33 |     # Makes the http request
34 |     res = requests.post(f'{server_url}', json=body) 
35 |     print(res.text)
36 |     data = res.json()
37 | 
38 |     # Extract the data from the response
39 |     return data.get('result',{}).get('content',[])[0].get('text')
40 | 
41 | 
42 | 
43 | if __name__ == '__main__':
44 |     ask_mcp_server("http://localhost:5000", "ask_personal_trainer", "What should I do for my weight?")
45 | 


--------------------------------------------------------------------------------
/user-info-for-server-a.md:
--------------------------------------------------------------------------------
  1 | # Health Context Profile
  2 | 
  3 | ## Personal Information
  4 | 
  5 | - **User ID**: JP_AI_2024
  6 | - **User Name**: John Doey
  7 | - **Date of Birth**: August 15, 1997
  8 | - **Gender**: Male
  9 | 
 10 | ## Physical Metrics
 11 | 
 12 | ### Base Measurements
 13 | 
 14 | - **Height**: 5'8" (last measured: Nov 30, 2024)
 15 | - **Weight**: 150 lbs (last measured: Dec 9, 2024)
 16 | - **BMI**: 22.7 (calculated: Dec 9, 2024)
 17 | 
 18 | ### Body Composition
 19 | 
 20 | - **Body Fat Percentage**: 23.5%
 21 | - **Muscle Mass**: 64.6 lbs
 22 | - **Bone Mass**: 7.1 lbs
 23 | - **Last Measured**: December 1, 2024
 24 | 
 25 | ## Vital Signs
 26 | 
 27 | ### Current Readings
 28 | 
 29 | - **Blood Pressure**: 118/75 mmHg
 30 | - **Heart Rate**: 68 bpm
 31 | - **Respiratory Rate**: 14 breaths/minute
 32 | - **Last Measured**: December 9, 2024
 33 | 
 34 | ## Health Goals
 35 | 
 36 | ### Weight Management
 37 | 
 38 | - **Target**: 150 lbs (maintenance)
 39 | - **Deadline**: June 30, 2025
 40 | - **Type**: Maintenance
 41 | 
 42 | ### Activity Targets
 43 | 
 44 | - **Daily Steps**: 8,000
 45 | - **Weekly Exercise**: 150 minutes
 46 | - **Weekly Workouts**: 3 sessions
 47 | 
 48 | ### Nutrition Plans
 49 | 
 50 | - **Daily Caloric Target**: 2,200 calories
 51 | - **Macronutrient Breakdown**:
 52 |   - Protein: 2.8 oz (80g)
 53 |   - Carbohydrates: 8.8 oz (250g)
 54 |   - Fats: 2.6 oz (73g)
 55 | 
 56 | ## Medical History
 57 | 
 58 | ### Current Conditions
 59 | 
 60 | 1. **Computer Vision Syndrome**
 61 |    - Diagnosed: September 15, 2023
 62 |    - Status: Active
 63 |    - Medications: None
 64 | 
 65 | 2. **Mild Anxiety**
 66 |    - Diagnosed: March 20, 2023
 67 |    - Status: Active
 68 |    - Treatment:
 69 |      - Type: Meditation App Subscription
 70 |      - Duration: 15 minutes
 71 |      - Frequency: Daily
 72 |      - Started: March 25, 2023
 73 |      - Ongoing
 74 | 
 75 | ### Allergies
 76 | 
 77 | - **Tree Pollen**
 78 |   - Severity: Mild
 79 |   - Symptoms:
 80 |     - Sneezing
 81 |     - Itchy eyes
 82 | 
 83 | ### Family History
 84 | 
 85 | - **Type 2 Diabetes**: Paternal grandfather
 86 | - **Hypertension**: Maternal grandmother
 87 | 
 88 | ## Preferences
 89 | 
 90 | ### Measurement System
 91 | 
 92 | - Imperial
 93 | 
 94 | ### Dietary Restrictions
 95 | 
 96 | - Vegetarian
 97 | - Low-caffeine
 98 | 
 99 | ### Exercise Preferences
100 | 
101 | 1. Yoga
102 | 2. Running
103 | 3. Home workouts
104 | 
105 | ### Notification Settings
106 | 
107 | - Reminders: Enabled
108 | - Progress Updates: Enabled
109 | - Health Tips: Enabled
110 | 
111 | ---
112 | 
113 | *Last Updated: December 10, 2024*
114 | 
115 | Note: Some medical measurements (blood pressure, etc.) are kept in their standard units as they are universally reported this way regardless of measurement system preference.
116 | 


--------------------------------------------------------------------------------
/user-info-for-server-b.md:
--------------------------------------------------------------------------------
  1 | # Professional Development Profile
  2 | 
  3 | ## Personal Information
  4 | 
  5 | - **Name**: John Doey
  6 | - **User ID**: JP_AI_2024
  7 | - **Current Role**: Machine Learning Engineer II
  8 | - **Industry**: Artificial Intelligence
  9 | - **Years of Experience**: 2
 10 | - **Preferred Work Style**: Hybrid
 11 | 
 12 | ## Career Metrics
 13 | 
 14 | ### Current Position
 15 | 
 16 | - **Title**: Machine Learning Engineer II
 17 | - **Band**: IC2
 18 | - **Start Date**: January 15, 2024
 19 | 
 20 | ### Technical Skills
 21 | 
 22 | 1. **PyTorch**
 23 |    - Proficiency: Advanced
 24 |    - Last Used: December 9, 2024
 25 | 
 26 | 2. **LLM Fine-tuning**
 27 |    - Proficiency: Intermediate
 28 |    - Last Used: December 9, 2024
 29 | 
 30 | 3. **MLOps**
 31 |    - Proficiency: Intermediate
 32 |    - Last Used: December 8, 2024
 33 | 
 34 | ### Soft Skills
 35 | 
 36 | 1. **Technical Communication**
 37 |    - Self Assessment: 8/10
 38 |    - Last Assessed: November 30, 2024
 39 | 
 40 | 2. **Project Management**
 41 |    - Self Assessment: 7/10
 42 |    - Last Assessed: November 30, 2024
 43 | 
 44 | ## Time Management
 45 | 
 46 | ### Work Schedule
 47 | 
 48 | - **Preferred Hours**: 9:30 AM - 6:30 PM (PST)
 49 | - **Focus Time Blocks**:
 50 |   - Morning: 120-minute block
 51 | 
 52 | ### Meeting Preferences
 53 | 
 54 | - **Maximum Daily Meetings**: 4
 55 | - **Preferred Duration**: 30 minutes
 56 | - **Buffer Time**: 15 minutes
 57 | 
 58 | ## Professional Goals
 59 | 
 60 | ### Short-term Objectives
 61 | 
 62 | 1. **LLM Evaluation Framework Project**
 63 |    - Role: Project Lead
 64 |    - Target Date: March 30, 2025
 65 |    - Status: In Progress
 66 |    - Type: Project
 67 | 
 68 | 2. **MLOps Certification**
 69 |    - Target Date: February 28, 2025
 70 |    - Status: In Progress
 71 |    - Type: Certification
 72 | 
 73 | ### Long-term Objectives
 74 | 
 75 | - **Primary Goal**: Senior ML Engineer Role
 76 |   - Target Year: 2026
 77 |   - Key Milestones:
 78 |     1. Lead 2 major technical initiatives (Due: December 31, 2025)
 79 |     2. Develop team mentorship experience
 80 |     3. Establish technical thought leadership
 81 | 
 82 | ## Development Activities
 83 | 
 84 | ### Current Projects
 85 | 
 86 | 1. **LLM Evaluation Framework**
 87 |    - Role: Technical Lead
 88 |    - Skills: ML Architecture, Team Leadership
 89 |    - Visibility: Company-wide
 90 | 
 91 | 2. **Model Optimization Initiative**
 92 |    - Role: Individual Contributor
 93 |    - Skills: Performance Tuning, MLOps
 94 |    - Visibility: Department
 95 | 
 96 | ### Training Programs
 97 | 
 98 | 1. **MLOps Certification Program**
 99 |    - Provider: Major Cloud Provider
100 |    - Status: In Progress
101 |    - Expected Completion: Q1 2025
102 | 
103 | 2. **Technical Leadership Workshop**
104 |    - Provider: Internal L&D
105 |    - Status: Planned
106 |    - Start Date: January 2025
107 | 
108 | ## Learning & Growth
109 | 
110 | ### Areas of Focus
111 | 
112 | 1. **Technical**
113 |    - Large Language Models
114 |    - Distributed Systems
115 |    - ML Infrastructure
116 | 
117 | 2. **Leadership**
118 |    - Team Management
119 |    - Technical Project Planning
120 |    - Stakeholder Communication
121 | 
122 | ### Resources
123 | 
124 | - Internal ML Engineering Wiki
125 | - Technical Conference Presentations
126 | - Industry Research Papers
127 | - Team Knowledge Sharing Sessions
128 | 
129 | ## Professional Network Development
130 | 
131 | ### Current Activities
132 | 
133 | - Regular 1:1s with Senior Engineers
134 | - Monthly ML Community Meetups
135 | - Internal Tech Talks Participant
136 | - Open Source Contributions
137 | 
138 | ### Mentorship
139 | 
140 | - Currently seeking mentorship in:
141 |   - Technical Leadership
142 |   - Project Management
143 | - Providing peer mentorship in:
144 |   - PyTorch
145 |   - LLM Implementation
146 | 
147 | ## Preferences
148 | 
149 | ### Learning Style
150 | 
151 | - Hands-on Implementation
152 | - Documentation Creation
153 | - Collaborative Problem-solving
154 | 
155 | ### Growth Areas
156 | 
157 | 1. System Architecture Design
158 | 2. Team Leadership
159 | 3. Technical Writing
160 | 
161 | ### Notification Settings
162 | 
163 | - Goal Reminders: Enabled
164 | - Networking Opportunities: Enabled
165 | - Learning Recommendations: Enabled
166 | 
167 | ---
168 | 
169 | *Last Updated: December 10, 2024*
170 | 


--------------------------------------------------------------------------------
/uv.lock:
--------------------------------------------------------------------------------
  1 | version = 1
  2 | requires-python = ">=3.9"
  3 | 
  4 | [[package]]
  5 | name = "certifi"
  6 | version = "2024.8.30"
  7 | source = { registry = "https://pypi.org/simple" }
  8 | sdist = { url = "https://files.pythonhosted.org/packages/b0/ee/9b19140fe824b367c04c5e1b369942dd754c4c5462d5674002f75c4dedc1/certifi-2024.8.30.tar.gz", hash = "sha256:bec941d2aa8195e248a60b31ff9f0558284cf01a52591ceda73ea9afffd69fd9", size = 168507 }
  9 | wheels = [
 10 |     { url = "https://files.pythonhosted.org/packages/12/90/3c9ff0512038035f59d279fddeb79f5f1eccd8859f06d6163c58798b9487/certifi-2024.8.30-py3-none-any.whl", hash = "sha256:922820b53db7a7257ffbda3f597266d435245903d80737e34f8a45ff3e3230d8", size = 167321 },
 11 | ]
 12 | 
 13 | [[package]]
 14 | name = "charset-normalizer"
 15 | version = "3.4.0"
 16 | source = { registry = "https://pypi.org/simple" }
 17 | sdist = { url = "https://files.pythonhosted.org/packages/f2/4f/e1808dc01273379acc506d18f1504eb2d299bd4131743b9fc54d7be4df1e/charset_normalizer-3.4.0.tar.gz", hash = "sha256:223217c3d4f82c3ac5e29032b3f1c2eb0fb591b72161f86d93f5719079dae93e", size = 106620 }
 18 | wheels = [
 19 |     { url = "https://files.pythonhosted.org/packages/69/8b/825cc84cf13a28bfbcba7c416ec22bf85a9584971be15b21dd8300c65b7f/charset_normalizer-3.4.0-cp310-cp310-macosx_10_9_universal2.whl", hash = "sha256:4f9fc98dad6c2eaa32fc3af1417d95b5e3d08aff968df0cd320066def971f9a6", size = 196363 },
 20 |     { url = "https://files.pythonhosted.org/packages/23/81/d7eef6a99e42c77f444fdd7bc894b0ceca6c3a95c51239e74a722039521c/charset_normalizer-3.4.0-cp310-cp310-macosx_10_9_x86_64.whl", hash = "sha256:0de7b687289d3c1b3e8660d0741874abe7888100efe14bd0f9fd7141bcbda92b", size = 125639 },
 21 |     { url = "https://files.pythonhosted.org/packages/21/67/b4564d81f48042f520c948abac7079356e94b30cb8ffb22e747532cf469d/charset_normalizer-3.4.0-cp310-cp310-macosx_11_0_arm64.whl", hash = "sha256:5ed2e36c3e9b4f21dd9422f6893dec0abf2cca553af509b10cd630f878d3eb99", size = 120451 },
 22 |     { url = "https://files.pythonhosted.org/packages/c2/72/12a7f0943dd71fb5b4e7b55c41327ac0a1663046a868ee4d0d8e9c369b85/charset_normalizer-3.4.0-cp310-cp310-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:40d3ff7fc90b98c637bda91c89d51264a3dcf210cade3a2c6f838c7268d7a4ca", size = 140041 },
 23 |     { url = "https://files.pythonhosted.org/packages/67/56/fa28c2c3e31217c4c52158537a2cf5d98a6c1e89d31faf476c89391cd16b/charset_normalizer-3.4.0-cp310-cp310-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:1110e22af8ca26b90bd6364fe4c763329b0ebf1ee213ba32b68c73de5752323d", size = 150333 },
 24 |     { url = "https://files.pythonhosted.org/packages/f9/d2/466a9be1f32d89eb1554cf84073a5ed9262047acee1ab39cbaefc19635d2/charset_normalizer-3.4.0-cp310-cp310-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:86f4e8cca779080f66ff4f191a685ced73d2f72d50216f7112185dc02b90b9b7", size = 142921 },
 25 |     { url = "https://files.pythonhosted.org/packages/f8/01/344ec40cf5d85c1da3c1f57566c59e0c9b56bcc5566c08804a95a6cc8257/charset_normalizer-3.4.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:7f683ddc7eedd742e2889d2bfb96d69573fde1d92fcb811979cdb7165bb9c7d3", size = 144785 },
 26 |     { url = "https://files.pythonhosted.org/packages/73/8b/2102692cb6d7e9f03b9a33a710e0164cadfce312872e3efc7cfe22ed26b4/charset_normalizer-3.4.0-cp310-cp310-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:27623ba66c183eca01bf9ff833875b459cad267aeeb044477fedac35e19ba907", size = 146631 },
 27 |     { url = "https://files.pythonhosted.org/packages/d8/96/cc2c1b5d994119ce9f088a9a0c3ebd489d360a2eb058e2c8049f27092847/charset_normalizer-3.4.0-cp310-cp310-musllinux_1_2_aarch64.whl", hash = "sha256:f606a1881d2663630ea5b8ce2efe2111740df4b687bd78b34a8131baa007f79b", size = 140867 },
 28 |     { url = "https://files.pythonhosted.org/packages/c9/27/cde291783715b8ec30a61c810d0120411844bc4c23b50189b81188b273db/charset_normalizer-3.4.0-cp310-cp310-musllinux_1_2_i686.whl", hash = "sha256:0b309d1747110feb25d7ed6b01afdec269c647d382c857ef4663bbe6ad95a912", size = 149273 },
 29 |     { url = "https://files.pythonhosted.org/packages/3a/a4/8633b0fc1a2d1834d5393dafecce4a1cc56727bfd82b4dc18fc92f0d3cc3/charset_normalizer-3.4.0-cp310-cp310-musllinux_1_2_ppc64le.whl", hash = "sha256:136815f06a3ae311fae551c3df1f998a1ebd01ddd424aa5603a4336997629e95", size = 152437 },
 30 |     { url = "https://files.pythonhosted.org/packages/64/ea/69af161062166b5975ccbb0961fd2384853190c70786f288684490913bf5/charset_normalizer-3.4.0-cp310-cp310-musllinux_1_2_s390x.whl", hash = "sha256:14215b71a762336254351b00ec720a8e85cada43b987da5a042e4ce3e82bd68e", size = 150087 },
 31 |     { url = "https://files.pythonhosted.org/packages/3b/fd/e60a9d9fd967f4ad5a92810138192f825d77b4fa2a557990fd575a47695b/charset_normalizer-3.4.0-cp310-cp310-musllinux_1_2_x86_64.whl", hash = "sha256:79983512b108e4a164b9c8d34de3992f76d48cadc9554c9e60b43f308988aabe", size = 145142 },
 32 |     { url = "https://files.pythonhosted.org/packages/6d/02/8cb0988a1e49ac9ce2eed1e07b77ff118f2923e9ebd0ede41ba85f2dcb04/charset_normalizer-3.4.0-cp310-cp310-win32.whl", hash = "sha256:c94057af19bc953643a33581844649a7fdab902624d2eb739738a30e2b3e60fc", size = 94701 },
 33 |     { url = "https://files.pythonhosted.org/packages/d6/20/f1d4670a8a723c46be695dff449d86d6092916f9e99c53051954ee33a1bc/charset_normalizer-3.4.0-cp310-cp310-win_amd64.whl", hash = "sha256:55f56e2ebd4e3bc50442fbc0888c9d8c94e4e06a933804e2af3e89e2f9c1c749", size = 102191 },
 34 |     { url = "https://files.pythonhosted.org/packages/9c/61/73589dcc7a719582bf56aae309b6103d2762b526bffe189d635a7fcfd998/charset_normalizer-3.4.0-cp311-cp311-macosx_10_9_universal2.whl", hash = "sha256:0d99dd8ff461990f12d6e42c7347fd9ab2532fb70e9621ba520f9e8637161d7c", size = 193339 },
 35 |     { url = "https://files.pythonhosted.org/packages/77/d5/8c982d58144de49f59571f940e329ad6e8615e1e82ef84584c5eeb5e1d72/charset_normalizer-3.4.0-cp311-cp311-macosx_10_9_x86_64.whl", hash = "sha256:c57516e58fd17d03ebe67e181a4e4e2ccab1168f8c2976c6a334d4f819fe5944", size = 124366 },
 36 |     { url = "https://files.pythonhosted.org/packages/bf/19/411a64f01ee971bed3231111b69eb56f9331a769072de479eae7de52296d/charset_normalizer-3.4.0-cp311-cp311-macosx_11_0_arm64.whl", hash = "sha256:6dba5d19c4dfab08e58d5b36304b3f92f3bd5d42c1a3fa37b5ba5cdf6dfcbcee", size = 118874 },
 37 |     { url = "https://files.pythonhosted.org/packages/4c/92/97509850f0d00e9f14a46bc751daabd0ad7765cff29cdfb66c68b6dad57f/charset_normalizer-3.4.0-cp311-cp311-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:bf4475b82be41b07cc5e5ff94810e6a01f276e37c2d55571e3fe175e467a1a1c", size = 138243 },
 38 |     { url = "https://files.pythonhosted.org/packages/e2/29/d227805bff72ed6d6cb1ce08eec707f7cfbd9868044893617eb331f16295/charset_normalizer-3.4.0-cp311-cp311-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:ce031db0408e487fd2775d745ce30a7cd2923667cf3b69d48d219f1d8f5ddeb6", size = 148676 },
 39 |     { url = "https://files.pythonhosted.org/packages/13/bc/87c2c9f2c144bedfa62f894c3007cd4530ba4b5351acb10dc786428a50f0/charset_normalizer-3.4.0-cp311-cp311-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:8ff4e7cdfdb1ab5698e675ca622e72d58a6fa2a8aa58195de0c0061288e6e3ea", size = 141289 },
 40 |     { url = "https://files.pythonhosted.org/packages/eb/5b/6f10bad0f6461fa272bfbbdf5d0023b5fb9bc6217c92bf068fa5a99820f5/charset_normalizer-3.4.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:3710a9751938947e6327ea9f3ea6332a09bf0ba0c09cae9cb1f250bd1f1549bc", size = 142585 },
 41 |     { url = "https://files.pythonhosted.org/packages/3b/a0/a68980ab8a1f45a36d9745d35049c1af57d27255eff8c907e3add84cf68f/charset_normalizer-3.4.0-cp311-cp311-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:82357d85de703176b5587dbe6ade8ff67f9f69a41c0733cf2425378b49954de5", size = 144408 },
 42 |     { url = "https://files.pythonhosted.org/packages/d7/a1/493919799446464ed0299c8eef3c3fad0daf1c3cd48bff9263c731b0d9e2/charset_normalizer-3.4.0-cp311-cp311-musllinux_1_2_aarch64.whl", hash = "sha256:47334db71978b23ebcf3c0f9f5ee98b8d65992b65c9c4f2d34c2eaf5bcaf0594", size = 139076 },
 43 |     { url = "https://files.pythonhosted.org/packages/fb/9d/9c13753a5a6e0db4a0a6edb1cef7aee39859177b64e1a1e748a6e3ba62c2/charset_normalizer-3.4.0-cp311-cp311-musllinux_1_2_i686.whl", hash = "sha256:8ce7fd6767a1cc5a92a639b391891bf1c268b03ec7e021c7d6d902285259685c", size = 146874 },
 44 |     { url = "https://files.pythonhosted.org/packages/75/d2/0ab54463d3410709c09266dfb416d032a08f97fd7d60e94b8c6ef54ae14b/charset_normalizer-3.4.0-cp311-cp311-musllinux_1_2_ppc64le.whl", hash = "sha256:f1a2f519ae173b5b6a2c9d5fa3116ce16e48b3462c8b96dfdded11055e3d6365", size = 150871 },
 45 |     { url = "https://files.pythonhosted.org/packages/8d/c9/27e41d481557be53d51e60750b85aa40eaf52b841946b3cdeff363105737/charset_normalizer-3.4.0-cp311-cp311-musllinux_1_2_s390x.whl", hash = "sha256:63bc5c4ae26e4bc6be6469943b8253c0fd4e4186c43ad46e713ea61a0ba49129", size = 148546 },
 46 |     { url = "https://files.pythonhosted.org/packages/ee/44/4f62042ca8cdc0cabf87c0fc00ae27cd8b53ab68be3605ba6d071f742ad3/charset_normalizer-3.4.0-cp311-cp311-musllinux_1_2_x86_64.whl", hash = "sha256:bcb4f8ea87d03bc51ad04add8ceaf9b0f085ac045ab4d74e73bbc2dc033f0236", size = 143048 },
 47 |     { url = "https://files.pythonhosted.org/packages/01/f8/38842422988b795220eb8038745d27a675ce066e2ada79516c118f291f07/charset_normalizer-3.4.0-cp311-cp311-win32.whl", hash = "sha256:9ae4ef0b3f6b41bad6366fb0ea4fc1d7ed051528e113a60fa2a65a9abb5b1d99", size = 94389 },
 48 |     { url = "https://files.pythonhosted.org/packages/0b/6e/b13bd47fa9023b3699e94abf565b5a2f0b0be6e9ddac9812182596ee62e4/charset_normalizer-3.4.0-cp311-cp311-win_amd64.whl", hash = "sha256:cee4373f4d3ad28f1ab6290684d8e2ebdb9e7a1b74fdc39e4c211995f77bec27", size = 101752 },
 49 |     { url = "https://files.pythonhosted.org/packages/d3/0b/4b7a70987abf9b8196845806198975b6aab4ce016632f817ad758a5aa056/charset_normalizer-3.4.0-cp312-cp312-macosx_10_13_universal2.whl", hash = "sha256:0713f3adb9d03d49d365b70b84775d0a0d18e4ab08d12bc46baa6132ba78aaf6", size = 194445 },
 50 |     { url = "https://files.pythonhosted.org/packages/50/89/354cc56cf4dd2449715bc9a0f54f3aef3dc700d2d62d1fa5bbea53b13426/charset_normalizer-3.4.0-cp312-cp312-macosx_10_13_x86_64.whl", hash = "sha256:de7376c29d95d6719048c194a9cf1a1b0393fbe8488a22008610b0361d834ecf", size = 125275 },
 51 |     { url = "https://files.pythonhosted.org/packages/fa/44/b730e2a2580110ced837ac083d8ad222343c96bb6b66e9e4e706e4d0b6df/charset_normalizer-3.4.0-cp312-cp312-macosx_11_0_arm64.whl", hash = "sha256:4a51b48f42d9358460b78725283f04bddaf44a9358197b889657deba38f329db", size = 119020 },
 52 |     { url = "https://files.pythonhosted.org/packages/9d/e4/9263b8240ed9472a2ae7ddc3e516e71ef46617fe40eaa51221ccd4ad9a27/charset_normalizer-3.4.0-cp312-cp312-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:b295729485b06c1a0683af02a9e42d2caa9db04a373dc38a6a58cdd1e8abddf1", size = 139128 },
 53 |     { url = "https://files.pythonhosted.org/packages/6b/e3/9f73e779315a54334240353eaea75854a9a690f3f580e4bd85d977cb2204/charset_normalizer-3.4.0-cp312-cp312-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:ee803480535c44e7f5ad00788526da7d85525cfefaf8acf8ab9a310000be4b03", size = 149277 },
 54 |     { url = "https://files.pythonhosted.org/packages/1a/cf/f1f50c2f295312edb8a548d3fa56a5c923b146cd3f24114d5adb7e7be558/charset_normalizer-3.4.0-cp312-cp312-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:3d59d125ffbd6d552765510e3f31ed75ebac2c7470c7274195b9161a32350284", size = 142174 },
 55 |     { url = "https://files.pythonhosted.org/packages/16/92/92a76dc2ff3a12e69ba94e7e05168d37d0345fa08c87e1fe24d0c2a42223/charset_normalizer-3.4.0-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:8cda06946eac330cbe6598f77bb54e690b4ca93f593dee1568ad22b04f347c15", size = 143838 },
 56 |     { url = "https://files.pythonhosted.org/packages/a4/01/2117ff2b1dfc61695daf2babe4a874bca328489afa85952440b59819e9d7/charset_normalizer-3.4.0-cp312-cp312-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:07afec21bbbbf8a5cc3651aa96b980afe2526e7f048fdfb7f1014d84acc8b6d8", size = 146149 },
 57 |     { url = "https://files.pythonhosted.org/packages/f6/9b/93a332b8d25b347f6839ca0a61b7f0287b0930216994e8bf67a75d050255/charset_normalizer-3.4.0-cp312-cp312-musllinux_1_2_aarch64.whl", hash = "sha256:6b40e8d38afe634559e398cc32b1472f376a4099c75fe6299ae607e404c033b2", size = 140043 },
 58 |     { url = "https://files.pythonhosted.org/packages/ab/f6/7ac4a01adcdecbc7a7587767c776d53d369b8b971382b91211489535acf0/charset_normalizer-3.4.0-cp312-cp312-musllinux_1_2_i686.whl", hash = "sha256:b8dcd239c743aa2f9c22ce674a145e0a25cb1566c495928440a181ca1ccf6719", size = 148229 },
 59 |     { url = "https://files.pythonhosted.org/packages/9d/be/5708ad18161dee7dc6a0f7e6cf3a88ea6279c3e8484844c0590e50e803ef/charset_normalizer-3.4.0-cp312-cp312-musllinux_1_2_ppc64le.whl", hash = "sha256:84450ba661fb96e9fd67629b93d2941c871ca86fc38d835d19d4225ff946a631", size = 151556 },
 60 |     { url = "https://files.pythonhosted.org/packages/5a/bb/3d8bc22bacb9eb89785e83e6723f9888265f3a0de3b9ce724d66bd49884e/charset_normalizer-3.4.0-cp312-cp312-musllinux_1_2_s390x.whl", hash = "sha256:44aeb140295a2f0659e113b31cfe92c9061622cadbc9e2a2f7b8ef6b1e29ef4b", size = 149772 },
 61 |     { url = "https://files.pythonhosted.org/packages/f7/fa/d3fc622de05a86f30beea5fc4e9ac46aead4731e73fd9055496732bcc0a4/charset_normalizer-3.4.0-cp312-cp312-musllinux_1_2_x86_64.whl", hash = "sha256:1db4e7fefefd0f548d73e2e2e041f9df5c59e178b4c72fbac4cc6f535cfb1565", size = 144800 },
 62 |     { url = "https://files.pythonhosted.org/packages/9a/65/bdb9bc496d7d190d725e96816e20e2ae3a6fa42a5cac99c3c3d6ff884118/charset_normalizer-3.4.0-cp312-cp312-win32.whl", hash = "sha256:5726cf76c982532c1863fb64d8c6dd0e4c90b6ece9feb06c9f202417a31f7dd7", size = 94836 },
 63 |     { url = "https://files.pythonhosted.org/packages/3e/67/7b72b69d25b89c0b3cea583ee372c43aa24df15f0e0f8d3982c57804984b/charset_normalizer-3.4.0-cp312-cp312-win_amd64.whl", hash = "sha256:b197e7094f232959f8f20541ead1d9862ac5ebea1d58e9849c1bf979255dfac9", size = 102187 },
 64 |     { url = "https://files.pythonhosted.org/packages/f3/89/68a4c86f1a0002810a27f12e9a7b22feb198c59b2f05231349fbce5c06f4/charset_normalizer-3.4.0-cp313-cp313-macosx_10_13_universal2.whl", hash = "sha256:dd4eda173a9fcccb5f2e2bd2a9f423d180194b1bf17cf59e3269899235b2a114", size = 194617 },
 65 |     { url = "https://files.pythonhosted.org/packages/4f/cd/8947fe425e2ab0aa57aceb7807af13a0e4162cd21eee42ef5b053447edf5/charset_normalizer-3.4.0-cp313-cp313-macosx_10_13_x86_64.whl", hash = "sha256:e9e3c4c9e1ed40ea53acf11e2a386383c3304212c965773704e4603d589343ed", size = 125310 },
 66 |     { url = "https://files.pythonhosted.org/packages/5b/f0/b5263e8668a4ee9becc2b451ed909e9c27058337fda5b8c49588183c267a/charset_normalizer-3.4.0-cp313-cp313-macosx_11_0_arm64.whl", hash = "sha256:92a7e36b000bf022ef3dbb9c46bfe2d52c047d5e3f3343f43204263c5addc250", size = 119126 },
 67 |     { url = "https://files.pythonhosted.org/packages/ff/6e/e445afe4f7fda27a533f3234b627b3e515a1b9429bc981c9a5e2aa5d97b6/charset_normalizer-3.4.0-cp313-cp313-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:54b6a92d009cbe2fb11054ba694bc9e284dad30a26757b1e372a1fdddaf21920", size = 139342 },
 68 |     { url = "https://files.pythonhosted.org/packages/a1/b2/4af9993b532d93270538ad4926c8e37dc29f2111c36f9c629840c57cd9b3/charset_normalizer-3.4.0-cp313-cp313-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:1ffd9493de4c922f2a38c2bf62b831dcec90ac673ed1ca182fe11b4d8e9f2a64", size = 149383 },
 69 |     { url = "https://files.pythonhosted.org/packages/fb/6f/4e78c3b97686b871db9be6f31d64e9264e889f8c9d7ab33c771f847f79b7/charset_normalizer-3.4.0-cp313-cp313-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:35c404d74c2926d0287fbd63ed5d27eb911eb9e4a3bb2c6d294f3cfd4a9e0c23", size = 142214 },
 70 |     { url = "https://files.pythonhosted.org/packages/2b/c9/1c8fe3ce05d30c87eff498592c89015b19fade13df42850aafae09e94f35/charset_normalizer-3.4.0-cp313-cp313-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:4796efc4faf6b53a18e3d46343535caed491776a22af773f366534056c4e1fbc", size = 144104 },
 71 |     { url = "https://files.pythonhosted.org/packages/ee/68/efad5dcb306bf37db7db338338e7bb8ebd8cf38ee5bbd5ceaaaa46f257e6/charset_normalizer-3.4.0-cp313-cp313-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:e7fdd52961feb4c96507aa649550ec2a0d527c086d284749b2f582f2d40a2e0d", size = 146255 },
 72 |     { url = "https://files.pythonhosted.org/packages/0c/75/1ed813c3ffd200b1f3e71121c95da3f79e6d2a96120163443b3ad1057505/charset_normalizer-3.4.0-cp313-cp313-musllinux_1_2_aarch64.whl", hash = "sha256:92db3c28b5b2a273346bebb24857fda45601aef6ae1c011c0a997106581e8a88", size = 140251 },
 73 |     { url = "https://files.pythonhosted.org/packages/7d/0d/6f32255c1979653b448d3c709583557a4d24ff97ac4f3a5be156b2e6a210/charset_normalizer-3.4.0-cp313-cp313-musllinux_1_2_i686.whl", hash = "sha256:ab973df98fc99ab39080bfb0eb3a925181454d7c3ac8a1e695fddfae696d9e90", size = 148474 },
 74 |     { url = "https://files.pythonhosted.org/packages/ac/a0/c1b5298de4670d997101fef95b97ac440e8c8d8b4efa5a4d1ef44af82f0d/charset_normalizer-3.4.0-cp313-cp313-musllinux_1_2_ppc64le.whl", hash = "sha256:4b67fdab07fdd3c10bb21edab3cbfe8cf5696f453afce75d815d9d7223fbe88b", size = 151849 },
 75 |     { url = "https://files.pythonhosted.org/packages/04/4f/b3961ba0c664989ba63e30595a3ed0875d6790ff26671e2aae2fdc28a399/charset_normalizer-3.4.0-cp313-cp313-musllinux_1_2_s390x.whl", hash = "sha256:aa41e526a5d4a9dfcfbab0716c7e8a1b215abd3f3df5a45cf18a12721d31cb5d", size = 149781 },
 76 |     { url = "https://files.pythonhosted.org/packages/d8/90/6af4cd042066a4adad58ae25648a12c09c879efa4849c705719ba1b23d8c/charset_normalizer-3.4.0-cp313-cp313-musllinux_1_2_x86_64.whl", hash = "sha256:ffc519621dce0c767e96b9c53f09c5d215578e10b02c285809f76509a3931482", size = 144970 },
 77 |     { url = "https://files.pythonhosted.org/packages/cc/67/e5e7e0cbfefc4ca79025238b43cdf8a2037854195b37d6417f3d0895c4c2/charset_normalizer-3.4.0-cp313-cp313-win32.whl", hash = "sha256:f19c1585933c82098c2a520f8ec1227f20e339e33aca8fa6f956f6691b784e67", size = 94973 },
 78 |     { url = "https://files.pythonhosted.org/packages/65/97/fc9bbc54ee13d33dc54a7fcf17b26368b18505500fc01e228c27b5222d80/charset_normalizer-3.4.0-cp313-cp313-win_amd64.whl", hash = "sha256:707b82d19e65c9bd28b81dde95249b07bf9f5b90ebe1ef17d9b57473f8a64b7b", size = 102308 },
 79 |     { url = "https://files.pythonhosted.org/packages/54/2f/28659eee7f5d003e0f5a3b572765bf76d6e0fe6601ab1f1b1dd4cba7e4f1/charset_normalizer-3.4.0-cp39-cp39-macosx_10_9_universal2.whl", hash = "sha256:980b4f289d1d90ca5efcf07958d3eb38ed9c0b7676bf2831a54d4f66f9c27dfa", size = 196326 },
 80 |     { url = "https://files.pythonhosted.org/packages/d1/18/92869d5c0057baa973a3ee2af71573be7b084b3c3d428fe6463ce71167f8/charset_normalizer-3.4.0-cp39-cp39-macosx_10_9_x86_64.whl", hash = "sha256:f28f891ccd15c514a0981f3b9db9aa23d62fe1a99997512b0491d2ed323d229a", size = 125614 },
 81 |     { url = "https://files.pythonhosted.org/packages/d6/27/327904c5a54a7796bb9f36810ec4173d2df5d88b401d2b95ef53111d214e/charset_normalizer-3.4.0-cp39-cp39-macosx_11_0_arm64.whl", hash = "sha256:a8aacce6e2e1edcb6ac625fb0f8c3a9570ccc7bfba1f63419b3769ccf6a00ed0", size = 120450 },
 82 |     { url = "https://files.pythonhosted.org/packages/a4/23/65af317914a0308495133b2d654cf67b11bbd6ca16637c4e8a38f80a5a69/charset_normalizer-3.4.0-cp39-cp39-manylinux_2_17_aarch64.manylinux2014_aarch64.whl", hash = "sha256:bd7af3717683bea4c87acd8c0d3d5b44d56120b26fd3f8a692bdd2d5260c620a", size = 140135 },
 83 |     { url = "https://files.pythonhosted.org/packages/f2/41/6190102ad521a8aa888519bb014a74251ac4586cde9b38e790901684f9ab/charset_normalizer-3.4.0-cp39-cp39-manylinux_2_17_ppc64le.manylinux2014_ppc64le.whl", hash = "sha256:5ff2ed8194587faf56555927b3aa10e6fb69d931e33953943bc4f837dfee2242", size = 150413 },
 84 |     { url = "https://files.pythonhosted.org/packages/7b/ab/f47b0159a69eab9bd915591106859f49670c75f9a19082505ff16f50efc0/charset_normalizer-3.4.0-cp39-cp39-manylinux_2_17_s390x.manylinux2014_s390x.whl", hash = "sha256:e91f541a85298cf35433bf66f3fab2a4a2cff05c127eeca4af174f6d497f0d4b", size = 142992 },
 85 |     { url = "https://files.pythonhosted.org/packages/28/89/60f51ad71f63aaaa7e51a2a2ad37919985a341a1d267070f212cdf6c2d22/charset_normalizer-3.4.0-cp39-cp39-manylinux_2_17_x86_64.manylinux2014_x86_64.whl", hash = "sha256:309a7de0a0ff3040acaebb35ec45d18db4b28232f21998851cfa709eeff49d62", size = 144871 },
 86 |     { url = "https://files.pythonhosted.org/packages/0c/48/0050550275fea585a6e24460b42465020b53375017d8596c96be57bfabca/charset_normalizer-3.4.0-cp39-cp39-manylinux_2_5_i686.manylinux1_i686.manylinux_2_17_i686.manylinux2014_i686.whl", hash = "sha256:285e96d9d53422efc0d7a17c60e59f37fbf3dfa942073f666db4ac71e8d726d0", size = 146756 },
 87 |     { url = "https://files.pythonhosted.org/packages/dc/b5/47f8ee91455946f745e6c9ddbb0f8f50314d2416dd922b213e7d5551ad09/charset_normalizer-3.4.0-cp39-cp39-musllinux_1_2_aarch64.whl", hash = "sha256:5d447056e2ca60382d460a604b6302d8db69476fd2015c81e7c35417cfabe4cd", size = 141034 },
 88 |     { url = "https://files.pythonhosted.org/packages/84/79/5c731059ebab43e80bf61fa51666b9b18167974b82004f18c76378ed31a3/charset_normalizer-3.4.0-cp39-cp39-musllinux_1_2_i686.whl", hash = "sha256:20587d20f557fe189b7947d8e7ec5afa110ccf72a3128d61a2a387c3313f46be", size = 149434 },
 89 |     { url = "https://files.pythonhosted.org/packages/ca/f3/0719cd09fc4dc42066f239cb3c48ced17fc3316afca3e2a30a4756fe49ab/charset_normalizer-3.4.0-cp39-cp39-musllinux_1_2_ppc64le.whl", hash = "sha256:130272c698667a982a5d0e626851ceff662565379baf0ff2cc58067b81d4f11d", size = 152443 },
 90 |     { url = "https://files.pythonhosted.org/packages/f7/0e/c6357297f1157c8e8227ff337e93fd0a90e498e3d6ab96b2782204ecae48/charset_normalizer-3.4.0-cp39-cp39-musllinux_1_2_s390x.whl", hash = "sha256:ab22fbd9765e6954bc0bcff24c25ff71dcbfdb185fcdaca49e81bac68fe724d3", size = 150294 },
 91 |     { url = "https://files.pythonhosted.org/packages/54/9a/acfa96dc4ea8c928040b15822b59d0863d6e1757fba8bd7de3dc4f761c13/charset_normalizer-3.4.0-cp39-cp39-musllinux_1_2_x86_64.whl", hash = "sha256:7782afc9b6b42200f7362858f9e73b1f8316afb276d316336c0ec3bd73312742", size = 145314 },
 92 |     { url = "https://files.pythonhosted.org/packages/73/1c/b10a63032eaebb8d7bcb8544f12f063f41f5f463778ac61da15d9985e8b6/charset_normalizer-3.4.0-cp39-cp39-win32.whl", hash = "sha256:2de62e8801ddfff069cd5c504ce3bc9672b23266597d4e4f50eda28846c322f2", size = 94724 },
 93 |     { url = "https://files.pythonhosted.org/packages/c5/77/3a78bf28bfaa0863f9cfef278dbeadf55efe064eafff8c7c424ae3c4c1bf/charset_normalizer-3.4.0-cp39-cp39-win_amd64.whl", hash = "sha256:95c3c157765b031331dd4db3c775e58deaee050a3042fcad72cbc4189d7c8dca", size = 102159 },
 94 |     { url = "https://files.pythonhosted.org/packages/bf/9b/08c0432272d77b04803958a4598a51e2a4b51c06640af8b8f0f908c18bf2/charset_normalizer-3.4.0-py3-none-any.whl", hash = "sha256:fe9f97feb71aa9896b81973a7bbada8c49501dc73e58a10fcef6663af95e5079", size = 49446 },
 95 | ]
 96 | 
 97 | [[package]]
 98 | name = "idna"
 99 | version = "3.10"
100 | source = { registry = "https://pypi.org/simple" }
101 | sdist = { url = "https://files.pythonhosted.org/packages/f1/70/7703c29685631f5a7590aa73f1f1d3fa9a380e654b86af429e0934a32f7d/idna-3.10.tar.gz", hash = "sha256:12f65c9b470abda6dc35cf8e63cc574b1c52b11df2c86030af0ac09b01b13ea9", size = 190490 }
102 | wheels = [
103 |     { url = "https://files.pythonhosted.org/packages/76/c6/c88e154df9c4e1a2a66ccf0005a88dfb2650c1dffb6f5ce603dfbd452ce3/idna-3.10-py3-none-any.whl", hash = "sha256:946d195a0d259cbba61165e88e65941f16e9b36ea6ddb97f00452bae8b1287d3", size = 70442 },
104 | ]
105 | 
106 | [[package]]
107 | name = "mcp-agent-router"
108 | version = "0.1.0"
109 | source = { virtual = "." }
110 | dependencies = [
111 |     { name = "requests" },
112 | ]
113 | 
114 | [package.metadata]
115 | requires-dist = [{ name = "requests", specifier = ">=2.32.3" }]
116 | 
117 | [[package]]
118 | name = "requests"
119 | version = "2.32.3"
120 | source = { registry = "https://pypi.org/simple" }
121 | dependencies = [
122 |     { name = "certifi" },
123 |     { name = "charset-normalizer" },
124 |     { name = "idna" },
125 |     { name = "urllib3" },
126 | ]
127 | sdist = { url = "https://files.pythonhosted.org/packages/63/70/2bf7780ad2d390a8d301ad0b550f1581eadbd9a20f896afe06353c2a2913/requests-2.32.3.tar.gz", hash = "sha256:55365417734eb18255590a9ff9eb97e9e1da868d4ccd6402399eaf68af20a760", size = 131218 }
128 | wheels = [
129 |     { url = "https://files.pythonhosted.org/packages/f9/9b/335f9764261e915ed497fcdeb11df5dfd6f7bf257d4a6a2a686d80da4d54/requests-2.32.3-py3-none-any.whl", hash = "sha256:70761cfe03c773ceb22aa2f671b4757976145175cdfca038c02654d061d6dcc6", size = 64928 },
130 | ]
131 | 
132 | [[package]]
133 | name = "urllib3"
134 | version = "2.2.3"
135 | source = { registry = "https://pypi.org/simple" }
136 | sdist = { url = "https://files.pythonhosted.org/packages/ed/63/22ba4ebfe7430b76388e7cd448d5478814d3032121827c12a2cc287e2260/urllib3-2.2.3.tar.gz", hash = "sha256:e7d814a81dad81e6caf2ec9fdedb284ecc9c73076b62654547cc64ccdcae26e9", size = 300677 }
137 | wheels = [
138 |     { url = "https://files.pythonhosted.org/packages/ce/d9/5f4c13cecde62396b0d3fe530a50ccea91e7dfc1ccf0e09c228841bb5ba8/urllib3-2.2.3-py3-none-any.whl", hash = "sha256:ca899ca043dcb1bafa3e262d73aa25c465bfb49e0bd9dd5d59f1d0acba2f8fac", size = 126338 },
139 | ]
140 |