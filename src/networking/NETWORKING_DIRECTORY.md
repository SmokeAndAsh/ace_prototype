# Networking Directory
Module that handles the API processes and north and southbound data bus system for the ACE agent.

```
networking <-- Handles APIs and Northbound/Southbound buses
├── __init__.py
├── northbound_bus.py <-- Telemetry
├── southbound_bus.py <-- Control
├── error_handling/
│     ├── client_error_handler.py <-- Handles client-specific errors
│     ├── gateway_error_handler.py <-- Handles gateway-specific errors
│     ├── llm_error_handler.py <-- Handles LLM-specific errors
│     ├── network_error_handler.py <-- Handles network-specific errors
│     └── logs/
│         ├── nb_logging.py <-- Logs networking-related telemetry
│         ├── northbound_log.txt
│         └── southbound_log.txt
└──  gateway <-- Handles sensory data
      ├── clients/ <-- External API clients
      │   ├── discord.py <-- Handles discord interactions
      │   └── terminal.py <-- Handles commandline interactions
      └── llm/ <-- Language model inferences
          ├── llm_client.py <-- Language model client functions
          ├── llm_server.py <-- Language model server functions
          ├── models/ <-- Language model files
          │   └── llm_model.gguf <-- Example
          └── prompt_templates/ <-- Prompt templates for language models
              └── alpaca.txt <-- Example
```