# Cognition Directory
Module handles language model functions and prompts, directing higher processes for the agent.

```
cognition/ <-- High-level cognitive processes
├── COGNITION.md <-- Here
├── cognition_main.py <-- Starts `Cognition` module
├── __init__.py
├── ace_cognition.yaml
├── Dockerfile
├── requirements.txt
├── error_handling/
│     ├── focus_error_handler.py <-- Handles Focus-module errors
│     ├── global_error_handler.py <-- Handles Global-module errors
│     └── independent_error_handler.py <-- Handles Independent-module errors
├── global_mod/ <-- Global cognitive module
│     ├── global_const.py <-- Global constants
│     ├── global_functions.py <-- Global functions
│     └── global_prompts/ <-- Prompts for the global module
│         ├── GLOBAL_MISSION.md <-- Global mission statement
│         ├── HEURISTIC_IMPERATIVES.md <-- Hieuristic imperatives statement
│         ├── UDHR.md <-- Universal Declaration of Human Rights
│         ├── L1_aspirational.md <-- Ace layer prompt
│         └── L2_global_strategy.md <-- Ace layer prompt
├── independent_mod/ <-- Independent cognitive module
│     ├── agent_persona_example.py <-- Example of an agent persona
│     ├── independent_const.py <-- Agent-specific constants
│     ├── independent_functions.py <-- Agent-specific functions
│     └── independent_prompts/ <-- Prompts for the independent module
│         ├── INDEPENDENT_MISSION.md <-- Independent mission statement
│         ├── PERSONA.md <-- Agent persona facts
│         ├── PERSONAL_PRINCIPLES.md <-- Agent-specific principles
│         ├── L3_agent_model.md  <-- Ace layer prompt
│         └── L4_executive_function.md <-- Ace layer prompt
└── focus_mod/ <-- Focus cognitive module
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
          ├── FOCUS_MISSION.md <-- Focus mission statement
          ├── CURRENT_TASK.md <-- Current task breakdown
          ├── L5_cognitive_control.md <-- Ace layer prompt
          └── L6_task_prosecution.md <-- Ace layer prompt
```

# Cognition Stack
- Kubernetes (kubectl)
- Markdown (markdown)
- Podman (podman)
- Python (python:3.10-slim)