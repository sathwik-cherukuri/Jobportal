# Job Portal Web Application

## Overview
A web-based job portal developed using Python and Django. The application is designed to help job seekers explore job listings and apply for opportunities.

## Features
- User registration and login
- Job listings with details such as title, company, location, and salary
- Job seeker information and profile management, where implemented
- Job application functionality
- Django models, views, and templates
- Static files for frontend styling

## Technologies Used
- Python
- Django
- HTML
- CSS
- Database configured for the project
- Git and GitHub

## Project Structure
- `config/` — project configuration
- `jobs/` — job portal application code
- `resumes/` — resume-related files or uploads
- `static/css/` — CSS files
- `staticfiles/` — collected static files, if used for deployment
- `templates/` — HTML templates
- `manage.py` — Django management utility
- `requirements.txt` — Python dependencies
- `build.sh` — build script

## Getting Started

### 1. Clone the repository
```bash
git clone YOUR_REPOSITORY_URL
cd YOUR_PROJECT_FOLDER
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply migrations
```bash
python manage.py migrate
```

### 5. Start the development server
```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Learning Outcomes
- Building a web application with Django
- Working with models, views, and templates
- Implementing user registration and login flows
- Managing job listings and application data
- Understanding database-backed web development

## Author
Sathwik Cherukuri
