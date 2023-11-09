# ACE Prototype Overview
A very in-process prototype for an Autonomous Cognitive Entity based on David Shapiro's [ACE Framework](https://github.com/daveshap/ACE_Framework/blob/main/ACE_Framework.md).

```
Agent <-- The Autonomous Cognitive Entity
└── Core <-- where the `src` folder would be
      ├── Cognition <-- High-level cognitive processes for the agent
      │         ├── Global <-- Global cognitive module
      │         ├── Independent <-- Independent cognitive module
      │         └── Focus <-- Focus cognitive module
      ├── Memory <-- Handles short and long term data management
      │         ├── Short Term Data <-- Cached, refreshed frequently
      │         ├── Long Term Data <-- Vectorized(?), reviewed periodically
      │         └── Reflective Data <-- NLP Interpreted, like a "journal"
      └── Networking <-- Handles APIs and Northbound/Southbound buses
                  ├── Gateway (Input/Output) <-- Handles API-related functionalities
                  ├── Northbound Bus <-- Telemetry
                  └── Southbound Bus <-- Control
```

# Current Project Goals

- Set up agent persona (Cognition)
- Get communication flow between agent and CLI (Networking)
- Create simple memory system (Memory)

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