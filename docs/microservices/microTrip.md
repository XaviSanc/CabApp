# microTrip
The microTrip service is responsible for managing the lifecycle of trips in the taxi platform. It provides CRUD operations for trips and generates receipts upon trip completion. It interacts with the Dispatch service (which assigns taxis and provides telemetry data), the Payment service (for receipt calculation), and the Analytics Processing (for data insights).

## API Endpoints

### Create a trip
  Only drivers would be allowed to create the trips. This validation would be done by the JWT token that would only allow drivers to attack this API.
```http
  POST /api/trip
```

| Header          | Body            | Type     | Description                        |
|--------------- |--------------- |-------- |---------------------------------- |
| `api_key`      |               | `string` | **Required**. Your API key        |
| `Bearer token` |               | `string` | **Required**. Your Bearer token   |
|               | `passenger_id`  | `string` | **Required**                       |
|               | `driver_id`     | `string` | **Required**                       |
|               | `car_id`        | `string` | **Required**                       |
|               | `start_location` | `float`  | **Required** (Latitude, Longitude) |
|               | `end_location`  | `float`  | **Required** (Latitude, Longitude) |

- **Extra data**: ETA_prediction, car, fuel_consumption_prediction...

#### Responses
 **Success - Trip Created**
 `HTTP 201 Created`
```
{
  "trip_id": "12345678_abcd",
  "status": "pending",
  "message": "Trip created successfully for {passenger_id} with {driver_id} on {car_id}"
}
```
**Bad Request - Missing Required Fields**
`HTTP 400 Bad Request`
```
{
  "detail": "Missing required fields: passenger_id, driver_id, start_location, end_location"
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

### Update trip status

```http
  PATCH /trips/{trip_id}
```

| Header          |Parameter |  Body            | Type     |       
|---------------  | | ---------------  |-------- |---------------------------------- |
| `api_key`       | |                  | `string` | 
| `Bearer token`  | |                  | `string` | 
|                 |`trip_id` |   | `string` | 
|                 | |     `status`  | `string` | 


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

### Update trip status

```http
  GET /trips/{trip_id}
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