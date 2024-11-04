## Objective: 
Build a basic REST API to manage employees in a company, focusing on CRUD operations, RESTful principles, and authentication.

## Features
- Create, list, retrieve, update, and delete employee records.
- Filtering by department and role.
- Pagination for employee listing.
- Token-based authentication for secure access.
- Proper error handling with HTTP status codes.
  
## Summary
This Employee Management API effectively implements CRUD operations while adhering to RESTful practices. It provides robust error handling and authentication, ensuring secure and efficient management of employee records. Postman simplifies testing by allowing users to easily validate each endpoint and scenario.

## Prerequisites
Before running the application, ensure you have the following installed:
- **Python** (3.7 or higher)
- **pip** (Python package manager)
- **Postman** or similar tool for testing API endpoints
- **Database** (e.g., PostgreSQL, MySQL, or SQLite)
  
## Technologies Used
- **Django Rest Framework**: Web framework for building the API.
- **PostgreSQL**: For storing and retrieveing the data.
- **Postman**: For Testing of API Endpoints.

## Installation
1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/employee-management-api.git
   cd employee-management-api
2. Create a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
4. Install the required dependencies:
   pip install -r requirements.txt

5. Set up the database (follow instructions in DATABASE.md if available).
   
7. Run the application:
   python manage.py runserver


