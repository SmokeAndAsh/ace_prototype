# Network Directory
Module that handles the API processes, connections and queues for the ACE agent.

```
network <-- Handles APIs, connections and queues
├── NETWORK.md
├── Dockerfile
├── requirements.txt
├── .dockerignore
├── kb/
│   ├── network_deployment.yaml
│   ├── network_secret.yaml
│   └── network_service.yaml
└── src/
    ├── network_main.py <-- Starts `Networking` module
    ├── error_handling/
    │   ├── client_error_handler.py <-- Handles client-specific errors
    │   ├── connection_error_handler.py <-- Handles connection-specific errors
    │   └── gateway_error_handler.py <-- Handles gateway-specific errors    
    ├── clients/ <-- Manages interactions with external clients
    │   ├── discord_cli.py <-- Handles discord interactions
    │   ├── huggingface_cli.py <-- Handles huggingface interactions
    │   ├── terminal_cli.py <-- Handles commandline interactions
    │   └── web_cli.py <-- WebUI for `Networking` module
    ├── connections/ <-- Manages connections, requests, and queues
    │   ├── http_connection.py <-- Handles http requests and connections
    │   └── kafka_connection.py <-- Handles apache kafka processes
    └── gateway/ <-- Handles API gateway
        ├── api_example.py    
        └── query_example.py
```

# Network Stack
Flask