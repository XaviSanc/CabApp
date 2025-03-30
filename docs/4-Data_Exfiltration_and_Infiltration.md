
# Data Exfiltration and Infiltration

To ensure the security of the data we collect and protect our platform from unauthorized access, we have implemented multiple layers of security measures:


## OAuth and Token-Based Authentication

We use OAuth for authentication and issue JWT tokens to validate user sessions securely.

Tokens are signed and include claims that allow services to authenticate users without exposing sensitive credentials.

## Token Validation Endpoint

A dedicated endpoint verifies token validity, expiration, and integrity before allowing access to resources.
All of our API endpoints rely on this endpoint to verify the validity of the token being provided.

## Role-Based Access Control (RBAC)

Our database schema is structured to enforce RBAC, restricting access based on user roles (e.g., driver, passenger, admin).

This prevents unauthorized users from querying or modifying data they shouldn’t have access to.

## Private Network for Services

All microservices, databases and cloud tools (Databricks) are sitting within the private company network
All microservices communicate within a private network, ensuring that internal APIs and databases are not exposed to the public internet.

## API Gateway
Our APIs are only accessible from the public network through our gateway, which adds an extra layer of security by requiring a unique API key for each microservice, with the option to assign specific keys to certain endpoints. Additionally, we can implement rate limiting based on IP to prevent attackers from overwhelming our servers with excessive requests.

## Web Application Firewall (WAF)

We will be using Cloudfare as our web app firewall. This component is integrated to protect against common web threats such as SQL injection, cross-site scripting (XSS), and other OWASP Top 10 vulnerabilities.

## Kafka Secure Communication
Our Kafka system will be using SSL certificate to validate the communications.

## Logging & Monitoring with Elasticsearch & Kibana
We log all server activity to Elasticsearch, allowing for real-time monitoring and anomaly detection. In case an anomaly is detected an alert will be triggered through Kibana to notify the team about a potential security breach.

## Infrastructure-Level Security
All resources are deployed within a secure cloud environment with strict IAM policies, ensuring that only authorized users can access or perform specific actions on designated resources.