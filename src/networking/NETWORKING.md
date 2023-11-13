# Networking Directory
Module that handles the API processes and north and southbound data bus system for the ACE agent.

```
networking <-- Handles APIs and Northbound/Southbound buses
├── NETWORKING.md <-- Here
├── networking_main.py <-- Starts `Networking` module
├── __init__.py
├── ace_networking.yaml
├── Dockerfile
├── requirements.txt
├── northbound_bus.py <-- Telemetry
├── southbound_bus.py <-- Control
├── error_handling/
│     ├── client_error_handler.py <-- Handles client-specific errors
│     ├── gateway_error_handler.py <-- Handles gateway-specific errors
│     ├── llm_error_handler.py <-- Handles LLM-specific errors
│     └── network_error_handler.py <-- Handles network-specific errors
├── gateway/ <-- Handles sensory data
│     ├── clients/ <-- External API clients
│     │   ├── discord_cli.py <-- Handles discord interactions
│     │   ├── huggingface_cli.py <-- Handles huggingface interactions
│     │   └── terminal_cli.py <-- Handles commandline interactions
│     ├── connections/ <-- Manages connections, requests, and queues
│     │   ├── http_connection.py <-- Handles http requests and connections
│     │   └── kafka_connection.py <-- Handles apache kafka processes  
│     └── llm/ <-- Language model inferences
│         ├── llm_config.py <-- Language model settings     
│         ├── llm_client.py <-- Language model client functions
│         ├── llm_prompt_handler.py <-- Handles dynamic language model prompts         
│         ├── llm_server.py <-- Language model server functions
│         ├── models/ <-- Language model files
│         │   └── llm_model.gguf <-- Example
│         └── prompt_templates/ <-- Prompt templates for language models
│             └── alpaca.txt <-- Example
└── logs/ <-- Logs from the Northbound Bus
      ├── nb_logging.py <-- Logs networking-related telemetry
      ├── northbound_log.txt
      └── southbound_log.txt
```

# Networking Stack
