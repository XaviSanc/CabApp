## Documentation

All the documentation of the decisions taken and the answers of the problem are under the **docs** folder.

## Requirements to run

- Docker

## How to run

If you want to run all the microservices be at the root folder level and if you have *Make* you can just do
```
make run
```
Otherwise:

```
docker-compose up --build
```

If you want to only run **microUser** get under the microUser folder and run
```
docker-compose up --build
```
You will be able to find the microservices under these ports:
- microUser: http://localhost:8000/docs
- microTrip: http://localhost:8001/docs
- microPayment: http://localhost:8002/docs
- microNotification: http://localhost:8004/docs

For testing the Auth endpoint use:
- Username: juan@example.com
- Password: password123

All of the users created have the same password.

## What has been done
- FastAPI app
- Clean architecture
- PostgreSQL
- Async implementation
- Using asyncpg for PostgreSQL and Pooling techniques
- Initialization of all microservices databases and users
- oAuth system with password encrypting
- Makefile
- Logging
