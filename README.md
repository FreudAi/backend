# API zahageek 

## base url
https://zahageek-back.onrender.com/

## Endpoint

### login /api/auth/login
#### Query
```json
{
    "email": "youremai@domain.com",
    "password": "yourpassword"
}
```
#### Response
```json
{
    "id": 1,
    "email": "youremai@domain.com",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6InlvdXJlbWFpQGRvbWFpbi5jb20iLCJleHAiOjE3MTkwNDgzOTd9.QYbq8REZYtYVFP1DjKFe9A08df8RrX0opzMJnV2tjI8"
}
```

### sign up /api/auth/register
#### Query
```json
{
    "firt_name": "First Name",
    "last_name": "Last Name",
    "email": "youremai@domain.com",
    "password": "yourpassword"
}
```
#### Response
```json
{
    "id": 1,
    "first_name": "",
    "last_name": "Last Name",
    "email": "youremai@domain.com",
    "profile_picture": "/images/Profile_avatar_placeholder_large.png"
}
```
