
# Async vs Sync
  
In the tech stack documentation we mentioned that one of the reasons we decided to go with FastAPI was because supports async implemenations. The application must be able to give fast responses while handling thousands and thousands of requests per second.

This with a sync approach would be harder to achieve because while a task is being finished the entire application might be idle until the task is completed. Even though synchronous executions are faster the risk of slowing the application is not worth.

Using async would allow us to handle many tasks concurrently without blocking any other activities of the application. This approach is much harder than syncrhonous applications because many more exceptions and errors can happen that need to be handled that may lead in data being lost.

  
## Decision

We have decided to go with the async approach in order to be able to scale our service to thousands of requests per second without compromising the speed of the response.

This decision has an impact on how the code is going to look like and how the data interaction with the database is going to be.

As we mentioned in the tech stack documentation, we decided to use PostgreSQL as our database. 
As PostgreSQL is an open source project and by default does not have an async driver we will have to use one made from the community **asyncpg**

Docs: https://github.com/MagicStack/asyncpg

