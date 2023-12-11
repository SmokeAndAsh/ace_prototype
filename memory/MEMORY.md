# Memory Directory
Module managing long-term, short-term and reflective data for the ACE agent.

```
memory/ <-- Handles short and long term data management
├── MEMORY.md
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── kb/
│   ├── memory_deployment.yaml
│   ├── memory_secret.yaml
│   ├── memory_service.yaml
│   └── psql_config.yaml
└── src/
    ├── memory_main.py <-- Starts `Memory` module  
    ├── error_handling/
    │   ├── ltm_error_handler.py <-- Handles long-term memory errors
    │   ├── stm_error_handler.py <-- Handles short-term memory errors
    │   └── ref_error_handler.py <-- Handles reflective memory errors
    ├── short_term/ <-- Cached, refreshed frequently
    │   ├── stm_config.yaml
    │   ├── stm_volume.yaml
    │   └── stm_main.py
    ├── long_term/ <-- Vectorized, reviewed periodically
    │   ├── ltm_config.yaml
    │   ├── ltm_volume.yaml
    │   └── ltm_main.py
    └── reflective/ <-- NLP Interpreted, like a "journal"
    │   ├── ref_config.yaml
    │   ├── ref_volume.yaml
        └── ref_main.py
```

# Memory Stack