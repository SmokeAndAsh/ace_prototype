# Cognition Directory
This module can leverage natural language processing libraries like NLTK or spaCy for handling natural language data.

```
cognition/ <-- High-level cognitive processes
├── __init__.py
├── COGNITION_DIRECTORY.md <-- Here
├── error_handling/
│     ├── focus_error_handler.py <-- Handles Focus-module errors
│     ├── global_error_handler.py <-- Handles Global-module errors
│     └── independent_error_handler.py <-- Handles Independent-module errors
├── global/ <-- Global cognitive module
│     ├── global_const.py <-- Global constants
│     ├── global_functions.py <-- Global functions
│     └── global_prompts/ <-- Prompts for the global module
│         ├── global_prompts.txt <-- Global prompts
│         ├── layer_01_aspirational.txt <-- Ace layer prompt
│         └── layer_02_global_strategy.txt <-- Ace layer prompt
├── independent/ <-- Independent cognitive module
│     ├── agent_persona_example.py <-- Example of an agent persona
│     ├── independent_const.py <-- Agent-specific constants
│     ├── independent_functions.py <-- Agent-specific functions
│     └── independent_prompts/ <-- Prompts for the independent module
│         ├── independent_prompts.txt <-- Agent-specific prompts
│         ├── layer_03_agent_model.txt  <-- Ace layer prompt
│         └── layer_04_executive_function.txt <-- Ace layer prompt
└── focus/ <-- Focus cognitive module
      ├── focus_const.py <-- Task-specific constants
      ├── focus_functions.py <-- Task-specific functions
      ├── task_list.py <-- List of available task functions
      ├── focus_actions/ <-- Classes for specific agent actions
      │   ├── action_memory.py <-- Actions related to agent memory
      │   ├── action_message.py <-- Actions related to text-based communications
      │   ├── action_perform.py <-- Class for evaluating and executing actions
      │   ├── action_time.py <-- Actions related to time management
      │   └── action_web.py <-- Actions related to web content and media
      └── focus_prompts/ <-- Prompts for the focus module
          ├── focus_prompts.txt <-- Task-specific prompts
          ├── layer_05_cognitive_control.txt <-- Ace layer prompt
          └── layer_06_task_prosecution.txt <-- Ace layer prompt
```