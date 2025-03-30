
# Vision

Over the next 2-3 years, our focus will be on building a scalable, intelligent, and secure data platform that enhances operational efficiency, improves customer experience, and unlocks new business opportunities. The key pillars of this vision include:
## Advances Data Analytics and AI integration
- Designing our platform with a streaming-first approach to fully leverage real-time data processing and maximize profitability.

- Through our real-time data processing we could leverage dynamic pricing based on demand, demand forecasting for zones during a specific timeframe (airports, stadiums surroundings in a match day) and real-time analytics

## Scalability and performance
- Implement auto-scaling to handle peak demand without affecting the performance
- Optimize database performance by improving query and choosing the right index strategies

## Data Governance

- Implementing a Medallion Architecture in Databricks (https://www.databricks.com/glossary/medallion-architecture) to enhance data organization within the lakehouse, ensuring structured data flow and improving data tracking and monitoring.
- Set up Service Principals to execute the required jobs and assign them appropriate RBAC roles.https://docs.databricks.com/aws/en/admin/users-groups/service-principals

## Cloud-Native & Event-Driven Architecture

- Expand our event-driven architecture using Kafka for seamless microservice integration
- Set up Kubernetes and integrate it with a pod management platform like ArgoCD to monitor and automatically scale resources.

## Security and Law Compliance
- Continuously monitor and enforce compliance with GDPR and other industry regulations.
- Implement Fraud Detection by using Neo4J graph database https://neo4j.com/use-cases/fraud-detection/