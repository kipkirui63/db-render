# db-render
Flask RESTful API Project
Description
This is a Flask RESTful API project for user registration, login, and user management, with authentication using JSON Web Tokens (JWT).

Table of Contents
Setup
Prerequisites
Installation
Usage
Endpoints
Configuration
License
Setup
Prerequisites
Python 3.x
Virtual environment (recommended for isolating dependencies)
PostgreSQL database
Installation
Clone the repository:

bash
Copy code
git clone https://https://github.com/kipkirui63/db-render
Navigate to the project directory:

bash
Copy code
cd your-api-project
Create and activate a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install project dependencies:

bash
Copy code
pip install -r requirements.txt
Set up your PostgreSQL database and update the database URI in app.py to point to your database.

Run the application:

bash
Copy code
python app.py
The Flask application should now be running, and you can access the API endpoints.

Usage
You can use this API to register new users, log in, and manage user information.
Endpoints
Register User:

Endpoint: /register
Method: POST
Request Body: JSON containing username, email, and password
Registers a new user and returns an access token.
Login User:

Endpoint: /login
Method: POST
Request Body: JSON containing username and password
Logs in a user and returns an access token.
Get User Information:

Endpoint: /user/<int:user_id>
Method: GET
Requires a valid access token.
Returns user information for the specified user_id.
Update User Information:

Endpoint: /user/<int:user_id>
Method: PUT
Requires a valid access token.
Update user information (username, email, phone number).
Delete User:

Endpoint: /user/<int:user_id>
Method: DELETE
Requires a valid access token.
Delete a user account.
Configuration
In app.py, you can configure the JWT_SECRET_KEY and the database URI.
License
This project is licensed under the MIT License - see the LICENSE file for details.

