
# Project Title

A brief description of what this project does and who it's for


# Tech Stack

For this application we have decided to use Python 3.12.9 and FastAPI as its framework.


## Why Python?

We have decided to use Python because it's easy to set up and code, and it provides a wide range of powerful external libraries supported by a strong and active community.

## Why FastAPI?

We are aware that there are more options that are more used than FastAPI like Django and Flask. But I prefer FastAPI because 2 main reasons.


- Is built on top of Pydantic and Starlette which makes it very fast due to its asynchronous implementation. This lead to a much better performance for API with lots of concurrent requests.
- FastAPI provides automatic API documentation which makes easier for testing and debugging.

## Package manager

For our package manager we have decided to use PIP as it is very easy to use and most widely used and supported.

## Databases

For our main database we have decided to use **PostgreSQL** and using **asyncpg** to do connection pooling asynchronously with the database (see more details in Async_vs_Sync.md).

We will have 1 server and 4 databases, one for the microTrip, one for microUser, one for microPayment, one for microDispatch. The best case scenario would be to have 4 servers with a database each so if one database goes down, the rest of the application keeps working while a replica is being created. But to simplify the exercise we will have only 1 server.

The tables in all of the databases will be divided into two schemas, DRIVER and PASSENGER. This division will help separating the concerns and data access models related to the different types of user, preventing mixing up the data.

It also enables us to more effectively define the RBAC for the users interacting with the services, enhancing the security and protection of our data.

For microNotification we will be using **Firebase Cloud Messaging** to be pushing the notifications into our users phones. The notifications will be also being ingested by our Analytics Processing service in our data processing cloud tool, in this case we have decided that it will be Databricks, that will be also subscribed .

For our logging system, we will utilize **Elasticsearch** to store all servers logs from our micros, enabling us to monitor potential bugs and trigger alerts using **Kibana**.
