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

## High-Level

**Cognition** handles high-level and abstract concepts like personality, task distribution and prioritization, ethical considerations and such. Practically speaking, it would be the final arbiter in how an agent executes a task if there's something causing indecision in the other modules.

**Memory** holds the data from previous interactions, successes, and failures so that the agent can reflect on and recall the appropriate information for responses to external stimulus, like conversations and eventually sensory data and things like that.

**Networking** handles the nitty gritty interactions between internal functions and services, which is gonna make it the most technically focused and program-heavy portion of the whole system. API management, dealing with errors, basically making sure the whole system won't crash if something gets caught up in it.

**Example:** Language models exist in the `Networking` module and are steered by the `Cognition` module, which are influenced by the data it pulls and reflects on from the `Memory` module.

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

## Networking

The **Gateway** handles interactions with inputs and outputs from APIs, such as language models and external services.

The **Northbound Bus** carries internal and external data through the ACE agent. Provides telemetry and useful data to flow through the agent while logging and handling errors and exceptions as they arise.

The **Southbound Bus** carries instructions through the ACE agent.  Provides direction and guidance for processes and functions throughout the system.

**Example:** The `Southbound Bus` directs the appropriate processes in response to the input received from the `Gateway` module and interactions from APIs and so on. If an error occurs or telemetry is meant to be documented, the `Northbound Bus` will track and log this data, and respond to any exceptions as needed.

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