# Diary Application

A simple diary application built with Django that allows users to create, view, and manage diary entries. This application features a clean and aesthetic user interface with dark theme support, making it visually appealing.

## Features

- Create new diary entries with headings and content.
- View a list of all diary entries, sorted by date.
- Individual diary entry details with timestamp.
- User-friendly 404 error page for invalid URLs.
- Dark theme for a modern aesthetic.

## Technologies Used

- **Django**: A high-level Python web framework.
- **HTML/CSS**: For structuring and styling the web pages.
- **Tailwind CSS**: A utility-first CSS framework for rapid UI development.
- **SQLite**: Default database for development (can be changed based on deployment requirements).

## Folder Structure
```bash
diary_app/
├── diary/                           # Django app containing diary-related functionalities
│   ├── migrations/                  # Database migrations for the diary app
│   ├── __init__.py                  # Python package marker
│   ├── admin.py                     # Admin panel configurations
│   ├── apps.py                      # App configuration
│   ├── models.py                    # Database models
│   ├── tests.py                     # Unit tests for the app
│   ├── views.py                     # View functions for handling requests
│   ├── urls.py                      # URL routing for the diary app
│   └── templates/                   # HTML templates for the app
│
├── diaryApplication/                # Project settings and configuration
│   ├── __init__.py                  # Python package marker
│   ├── asgi.py                      # ASGI configuration
│   ├── settings.py                  # Project settings
│   ├── urls.py                      # Project-wide URL routing
│   └── wsgi.py                      # WSGI configuration                       
└── manage.py                             # Command-line utility for interacting with the project
```
## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/bhargav-yarlagadda /Diary_app_django.git
   cd diaryApplication
   ```
2. **Apply migrations**
   ```bash
    python manage.py migrate
    ```
3. run the server
  ```bash
  py manage.py runserver
  ```
