# Cognition Directory
```
cognition/ <-- high-level cognitive processes
├── global/ <-- global cognitive module
│     ├── global_const.py <-- global constants
│     ├── global_functions.py <-- global functions
│     └── global_prompts/ <-- prompts for the global module
│                 ├── global_prompts.txt <-- global prompts
│                 ├── layer_01_aspirational.txt <-- ace layer prompt
│                 └── layer_02_global_strategy.txt <-- ace layer prompt
├── independent/ <-- independent cognitive module
│     ├── independent_const.py <-- agent-specific constants
│     ├── independent_functions.py <-- agent-specific functions
│     └── independent_prompts/ <-- prompts for the independent module
│                 ├── independent_prompts.txt <-- agent-specific prompts
│                 ├── layer_03_agent_model.txt  <-- ace layer prompt
│                 └── layer_04_executive_function.txt <-- ace layer prompt
└── focus/ <-- focus cognitive module
        ├── focus_const.py <-- task-specific constants
        ├── focus_functions.py <-- task-specific functions
        ├── task_list.py <-- list of available task functions
        └── focus_prompts/ <-- prompts for the focus module
                    ├── focus_prompts.txt <-- task-specific prompts
                    ├── layer_05_cognitive_control.txt <-- ace layer prompt
                    └── layer_06_task_prosecution.txt <-- ace layer prompt
```