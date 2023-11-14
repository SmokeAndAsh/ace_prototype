# Network Directory
Module that handles the API processes and north and southbound data bus system for the ACE agent.

```
network <-- Handles APIs and Northbound/Southbound buses
├── NETWORK.md
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── kb/
│   ├── pod/
│   │   └── ace_network.yaml
│   ├── service/
│   │   └── network_service.yaml
│   └── deployment/
│       └── network_deployment.yaml
└── src/
    ├── network_main.py <-- Starts `Networking` module
    ├── northbound_bus.py <-- Telemetry
    ├── southbound_bus.py <-- Control  
    ├── error_handling/
    │   ├── client_error_handler.py <-- Handles client-specific errors
    │   ├── gateway_error_handler.py <-- Handles gateway-specific errors
    │   ├── llm_error_handler.py <-- Handles LLM-specific errors
    │   └── network_error_handler.py <-- Handles network-specific errors
    ├── gateway/
    │   ├── clients/
    │   │   ├── discord_cli.py <-- Handles discord interactions
    │   │   ├── huggingface_cli.py <-- Handles huggingface interactions
    │   │   ├── terminal_cli.py <-- Handles commandline interactions
    │   │   └── web_cli.py <-- WebUI for `Networking` module
    │   ├── connections/ <-- Manages connections, requests, and queues
    │   │   ├── http_connection.py <-- Handles http requests and connections
    │   │   └── kafka_connection.py <-- Handles apache kafka processes
    │   └── llm/ <-- Language model inferences
    │       ├── llm_config.py <-- Language model settings
    │       ├── llm_client.py <-- Language model client functions
    │       ├── llm_prompt_handler.py <-- Handles dynamic language model prompts
    │       ├── llm_server.py <-- Language model server functions
    │       └── prompt_templates/ <-- Prompt templates for language models
    │           └── alpaca.txt <-- Example
    └── logs/ <-- Logs from the Northbound Bus
        ├── nb_logging.py <-- Logs networking-related telemetry
        ├── northbound_log.txt
        └── southbound_log.txt
```

# Network Stack
- Flask (flask)
- Kubernetes (kubectl)
- Markdown (markdown)
- Podman (podman)
- Python (python:3.10-slim)