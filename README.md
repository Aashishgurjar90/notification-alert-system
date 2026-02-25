# Multi-Tenant Notification & Alert System

A Django REST Framework based backend system for managing alerts with secure JWT authentication and multi-tenant architecture.

## Features

- JWT Authentication
- Multi-Tenant Architecture
- Role-based Access Control
- Alert Management API
- Alert Status Workflow (Open → In Progress → Closed)
- Tenant-based Data Isolation
- Dashboard Statistics API
- Severity Filtering
- Secure REST APIs

## Tech Stack

- Python 3.12
- Django
- Django REST Framework
- SQLite
- JWT Authentication
- Git & GitHub

## Project Structure

notification-alert-system/
│
├── alert_system/
├── alerts/
├── accounts/
├── manage.py
├── .gitignore
└── README.md

## Installation

1. Clone repository

git clone https://github.com/Aashishgurjar90/notification-alert-system.git

2. Create virtual environment

python -m venv venv

3. Activate environment

venv\Scripts\activate

4. Install dependencies

pip install django djangorestframework djangorestframework-simplejwt

5. Run migrations

python manage.py migrate

6. Run server

python manage.py runserver

## API Endpoints

Authentication

POST /api/token/

Alerts

GET /api/alerts/
POST /api/alerts/
GET /api/alerts/{id}/
PATCH /api/alerts/{id}/update_status/

Dashboard

GET /api/dashboard/

## Author

Aashish Gurjar