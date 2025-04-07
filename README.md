# Profiles REST API

This is a REST API project for managing user profiles.

## Features

- User authentication and authorization
- Create, update, and delete user profiles
- View user profile details
- Token-based authentication

## Technologies Used

- Python
- Django
- Django REST Framework
- PostgreSQL

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/profiles-rest-api.git
   ```
2. Navigate to the project directory:
   ```bash
   cd profiles-rest-api
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Apply migrations:
   ```bash
   python manage.py migrate
   ```
6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

- Access the API at `http://127.0.0.1:8000/`
- Use tools like Postman or cURL to interact with the endpoints.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
