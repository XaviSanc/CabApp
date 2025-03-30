# microUser
The microUser service manages user-related data and authentication for both passengers and drivers in the platform. It handles user registration, profile management, authentication, and provides user details to other services.

## API Endpoints
### Drivers Login
```http
  POST /auth/driver/login
```

| Header          | Body            | Type     | Description                        |
|--------------- |--------------- |-------- |---------------------------------- |
| `api_key`      |               | `string` | **Required**. Your API key        |
|               | `email`        | `string` | **Required**                       |
|               | `password`     | `string` | **Required**  Encrypted by the HTTPS in transit                   |



#### Responses
 **Success - Login successfully**
 `HTTP 200 OK`
```
{
  "access_token": "jwt_token",
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

```
**Internal Server Error - Unexpected issue**
`HTTP 500 Internal Server Error`
```
{
  "error": "Something went wrong. Please try again later."
}
```
### Passengers Login
```http
  POST /auth/passenger/login
```

| Header          | Body            | Type     | Description                        |
|--------------- |--------------- |-------- |---------------------------------- |
| `api_key`      |               | `string` | **Required**. Your API key        |
|               | `email`        | `string` | **Required**                       |
|               | `password`     | `string` | **Required**  Encrypted by the HTTPS in transit                   |


#### Responses
 **Success - Login successfully**
 `HTTP 200 OK`
```
{
  "access_token": "jwt_token",
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

```
**Internal Server Error - Unexpected issue**
`HTTP 500 Internal Server Error`
```
{
  "error": "Something went wrong. Please try again later."
}
```
### Validate token
```http
  POST /auth/validate
```

| Header          | Body            | Type     | Description                        |
|--------------- |--------------- |-------- |---------------------------------- |
| `api_key`      |               | `string` | **Required**. Your API key        |
|     `token`        |       | `string` | **Required** Bearer token                       |



#### Responses
 **Success - Login successfully**
 `HTTP 200 OK`
```
{

}
```

**Unauthorized - Missing API key, missing/invalid/expired token**
`HTTP 401 Unauthorized`
```
{
  "detail": "Access denied due to invalid subscription key"
}
{
  "detail": "Token has expired"
}
{
  "detail": "Invalid token"
}

```
**Internal Server Error - Unexpected issue**
`HTTP 500 Internal Server Error`
```
{
  "error": "Something went wrong. Please try again later."
}
```

### Create a Passenger account

```http
  POST /user/passenger
```

| Header          | Body            | Type     | Description                        |
|--------------- |--------------- |-------- |---------------------------------- |
| `api_key`      |               | `string` | **Required**. Your API key        |
|               | `first_name`     | `string` | **Required**                       |
|               | `last_name`     | `string` | **Required**                       |
|               | `email`        | `string` | **Required**                       |
|               | `password`     | `string` | **Required** Password will be stored encrypted by passlib hash https://passlib.readthedocs.io/en/stable/                      |
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

### Create a Driver account

```http
  POST /user/driver
```

| Header          | Body            | Type     | Description                        |
|--------------- |--------------- |-------- |---------------------------------- |
| `api_key`      |               | `string` | **Required**. Your API key        |
|               | `first_name`     | `string` | **Required**                       |
|               | `last_name`     | `string` | **Required**                       |
|               | `email`        | `string` | **Required**                       |
|               | `password`     | `string` | **Required** Password will be stored encrypted by passlib hash https://passlib.readthedocs.io/en/stable/                         |
|               | `phone_number`  | `string` | **Required**                       |
|               | `Car`  | `Car` | **Required** model, color, license_plate                      |



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
 **Success - User Found - Passenger account**
 `HTTP 200 OK`
```
{
  "user_id": "passenger456",
  "first_name": "Juan",
  "last_name": "Fernandez",
  "email": "juan@example.com",
  "phone_number": "+34666333222",
  "role": "passenger",
  "payment_methods": ["mastercard_ending_5678"],
}
```
**Success - User Found - Driver account**
 `HTTP 200 OK`
```
{
  "user_id": "driver789",
  "first_name": "Sara",
  "last_name": "Benitez",
  "email": "Sara@example.com",
  "phone_number": "+34666333222",
  "role": "driver",
  "driver_info": {
    "availability": "UNAVAILABLE",
    "car_id": "car789",
    "rating": 4.9
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

**404 Not Found – User not found**
 `HTTP 404 Not Found`
```
{
  "error": "User with ID 'driver789' not found."
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
|                 |`user_id` |   | `string` | 

#### Responses
 **Success - User has been updated successfully**
 `HTTP 200 OK`
```
{ 
    "phone_number": "+34777888999",
}
```

**404 Not Found – User not found**
 `HTTP 404 Not Found`
```
{
  "error": "User with ID 'driver789' not found."
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
|                 |`driver_id` |   | `string` | 
|                 |`car_id` |   | `string` | 

#### Responses
 **Success - Driver availability has been updated.**
 `HTTP 200 OK`
```
{ 
    availability: true
  }
```

**404 Not Found – User not found**
 `HTTP 404 Not Found`
```
{
  "error": "User with ID 'driver789' not found."
}
```
**409 Conflict – Driver Already Assigned to a Trip**
 `HTTP 409 Conflict`
```
{
  "error": "Cannot change availability. Driver is currently on an active trip."
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


## Workflow Driver login- Happy path

1. Driver logs in → `GET /auth/driver/login`
- The microUser service checks if user exists.
- If exists hashes the password and compares it to the one stored.
- If credentials are correct sends the JWT to the FE.
- If credentials are correct the JWT is generated incluiding the driver_id and the role of the user, in this case DRIVER
2. When other requests are done to the BE the JWT will be decrypted to use "role" property to attack the DRIVER schema tables by using a specific database user with restricted permissions over the DRIVER schema.
## Workflow Passenger login- Happy path

1. Passsenger logs in → `GET /auth/passenger/login`
- The microUser service checks if user exists.
- If exists hashes the password and compares it to the one stored.
- If credentials are correct the JWT is generated incluiding the passenger_id and the role of the user, in this case PASSENGER
2. When other requests are done to the BE the JWT will be decrypted to use "role" property to attack the PASSENGER schema tables by using a specific database user with restricted permissions over the PASSENGER schema.