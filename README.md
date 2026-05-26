# Job Portal Website

A Django-based Job Portal website where employers can post jobs and job seekers can apply online.

## Features

- Employer Registration & Login
- Job Seeker Registration & Login
- Add/Edit/Delete Jobs
- Apply for Jobs
- Applicant Management
- Search Jobs
- Contact Page
- Custom 404 Page
- Resume Upload
- Status Update for Applicants

## Technologies Used

- Python
- Django
- HTML
- CSS
- Bootstrap
- SQLite

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/jobportal.git
```

### Go to Project Folder

```bash
cd jobportal
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Migrations

```bash
python manage.py migrate
```

### Start Server

```bash
python manage.py runserver
```

## Admin Panel

Create superuser:

```bash
python manage.py createsuperuser
```

Admin URL:

```bash
http://127.0.0.1:8000/admin
```

## Project Structure

- jobapp/
- templates/
- static/
- media/
- manage.py

## Future Improvements

- Email Verification
- Job Recommendations
- Resume Parsing
- Chat System
- Payment Integration

## Author

PARMESHWAR PAWAR