
# Understanding Business Problem
  
Software is built to solve real problems so it needs to be designed and molded around them.

## Functional Requirements

### User Management
- The platform must allow passengers and drivers to create and manage accounts.
- Users must be able to login and authenticate using a token-based system (e.g., JWT).
- Role-based access control (RBAC) must be implemented for different user roles (passenger, driver, admin).
- Drivers should be able to manage their availability and update their profile (e.g., car details).

### Trip Management
- Passengers must be able to request a ride.
- Drivers must be able to accept ride requests and update the trip status (e.g., assigned, started, completed, canceled).
- Trip details, including pickup location, destination, trip status, and price calculation, should be recorded and stored.
- The platform should generate receipts after a trip is completed and send them to the Payment Service aka microPayment.

## Non-Functional Requirements

### Scalability
- The platform should be designed to scale horizontally, handling increased traffic as the number of users and trips grows.
- Kafka should support high throughput and handle millions of events per second as the platform scales.
- Databricks should scale its processing capabilities based on data volume and complexity of tasks (e.g., batch processing, real-time processing).

### Performance
- Real-time event processing should be completed with minimal latency to ensure fast updates to trip statuses and user information.
- The system should support low-latency communication between microservices, particularly for critical updates like trip status and driver availability.
- The system should be optimized for high query performance when accessing data.

### Availability and Reliability

- The system must have a high availability architecture, ensuring minimal downtime.