# You_Track_API
## Endpoints

```javascript
POST /users - create a new user
DELETE /user/me delete user
POST /auth
{
    "username": "danijax",
    "password": "password"
}
PUT /user/me - update user account
GET /user/me - get user account information

POST /locations jwttoken
{
    "mcc": 310,
    "mnc": 410,
    "cells": [{
        "lac": 7033,
        "cid": 17811
    }]
}

GET /locations jwttoken
{
    "lat": 39.56763197,
    "lon": -105.00727917

}
```

