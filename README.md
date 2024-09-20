# E-Commerce Backend with Flask

This is a Flask-based backend for an e-commerce platform. It provides APIs for user management, product handling, order processing, and authentication. The application uses SQLAlchemy for ORM, JWT for authentication, and is designed to be scalable, secure, and easy to maintain.

## Features

- **User Authentication**: Register, login, password reset, and JWT-based authentication.
- **Product Management**: APIs for adding, updating, deleting, and viewing products.
- **Order Processing**: Handling of user orders, payment processing, and order history.
- **Database Integration**: SQLAlchemy ORM with Flask-Migrate for database migrations.
- **Email Support**: Flask-Mail for sending emails (order confirmation, password reset, etc.).
- **Security**: Password hashing with Flask-Bcrypt and secure token-based authentication using JWT.

## Getting Started

### Prerequisites

Ensure you have the following installed:
- Python 3.8+
- pip (Python package manager)
- A SQL database (e.g., PostgreSQL, MySQL, or SQLite for development)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/ecommerce-backend.git
    cd ecommerce-backend
    ```

2. Create and activate a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:
    - Create a `.env` file in the root directory to store sensitive configuration variables.
    - Example `.env` file:

      ```bash
      FLASK_APP=app.py
      FLASK_ENV=development
      SECRET_KEY=your_secret_key
      JWT_SECRET_KEY=your_jwt_secret_key
      SQLALCHEMY_DATABASE_URI=sqlite:///ecommerce.db
      MAIL_SERVER=smtp.example.com
      MAIL_PORT=587
      MAIL_USE_TLS=True
      MAIL_USERNAME=your_email@example.com
      MAIL_PASSWORD=your_email_password
      ```

5. Initialize the database:

    ```bash
    flask db init
    flask db migrate
    flask db upgrade
    ```

6. Run the development server:

    ```bash
    flask run
    ```

The backend will be running on `http://127.0.0.1:5000/`.

### Project Structure

```
.
├── app/
│   ├── __init__.py        # Initializes Flask app and extensions
│   ├── models.py          # Database models
│   ├── routes.py          # API routes for user, products, orders, etc.
│   ├── auth.py            # JWT Authentication and authorization
│   └── utils.py           # Utility functions (e.g., password hashing)
├── migrations/            # Flask-Migrate database migration files
├── requirements.txt       # Python package dependencies
├── config.py              # Application configuration
├── app.py                 # Entry point for the application
└── README.md              # This README file
```

### API Endpoints

| Method | Endpoint                  | Description                            |
|--------|---------------------------|----------------------------------------|
| POST   | `/api/auth/register`       | Register a new user                   |
| POST   | `/api/auth/login`          | User login                            |
| POST   | `/api/auth/reset-password` | Request a password reset              |
| GET    | `/api/products`            | List all products                     |
| POST   | `/api/products`            | Add a new product (Admin)             |
| PUT    | `/api/products/<id>`       | Update a product (Admin)              |
| DELETE | `/api/products/<id>`       | Delete a product (Admin)              |
| POST   | `/api/orders`              | Create a new order                    |
| GET    | `/api/orders/<id>`         | View an order's details               |


### Deployment

For production, use a WSGI server like Gunicorn:

```bash
gunicorn -w 4 app:app
```

You can deploy the application on platforms like Heroku, AWS, or DigitalOcean. Make sure to configure your environment variables and update your database settings for production.

### Contributing

If you'd like to contribute to this project, please fork the repository, create a new branch, and submit a pull request.

