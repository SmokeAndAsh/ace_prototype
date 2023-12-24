# ACE Prototype Overview
A very in-process prototype for an Autonomous Cognitive Entity based on David Shapiro's [ACE Framework](https://github.com/daveshap/ACE_Framework/blob/main/ACE_Framework.md).

`start.py` is currently set up to run a command line test with a local language model.

```
ace/ <-- Project root
├── README.md
├── start.py <-- Currently for testing purposes
├── library/ <-- Library for system models
├── system/ <-- ACE system management
│   ├── SYSTEM.md
│   ├── northbound_bus.py <-- Telemetry
│   ├── southbound_bus.py <-- Control
│   └── logs/ <-- Logs from the bus system
├── cognition/ <-- High-level cognitive processes for the agent
│   ├── COGNITION.md
│   ├── Dockerfile
│   ├── pyproject.toml
│   ├── kb/ <-- Kubernetes files
│   └── src/
│       ├── memory_start.py <-- Starts `Cognition` module
│       ├── memory_diagnostics.py <-- Checks `Cognition` module health
│       ├── error_handling/ <-- `Cognition` module error handling
│       ├── global_mod/ <-- Global cognitive module
│       ├── independent_mod/ <-- Independent cognitive module
│       ├── focus_mod/ <-- Focus cognitive module
│       └── tests/ <-- Various testing files
├── memory/ <-- Handles short and long term data management
│   ├── MEMORY.md
│   ├── Dockerfile
│   ├── pyproject.toml
│   ├── kb/ <-- Kubernetes files
│   └── src/
│       ├── memory_start.py <-- Starts `Memory` module
│       ├── memory_diagnostics.py <-- Checks `Memory` module health
│       ├── error_handling/ <-- `Memory` module error handling
│       ├── short_term/ <-- Cached, refreshed frequently
│       ├── long_term/ <-- Vectorized, reviewed periodically
│       ├── reflective/ <-- NLP Interpreted, like a "journal"
│       └── tests/ <-- Various testing files
└── network/ <-- Handles APIs, connections and queues
    ├── NETWORK.md
    ├── Dockerfile
    ├── pyproject.toml
    ├── kb/ <-- Kubernetes files
    └── src/
        ├── network_start.py <-- Starts `Network` module
        ├── network_diagnostics.py <-- Checks `Network` module health
        ├── error_handling/ <-- `Network` module error handling
        ├── gateway/ <-- Handles API gateway
        ├── connections/ <-- Manages connections, requests, and queues
        └── tests/ <-- Various testing files
```

# Prototype Overview

**System** handles the `Northbound` and `Southbound` busses that receives and delivers information securely throughout the ACE agent's system.

**Cognition** handles high-level and abstract concepts like personality, task distribution and prioritization, ethical considerations and such. Practically speaking, it would be the final arbiter in how an agent executes a task if there's something causing indecision in the other modules.

**Memory** holds the data from previous interactions, successes, and failures so that the agent can reflect on and recall the appropriate information for responses to external stimulus, like conversations and eventually sensory data and things like that.

**Network** handles the interactions between the internal ACE modules and external functions and services, API monitoring and management, and secure transfer and management of external data.

**Example:** Language models exist are managed by the `Cognition` module which is influenced by the data it pulls and reflects on from the `Memory` module, and then returns a decision for a response or action to the `Network` module to execute through relevant APIs.

## System
The **Northbound Bus** carries internal and external data through the ACE agent. Provides telemetry and useful data to flow through the agent while logging and handling errors and exceptions as they arise.

The **Southbound Bus** carries instructions through the ACE agent.  Provides direction and guidance for processes and functions throughout the system.

**Example:** The `Southbound Bus` directs the appropriate processes in response to the input received from a given module. If an error occurs or telemetry is meant to be documented, the `Northbound Bus` will track and log this data, and respond to any exceptions as needed.

## Cognition

The **Global** module handles the `Aspirational Layer` and the `Global Strategy Layer`. This deals with prompts that instruct an agent on how to handle the more broad ethical and long-term components of its responses.

The **Independent** module focuses more on an agent's personality and individual memories which influence more nuanced aspects of its responses and reactions to its environment and conversations. In the ACE framework, that's represented by the `Agent Model Layer` and the `Executive Function Layer`.

And the **Focus** module is for handling very specific task, like dealing with APIs or sending messages to specific people or something like that. That's encapsulated by the `Cognitive Control Layer` and `Task Prosecution Layer` in the ACE framework.

**Example:** The `Focus` module executes a task based on the instructions and guidance it receives from the `Independent` module, which is influenced by the agent's persona as well as the ethical and aspirational imperatives provided by the `Global` module.

## Memory

**Short-Term Data** is cached data that is regularly reviewed, filtered and flushed. Intended for immediate use and current conversational context.

**Long-Term Data** is data that is stored in a persistent database for later reflection and recollection when appropriate. Intended for information that is unlikely to change very often and likely to be referenced with some regularity.

**Reflective Data** is intended to be a sort of "journal" for agents to review and reflect on stored data to contextualize and understand it in the context of their individual experience. This allows for more nuanced understanding of events and concepts over a period of time.

**Example:** In an exchange on a platform like Discord, the ACE agent would have the immediate conversation context saved as `Short-Term Data`, and if parts of the conversation are considered relevant for later use, it will be saved as `Long-Term Data`. After some criteria is met, the agent will review and reflect on the both forms of data it has collected, write a summary to be saved as `Reflective Data`, and decide if any of that information needs to be altered or removed.

## Network

The **Gateway** submodule manages general interactions with external processes and services, as well as orchestrating the `Clients` and `Connections` in the `Network` module..

**Connection** is a `Gateway` class that refers to connections, requests, and queues in the `Network` module.

**Client** is a `Gateway` class that refers to client-specific interactions, details and processes in the `Network` module.

**Example:** To communicate with the ACE agent through a platform like Discord, you would need the `Gateway` submodule to initialize a `LanguageClient` to generate responses and a `CommunicatonClient` to provide proper authentication, with the `HttpConnection` properly set to handle requests and errors as needed.

# Programming Stack

- Programming Language(s): Python
- API Framework: Flask
- Configuration: ConfigMaps
- Container Management: Podman, Kind, Kubernetes
- Container Orchestration: Helm Charts
- Database Management: PostgreSQL
- Logging: Prometheus, Grafana
- Security: OAuth, Secrets
- Task Management: Apache Kafka, WebSockets

# ACE Framework Breakdown
1. **Aspirational Layer (Layer 1):** Translate the ethical framework into a set of Python classes and methods that process incoming information from the northbound bus to make value-aligned decisions. This might involve NLP tasks to interpret moral dilemmas or general mission goals.

2. **Global Strategy Layer (Layer 2):** Build the agents' world model using data from sensors, API, and other sources. This layer will convert broader goals into strategic objectives that are more grounded in the current environmental context.

3. **Agent Model Layer (Layer 3):** Combine real-time telemetry data with the agent's static configuration and past experiences to form a self-aware model, including the agent's capabilities and strategic objectives. This layer refines strategies within the context of self-knowledge.

4. **Executive Function Layer (Layer 4):** Here we develop resource and risk management systems, and we take the refined strategies to create executable plans that are adapted to practical constraints like resource availability and environmental risks.

5. **Cognitive Control Layer (Layer 5):** This layer involves implementing systems for task switching and selection, determining the most pertinent tasks to focus on at any given time based on overall strategies and real-time environmental conditions.

6. **Task Prosecution Layer (Layer 6):** We will define the mechanics of task execution, including initializing tasks, performing actions, monitoring progress, and detecting completion. This will include interfaces for the agent's actuators and feedback systems.

# Communication Buses
**Natural Language Prompts and Responses:** We could utilize the structure we've been building to drive the language model with specific prompts corresponding to each layer. The outputs could then guide decision-making.

**Layer Interaction:** Define clear interfaces between layers, where each layer only communicates with its immediate neighbors (north or south), abiding by the ACE Framework's principles.

**Iterative Development:** Start with foundational functions for each layer and continually build up complexity. Leveraging the prompts and processing strategies from the ACE_Framework.md, we can ensure that development aligns with the ACE principles.

**Telemetry and Decision-Making:** Use the telemetry from the Northbound Bus to inform decisions at various layers, and send commands and strategies down through the Southbound Bus.

## Data Flow
1. The ACE receives sensory data and reports from the Northbound Bus.
2. The Aspirational Layer makes ethical judgments based on this data.
3. Decisions are sent to the Global Strategy Layer to align with environmental context.
4. The Agent Model Layer personalizes strategies, acknowledging self-capabilities.
5. The Executive Function Layer turns strategies into executable plans.
6. The Cognitive Control Layer decides on the most pertinent tasks.
7. The Task Execution Layer carries out the actions, reports successes/failures, and asks for new tasks.