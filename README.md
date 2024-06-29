# Roflan ToDo App

A simple and efficient ToDo application built with Flask, SQLAlchemy, and Marshmallow. This app allows users to create, view, and delete tasks, providing a clean and responsive user interface.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Key Files Description](key-files-description)
- [API Endpoints](#api-endpoints)
- [License](#license)

## Features

- Create new tasks with a title and description.
- View all tasks in a list.
- Delete tasks from the list.
- Responsive UI with real-time updates.
- Error handling and validation using Marshmallow.
- Integrated with SQLAlchemy for database operations.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework.
- **SQLAlchemy**: SQL toolkit and Object-Relational Mapping (ORM) library.
- **Marshmallow**: An ORM/ODM/framework-agnostic library for object serialization/deserialization and validation.
- **HTML/CSS/JavaScript**: Frontend technologies for the user interface.
- **Bootstrap**: A CSS framework for building responsive web designs.

## Getting Started

### Prerequisites

- Python 3.11+
- PostgreSQL (or any other preferred SQL database)

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/vladimirblanven/roflantodoapp.git
    cd roflantodoapp
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the database:**

    Create database and the user with privileges in preferred SQL database. Update the `DATABASE_URL` in `config.py` with your database credentials (PostgreSQL for e.g.):

    ```python
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/databasename'
    ```

5. **Initialize the database and create table:**

    ```python
    from app import create_app, db
    from app.models import TodoModel
    app = create_app()
    with app.app_context():
        db.create_all()
    ```

### Running the Application

1. **Start the Flask development server:**

    ```bash
    python runner.py
    ```

2. **Open your browser and navigate to:**

    ```
    http://127.0.0.1:8000
    ```

## Project Structure

```plaintext
roflantodoapp/
├── app/
│   ├── __init__.py
│   ├── extensions.py
│   ├── models.py
│   ├── utils.py
│   ├── views.py
│   ├── static/
│   │   ├── styles.css
│   │   ├── scripts.js
│   │   ├── favicon.ico
│   │   └── robots.txt
│   └── templates/
│       └── index.html
├── tests/
├── config.py
├── runner.py
├── pyproject.toml
├── requirements.txt
├── README.md
└── LICENSE.md
```

## Key Files Description

### `/roflantodoapp/app/__init__.py`
This file initializes the Flask application, configures the app, and registers the main blueprint.

### `/roflantodoapp/app/extensions.py`
This file initializes and configures the extensions used in the application, such as SQLAlchemy for database interactions.

### `/roflantodoapp/app/models.py`
Defines the database models. In this project, it includes the `Todo` model representing a to-do item.

### `/roflantodoapp/app/utils.py`
Contains utility functions used in the application. For example, it includes a function to get the first available ID for a new to-do item.

### `/roflantodoapp/app/views.py`
Defines the routes and views for the application. It includes routes for creating, retrieving, and deleting to-do items.

### `/roflantodoapp/app/static/styles.css`
Contains the CSS styles for the application's frontend.

### `/roflantodoapp/app/static/scripts.js`
Includes JavaScript code for handling frontend interactions, such as submitting new to-do items and displaying the current date and time.

### `/roflantodoapp/app/templates/index.html`
The main HTML template for the application's frontend. It includes the structure and elements for displaying and managing to-do items.

### `/roflantodoapp/config.py`
Defines the configuration settings for the Flask application, including database URI and debug mode.

### `/roflantodoapp/runner.py`
The entry point for running the Flask application. It creates an app instance and runs the server.

### `/roflantodoapp/pyproject.toml`
Poetry configuration file for the Python project, including metadata and dependencies.

### `/roflantodoapp/requirements.txt`
Lists the Python packages required for the project.

## API Endpoints 

### Get All ToDos

- **URL:** `/todos`
- **Method:** `GET`
- **Description:** Retrieve a list of all todos.
- **Response:**
  ```json
  [
      {
          "id": 1,
          "title": "Sample ToDo",
          "description": "This is a sample todo",
          "created_at": "2024-06-28T12:00:00"
      }
  ]

### Create a New ToDo
- **URL:** `/todos`
- **Method:** `POST`
- **Description:** Create a new todo.
- **Request Body**
  ```json
  [
      {
          "title": "New ToDo",
          "description": "Description of the new todo"
      }
  ]
- **Response:**
  ```json
  [
      {
         "id": 1,
         "title": "Sample ToDo",
         "description": "This is a sample todo",
         "created_at": "2024-06-28T12:00:00"
      }
  ]

### Get a Specific ToDo 
- **URL:** `/todos/<int:todo_id>`
- **Method:** `GET`
- **Description:** Retrieve a specific todo by ID.
- **Response:**
  ```json
  [
      {
         "id": 1,
         "title": "Sample ToDo",
         "description": "This is a sample todo",
         "created_at": "2024-06-28T12:00:00"
      }
  ]

### Delete a ToDo
- **URL:** `/todos/<int:todo_id>`
- **Method:** DELETE
- **Description:** Delete a specific todo by ID.
- **Response:**
  ```json
  [
      {
         "id": 1,
         "title": "Sample ToDo",
         "description": "This is a sample todo",
         "created_at": "2024-06-28T12:00:00"
      }
  ]

### License
This project is licensed under the MIT License - see the `LICENSE.md` file for details.