# System Directory
Module for the North and Southbound bus system directing telemetry and control data throughout the ACE agent.

```
system/ <-- General system files
├── SYSTEM.md
├── northbound_bus.py <-- Telemetry
├── southbound_bus.py <-- Control
└── logs/ <-- Logs from the bus system
    ├── nb_logging.py <-- Telemetry logs
    ├── sb_logging.py <-- Control logs
    ├── northbound_log.txt
    └── southbound_log.txt
```