# Cintasii Education Web Application Backend

Welcome to the backend repository of **Cintasii Education**, a tutor management web application designed to streamline session scheduling, payment processing, and user role management for over 40 active participants. Built with **FastAPI**, this backend integrates key functionalities to empower instructors and students with a seamless education platform.

## Features

- **User Management**: Manage roles (students, tutors, admins) with secure authentication and authorization.
- **Session Scheduling**: Allow tutors and students to manage and track their lessons in real-time.
- **Payment Processing**: Automate and track payment details efficiently.
- **Interactive Education Platform**: Enable instructors to deliver interactive lessons and monitor student progress. (Coming soon)

---

## Project Structure

The backend codebase follows a modular structure for scalability and maintainability:

```plaintext
src/
├── settings.py                # Central configuration for the app
├── accounts/                  # Handles user accounts and authentication
│   ├── database.py            # User-specific database operations
│   ├── models.py              # User data models
│   ├── routes.py              # API endpoints for accounts
│   ├── schemas.py             # Data validation and serialization for accounts
│   ├── users.py               # User service logic
├── api/                       # API routing and initialization
│   ├── api.py                 # Main API router
├── roles/                     # User roles and permissions management
│   ├── models.py              # Role-based models
│   ├── routes.py              # API endpoints for roles
│   ├── schemas.py             # Data validation for role operations
│   ├── service.py             # Business logic for roles
├── logging/                   # Logging configuration
│   ├── log_config.py          # Custom logging setup
│   ├── __init__.py            # Module initializer
├── database/                  # Database setup and migrations
│   ├── core.py                # Database connection and ORM setup
│   ├── manage.py              # Database management utilities
│   ├── migrations/            # Database migrations folder
│       ├── env.py             # Migration environment setup
│       ├── README             # Migration documentation
│       ├── script.py.mako     # Migration templates
│       ├── versions/          # Migration versions
│           ├── c4f6d1767778_add_firstname_lastname_to_user.py
│           ├── cecd2e46742d_roles_tables.py
│           ├── f5d93a9c2a3a_initial_tables.py
```

---

## Key Technologies

- **FastAPI**: High-performance API framework for building scalable and modern web applications.
- **PostgreSQL**: Database for handling relational data.
- **Alembic**: Database migration tool.
- **Pydantic**: For data validation and serialization.
- **Custom Logging**: Robust logging for application monitoring and debugging.

---

## Installation

### Prerequisites

- Python 3.9+
- PostgreSQL 12+
- Virtual Environment (recommended)

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/chiishie/cintasii-backend-main.git
   cd cintasii-backend-main
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows, use venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Environment Variables**:
   Create a `.env` file in the root directory and configure the following:
   ```env
   DATABASE_URL=postgresql://username:password@localhost/cintasii
   SECRET_KEY=your_secret_key
   ```

5. **Apply Migrations**:
   ```bash
   alembic upgrade head
   ```

6. **Run the Application**:
   ```bash
   uvicorn api.api:app --reload
   ```

---

## API Endpoints

### Accounts

- `POST /accounts/login`: User login.
- `POST /accounts/register`: User registration.
- `GET /accounts/me`: Get current user details.

### Roles

- `GET /roles`: List all roles.
- `POST /roles`: Create a new role.

### Sessions and Payments (Coming Soon)

---

## Future Enhancements

- **Integrate Payment Gateway**: Support for automated payment solutions.
- **Admin Dashboard**: Advanced features for administrators to manage the platform.
- **Real-time Notifications**: Alerts for session updates and payments.

---

## Contributions

Contributions are welcome! Feel free to fork the repository and create a pull request with your proposed changes.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For any issues or questions, please contact [Chidubem Ishie](mailto:chidubem.i.ishie@gmail.com).
