# Network Directory
Module that handles the API processes, connections and queues for the ACE agent.

```
network <-- Handles APIs, connections and queues
├── NETWORK.md
├── Dockerfile
├── pyproject.toml
├── kb/
│   ├── network_config.yaml
│   ├── network_deployment.yaml
│   ├── network_secret.yaml
│   └── network_service.yaml
└── src/
    ├── network_start.py <-- Starts `Network` module
    ├── network_diagnostics.py <-- Checks `Network` module health
    ├── error_handling/ <-- Network module error handling
    │   ├── network_error_handler.py <-- Handles general network errors    
    │   ├── client_error_handler.py <-- Handles client-specific errors
    │   └── gateway_error_handler.py <-- Handles gateway-specific errors    
    ├── gateway/ <-- Handles API gateway
    │   ├── gateway_main.py <-- Primary gateway, handles clients, connections and routes
    │   ├── api_routes.py <-- Manages internal and external API routes
    │   ├── client_handler.py <-- Handles generalized client utilities
    │   └── clients/ <-- Holds code for interactions with external clients
    │       ├── comm_clients/ <-- Handles `CommunicationClient` interactions
    │       ├── lang_clients/ <-- Handles `LanguageClient` interactions
    │       ├── sys_clients/ <-- Handles `SystemClient` interactions
    │       └── web_clients/ <-- Handles `WebClient` interactions
    ├── connections/ <-- Manages connections, requests, and queues
    │   ├── db_connections/ <-- Handles database requests and connections
    │   ├── http_connections/ <-- Handles http requests and connections
    │   └── queue_connections/ <-- Handles message queue requests and connections
    └── tests/ <-- Various testing files
```

# Network Stack
- confluent-kafka
- discord.py
- Flask
- requests
- PyNaCl

# Network Module
## Start Up
1. Build module image (Podman)
```
podman build -t localhost/network-module:latest .
```
```
podman save localhost/network-module:latest -o network-module.tar`
```
2. Load module image (Kind)
```
kind load image-archive network-module.tar --name ace-cluster
```
```
kubectl apply -f kb/
```
3. Check deployment (Kubectl)
```
kubectl get deployments
```
```
kubectl get pods
```
```
kubectl logs network-deployment
```


