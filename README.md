# <p align='center'> Customer Relation Management System</p>

<details>

<summary>Table of Contents</summary>

- [Description](#description)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Live On PythonAnywhere](#live-on-pythonanywhere)
- [Project Strucutre](#project-structure)
- [Setup](#setup)
- [API Endpoints](#api-endpoints)
- [Screenshots](#screenshots)

</details>

## Description
A minimal CRM built with Django that lets you manage clients/customers from a simple, clean dashboard. It supports authentication, CRUD for clients, category linkage, and a search experience across multiple fields.

## Features

- User registration, login, logout
- Dashboard listing all clients
- Client detail page + update form
- Client categories (ForeignKey)
- Search clients by name or ID
- Server-side form rendering with crispy-forms (Bootstrap 4)

## Tech Stack

- Python 3.10+, Django 5.x
- Django REST Framework
- djangorestframework-simplejwt
- django-crispy-forms + crispy-bootstrap4
- SQLite (default; easily swappable)

## Live on PythonAnywhere
Interact with the live demo:

`link:` [CRM System](https://abdulrahmanks.pythonanywhere.com/)

    Note: the demo runs on a free tier, so initial load can be slow (cold start).

## Project Structure
```bash
CRM-System/
├─ CRM/                  # Project package (settings, urls, wsgi)
├─ web/                  # App: views, models, forms, templates
├─ templates/            # Base and shared templates
├─ manage.py
└─ requirements.txt
```

## Setup

1. Clone & enter the project

    ```bash
    git clone https://github.com/Abdulrahman-K-S/CRM-System.git
    cd CRM-System
    ```

2. Create & activate a virtual environment
    ```bash
    python -m venv venv
    venv/Scripts/activate
    ```

3. Install dependencies (found in [requirments.txt](requirments.txt))
    ```bash
    pip install -r requirments.txt
    ```

4. Run the dev server
    ```bash
    cd CRM/
    python manage.py runserver
    ```

## API Endpoints

## Screenshots
