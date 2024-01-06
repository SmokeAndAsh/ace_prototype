# Lite Directory

```
ace-lite-prototype/
├── docs/ <-- documentation
├── ace-lite-app/ <-- Helm Chart files
├── kb/ <-- Kubernetes files
├── config/ <-- configuration files
│   ├── development/
│   ├── production/
│   └── testing/
├── src/ <-- source code
│   ├── app/
│   ├── models/
│   └── services/
├── db/ <-- database files
│   ├── migrations/
│   └── seeds/
├── scripts/ <-- utility scripts
├── logs/ <-- log files
└── tests/ <-- test scripts
    ├── integration/
    └── unit/
```

- **/src:** Contains all source code, divided into subdirectories for different parts of the system, such as APIs, services, or data models.
- **/config:** Contains configuration files. Subdirectories might be used to separate different environments like development or production.
- **/db:** Holds database-related files, including migrations and seed data.
- **/logs:** Dedicated space for log files, possibly further divided by date or component.
- **/tests:** Contains all test scripts, potentially organized into unit and integration tests.
- **/docs:** For project documentation, including setup guides and API references.
- **/scripts:** Utility scripts for tasks like database migration, setup, or deployment.

# Lite Programming Stack
- Programming Language(s): Python
- API Framework: Flask
- Configuration: ConfigMaps
- Container Management: Podman, Kind, Kubernetes
- Container Orchestration: Helm Charts
- Database Management: PostgreSQL
- Logging: Prometheus, Grafana
- Security: Keycloak, OAuth, Secrets
- Task Management: Apache Kafka, WebSockets

# Lite Python Packages
- Authlib
- Flask
- Flask-SQLAlchemy
- prometheus_flask_exporter
- psycopg2
- requests
- SQLAlchemy