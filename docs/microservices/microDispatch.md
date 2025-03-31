# microDispatch
MicroDispatch is a core microservice in our taxi platform responsible for managing the dispatching of trips to drivers. It serves as the intermediary between passengers and drivers, handling requests for ride assignments, driver availability, and trip statuses. The service is integrated with other microservices like MicroTrip, MicroUser, and MicroNotification, enabling seamless trip management, user interactions, and real-time notifications.
## API Endpoints

### Get trip options for a Passenger
```http
  GET /dispatch/passenger/{passenger_id}/available-trips
```
| Header          |Parameter |  Body            | Type     |       
|---------------  | | ---------------  |-------- |---------------------------------- |
| `api_key`       | |                  | `string` | 
| `Bearer token` |               | `string` | **Required**. Your Bearer token   |
|                 |`passenger_id` |   | `string` | 


#### Responses
 **Success - List of available trips for the passenger.**
 `HTTP 200 OK`
```
{
"available_trips": [
    {
      "trip_id": "uuid_of_trip1",
      "pickup_location": "location_1",
      "destination_location": "location_2",
      "estimated_price": 12.50,
      "driver_id": "uuid_of_driver1"
    },
    {
      "trip_id": "uuid_of_trip2",
      "pickup_location": "location_3",
      "destination_location": "location_4",
      "estimated_price": 15.00,
      "driver_id": "uuid_of_driver2"
    }
  ]
}
```
**404 Not Found – Not avaailable trips found**
 `HTTP 404 Not Found`
```
{
  "error": "No available trips found."
}
```

### Request ride from passenger to driver
```http
   POST /dispatch/passenger/{passenger_id}/ride/{driver_id}
```
| Header          |Parameter |  Body            | Type     |       
|---------------  | | ---------------  |-------- |---------------------------------- |
| `api_key`       | |                  | `string` | 
| `Bearer token` |               | `string` | **Required**. Your Bearer token   |
|                 |`passenger_id` |   | `string` | 
|                 |`driver_id` |   | `string` | 
|                 | |  `trip_id` | `string` | 


#### Responses
 **Success - List of available trips for the passenger.**
 `HTTP 200 OK`
```
{
  "trip_id": "uuid_of_trip",
  "status": "pending",
  "driver_id": "uuid_of_driver",
  "pickup_location": "location_1",
  "destination_location": "location_2",
  "estimated_price": 12.50
}

```
**400 Bad Request – Invalid or missing parameters**
 `HTTP 404 Bad Request`
```
{
  "error": "Invalid trip ID or driver ID."
}
```
**404 Not Found – Requested trip no longer available**
 `HTTP 404 Not Found`
```
{
  "error": "Trip not available."
}
```

### Driver accept ride
```http
   POST /dispatch/driver/{driver_id}/ride/accept
```
| Header          | Body            | Type     | Description                        |
|--------------- |--------------- |-------- |---------------------------------- |
| `api_key`      |               | `string` | **Required**. Your API key        |
|    `token`           |      | `string` | **Required** Bearer                      |
|               | `trip_id`     | `string` | **Required**        |
|               | `passenger_id`     | `string` | **Required**        |

#### Responses
 **Success - Tripp successfully accepted.**
 `HTTP 200 OK`
```
{
  "trip_id": "uuid_of_trip",
  "driver_id": "uuid_of_driver",
  "passenger_id": "uuid_of_passenger",
  "status": "accepted",
  "pickup_location": "location_1",
  "destination_location": "location_2",
  "estimated_price": 12.50
}

```
**400 Bad Request – Invalid or missing parameters** `HTTP 404 Bad Request`

```
{
  "error": "Invalid trip ID or driver ID."
}
```

**404 Not Found – Requested trip no longer available** `HTTP 200 OK`
```

{
  "error": "Trip not available or already accepted."
}
```


### Driver declines ride
```http
   POST /dispatch/driver/{driver_id}/ride/decline
```
| Header          | Body            | Type     | Description                        |
|--------------- |--------------- |-------- |---------------------------------- |
| `api_key`      |               | `string` | **Required**. Your API key        |
|    `token`           |      | `string` | **Required** Bearer                      |
|               | `trip_id`     | `string` | **Required**        |
|               | `passenger_id`     | `string` | **Required**        |
|               | `reason`     | `string` | **Required**        |

#### Responses
 **Success - Tripp successfully declined.**
 `HTTP 200 OK`
```
{
  "trip_id": "uuid_of_trip",
  "driver_id": "uuid_of_driver",
  "passenger_id": "uuid_of_passenger",
  "status": "declined",
  "reason": "reason_for_decline"
}

```
**400 Bad Request – Invalid or missing parameters** `HTTP 404 Bad Request`

```
{
  "error": "Invalid trip ID or driver ID."
}
```

**404 Not Found – Requested trip no longer available** `HTTP 200 OK`
```

{
  "error": "Trip not found"
}
```



### Drivers receiving new requests
The drivers will be receiving rides requests from the passengers through a notification triggered by `POST /dispatch/passenger/{passenger_id}/ride/{driver_id}`. 