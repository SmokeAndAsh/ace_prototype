# Memory Directory
Module managing long-term, short-term and reflective data for the ACE agent.

```
memory/ <-- Handles short and long term data management
├── MEMORY.md <-- Here
├── memory_main.py <-- Starts `Memory` module
├── __init__.py
├── ace_memory.yaml
├── Dockerfile
├── requirements.txt
├── error_handling/
│     ├── ltm_error_handler.py <-- Handles long-term memory errors
│     ├── stm_error_handler.py <-- Handles short-term memory errors
│     └── rm_error_handler.py <-- Handles reflective memory errors
├── short_term_data/ <-- Cached, refreshed frequently
│   └── stm_main.py
├── long_term_data/ <-- Vectorized, reviewed periodically
│   └── ltm_main.py
└── reflective_data/ <-- NLP Interpreted, like a "journal"
    └── reflective_main.py
```

# Memory Stack