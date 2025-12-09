# Authentication and Database Construction

## Database Schema
The application uses the default Django `User` model for authentication, extended or related to other models as needed.

### Core Models
- **User**: Handles authentication (username, password, email).
- **Receipt**: (Planned) To store receipt data, linked to User.

## Authentication Flow
The project uses **JWT (JSON Web Tokens)** for secure authentication via `djangorestframework-simplejwt`.

### Endpoints
- `api/token/`: Obtain a pair of access and refresh tokens.
- `api/token/refresh/`: Refresh the access token using the refresh token.

## Configuration
- **Backend**: Django REST Framework with SimpleJWT.
- **Frontend**: Next.js will store the JWT (e.g., in localStorage or cookies) and include it in the `Authorization` header (`Bearer <token>`) for protected requests.

## Database Setup
Currently using **SQLite** for development (`db.sqlite3`).
Production is configured to use **PostgreSQL** via environment variables.
