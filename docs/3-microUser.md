# microUser
The MicroUser service manages user-related data and authentication for both passengers and drivers in the platform. It handles user registration, profile management, authentication, and provides user details to other services.

## API Endpoints

### Create a User

```http
  POST /users/
```

| Header          | Body            | Type     | Description                        |
|--------------- |--------------- |-------- |---------------------------------- |
| `api_key`      |               | `string` | **Required**. Your API key        |
|               | `first_name`     | `string` | **Required**                       |
|               | `last_name`     | `string` | **Required**                       |
|               | `email`        | `string` | **Required**                       |
|               | `password`     | `string` | **Required**                       |
|               | `role`  | `string` | **Required**                       |
|               | `phone_number`  | `string` | **Required**                       |



#### Responses
 **Success - User Created**
 `HTTP 201 Created`
```
{
  "user_id": "12345678_abcd",
  "message": "User created successfully"
}
```
**Conflict - User Already Exists**
`HTTP 409 Conflict`
```
{
  "detail": "User with this email already exists. Please provide a unique email address"
}
```

**Bad Request**
`HTTP 400 Bad Request`
```
{
  "detail": "Invalid request data. Required fields are missing or invalid"
}
```

**Unauthorized - Missing API key, missing/invalid/expired token**
`HTTP 401 Unauthorized`
```
{
  "detail": "Access denied due to invalid subscription key"
}
{
  "detail": "ExpiredSignatureError: Signature has expired"
}
{
  "detail": "Not authenticated"
}
{
  "detail": "Not authorized"
}
```
**Internal Server Error - Unexpected issue**
`HTTP 500 Internal Server Error`
```
{
  "error": "Something went wrong. Please try again later."
}
```

### Get User Details

```http
  GET /users/{user_id}
```

| Header          |Parameter |  Body            | Type     |       
|---------------  | | ---------------  |-------- |---------------------------------- |
| `api_key`       | |                  | `string` | 
| `Bearer token`  | |                  | `string` | 
|                 |`user_id` |   | `string` | 


#### Responses
 **Success - Trip status updated successfully**
 `HTTP 200 OK`
```
{
  "trip_id": "12345678_abcd",
  "status": "started",
}
```
**400 Bad Request – Invalid status update**
 `HTTP 400 Bad Request`
```
{
  "error": "Invalid status transition from 'completed' to 'started'."
}
```
**Unauthorized - Missing API key, missing/invalid/expired token**
`HTTP 401 Unauthorized`
```
{
  "detail": "Access denied due to invalid subscription key"
}
{
  "detail": "ExpiredSignatureError: Signature has expired"
}
{
  "detail": "Not authenticated"
}
{
  "detail": "Not authorized"
}
```
**403 Forbidden – User is not allowed to update the trip status**
 `HTTP 403 Forbidden`
```
{
  "error": "Forbidden. Only the assigned driver or passenger can update the trip status."
}
``` 

**404 Not Found – Trip ID does not exist**
 `HTTP 404 Not Found`
```
{
  "error": "Trip with ID 'abc123' not found."
}
``` 
**Internal Server Error - Unexpected issue**
`HTTP 500 Internal Server Error`
```
{
  "error": "Something went wrong. Please try again later."
}
```

### Update user data

```http
  PATCH /users/{user_id}
```

| Header          |Parameter |  Body            | Type     |       
|---------------  | | ---------------  |-------- |---------------------------------- |
| `api_key`       | |                  | `string` | 
| `Bearer token`  | |                  | `string` | 
|                 |`trip_id` |   | `string` | 

#### Responses
 **Success - Trip details successfully retrieved.**
 `HTTP 200 OK`
```
{ "trip_id": "abc123", 
"passenger_id": "12345",
 "driver_id": "67890",
  "car_id": "c9876", 
  "start_location": { "latitude": 40.7128, "longitude": -74.0060 }, 
  "end_location": { "latitude": 34.0522, "longitude": -118.2437 }, 
  "status": "completed", 
  "receipt": 45.50, 
  "start_time": "2025-03-29T10:00:00Z", 
  "end_time": "2025-03-29T10:45:00Z", 
  "estimated_duration": 2700, 
  "actual_duration": 2700 
  }
```

**404 Not Found – Trip ID does not exist**
 `HTTP 404 Not Found`
```
{
  "error": "Trip with ID 'abc123' not found."
}
``` 
**Unauthorized - Missing API key, missing/invalid/expired token**
`HTTP 401 Unauthorized`
```
{
  "detail": "Access denied due to invalid subscription key"
}
{
  "detail": "ExpiredSignatureError: Signature has expired"
}
{
  "detail": "Not authorized"
}
```
**Internal Server Error - Unexpected issue**
`HTTP 500 Internal Server Error`
```
{
  "error": "Something went wrong. Please try again later."
}
```
### Set driver availability
```http
  PATCH /users/{driver_id}/{car_id}/availability
```

| Header          |Parameter |  Body            | Type     |       
|---------------  | | ---------------  |-------- |---------------------------------- |
| `api_key`       | |                  | `string` | 
| `Bearer token`  | |                  | `string` | 
|                 |`trip_id` |   | `string` | 

#### Responses
 **Success - Trip details successfully retrieved.**
 `HTTP 200 OK`
```
{ "trip_id": "abc123", 
"passenger_id": "12345",
 "driver_id": "67890",
  "car_id": "c9876", 
  "start_location": { "latitude": 40.7128, "longitude": -74.0060 }, 
  "end_location": { "latitude": 34.0522, "longitude": -118.2437 }, 
  "status": "completed", 
  "receipt": 45.50, 
  "start_time": "2025-03-29T10:00:00Z", 
  "end_time": "2025-03-29T10:45:00Z", 
  "estimated_duration": 2700, 
  "actual_duration": 2700 
  }
```

**404 Not Found – Trip ID does not exist**
 `HTTP 404 Not Found`
```
{
  "error": "Trip with ID 'abc123' not found."
}
``` 
**Unauthorized - Missing API key, missing/invalid/expired token**
`HTTP 401 Unauthorized`
```
{
  "detail": "Access denied due to invalid subscription key"
}
{
  "detail": "ExpiredSignatureError: Signature has expired"
}
{
  "detail": "Not authorized"
}
```
**Internal Server Error - Unexpected issue**
`HTTP 500 Internal Server Error`
```
{
  "error": "Something went wrong. Please try again later."
}
```


## Workflow - Happy path
Observation: every 3-5 seconds the location of the driver gets update through the Dispatch service.
1. Passenger requests available trips → `GET /dispatch/trips`
- The Dispatch service finds available drivers based on location & availability.
- Returns a list of potential trips (drivers, estimated prices, ETA, etc.).
2. Passenger selects a trip → `POST /trips/`
- The microTrip service creates a new trip entry with status "pending".
- Sends an event to Notification service to notify the driver.
3. Driver receives trip request & accepts → `PATCH /trips/{trip_id}` with `{ "status": "assigned" }`
- The microTrip service updates the trip status.
- Notifies the passenger through the Notification service and Dispatch service that the trip has been assigned.

4. Driver picks up the passenger and starts the trip → `PATCH /trips/{trip_id}` with `{ "status": "started" }`
- The microTrip service updates the status.
- Telemetry data id collected by the Dispatch service (location updates, speed, etc.).

5. Trip completes → `PATCH /trips/{trip_id}` with `{ "status": "completed" }`
- The microTrip service records the trip end time.
- Sends data to Payment service for price calculation.
- Publishes an event to Analytics Processing for data tracking.

6. Payment service calculates price → POST `/billing/trip/{trip_id}`
- Payment service calculates price.
- Notification Service notifies the passenger about the trip cost.

7. Passenger gets receipt → GET `/billing/trip/{trip_id}/receipt` 
- Passenger retrieves invoice & trip summary.
- Notification Service can send an email/SMS with the receipt.