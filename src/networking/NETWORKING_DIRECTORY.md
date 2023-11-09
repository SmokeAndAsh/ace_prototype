# Networking Directory
```
networking <-- Handles APIs and Northbound/Southbound buses
├── networking.py
├── error_handling/
│     ├── client_error_handler.py <-- Handles client-specific errors
│     ├── gateway_error_handler.py <-- Handles gateway-specific errors
│     ├── llm_error_handler.py <-- Handles LLM-specific errors
│     └── network_error_handler.py <-- Handles network-specific errors
├── gateway/ <-- Handles sensory data
│     ├── gateway.py
│     ├── clients/ <-- External API clients
│     │         └── client.py
│     └── llm/ <-- Language model inferences
│                 ├── llm_client.py
│                 ├── llm_server.py
│                 ├── llm_utils.py
│                 └── models/ <-- Language model files
│                            ├── athena-v4.Q4_K_M.gguf
│                            ├── athena-v4.Q4_K_M.gguf
│                            ├── llama-2-7b-chat.Q4_K_M.gguf
│                            └── llama-2-7b-chat.Q5_K_S.gguf
├── northbound_bus/ <-- Telemetry
│     └── northbound_bus.py
└── southbound_bus/ <-- Control
      └── southbound_bus.py
```