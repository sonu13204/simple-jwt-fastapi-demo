# simple-jwt-fastapi-demo
Demo application to implement JWT with FatsAPI
# FastAPI JWT Authentication Demo

This project demonstrates how to implement **JWT (JSON Web Token)** based authentication in a FastAPI application. It includes access token generation, token verification, token expiration, refresh token handling, and secure endpoints.

---

## **Features**

- User login to generate **JWT access tokens**.
- **Token expiration** implemented for security.
- **Refresh tokens** to extend user sessions.
- Secured endpoints that require valid JWT tokens.
- Password hashing using **bcrypt** for added security.
- Example project using **FastAPI** and **PyJWT** libraries.
- Simple in-memory mock database for demonstration.

---

## **Tech Stack**

- **Python** (>= 3.8)
- **FastAPI** (for building APIs)
- **PyJWT** (for handling JWT tokens)
- **bcrypt** (for password hashing)
- **uvicorn** (for running the server)

---

## **Project Structure**

```bash
.
├── app/
│   ├── main.py          # Entry point for FastAPI app
│   ├── auth.py          # JWT-related logic (access/refresh tokens)
│   ├── models.py        # Pydantic models for request/response
│   ├── database.py      # Mock database for user credentials
│   ├── utils.py         # Utility functions (e.g., password hashing)
│   └── refresh_token.py # Refresh token logic
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## **Setup Instructions**
## **Step 1: Clone the Repository**
```bash
git clone https://github.com/yourusername/fastapi-jwt-demo.git
cd fastapi-jwt-demo
```
## **Step 2: Create a Virtual Environment**
```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
## **Step 3: Install Dependencies**
```
pip install -r requirements.txt
```
## **Step 4: Run the Application**
Start the FastAPI server using Uvicorn:

```
uvicorn app.main:app --reload
```
## **Step 5: Test the Endpoints**
**You can test the API endpoints using Swagger UI or Postman.**
```
Swagger UI: Open your browser and go to http://127.0.0.1:8000/docs.

ReDoc: Alternative API documentation at http://127.0.0.1:8000/redoc.
```

## **API Endpoints**

| **Method** | **Endpoint**          | **Description**                               | **Request Body**                                                                                  |
|------------|-----------------------|-----------------------------------------------|--------------------------------------------------------------------------------------------------|
| POST       | `/login`              | Authenticate user and return access/refresh tokens | `{ "username": "testuser", "password": "testpassword" }`                                        |
| POST       | `/refresh`            | Generate new access token using refresh token   | `{ "refresh_token": "<your_refresh_token>" }`                                                   |
| GET        | `/protected`          | Access secured endpoint (requires valid token)  | **Header**: `Authorization: Bearer <access_token>`                                              |
| GET        | `/health`             | Check the application's health status           | No request body needed                                                                          |



## **How to Use**

**Step 1: Login to Get JWT Access and Refresh Tokens**

Send a POST request to /login with the following JSON body:

```
{
  "username": "testuser",
  "password": "testpassword"
}
```
Response:
```
{
  "access_token": "<your_jwt_access_token>",
  "refresh_token": "<your_refresh_token>",
  "token_type": "bearer"
}
```

**Step 2: Access a Protected Endpoint**

Send a GET request to `/protected` with the Authorization header:
```
Authorization: Bearer <your_jwt_access_token>
```
Response:
```
{
  "message": "Access granted for protected route."
}
```

**Step 3: Refresh Access Token**

When the access token expires, use the refresh token to generate a new access token.

Send a POST request to `/refresh` with the following JSON body:
```
{
  "refresh_token": "<your_refresh_token>"
}
```
Response:
```
{
  "access_token": "<new_access_token>",
  "token_type": "bearer"
}
```



