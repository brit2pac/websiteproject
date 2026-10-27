# IT Task Manager

A simple task management web application built with Django. It was created to make it easier to organize tasks, keep track of deadlines, and manage work within a team.

## About the project

The application allows users to manage tasks in one place. Each task can have a description, deadline, priority, type, and assigned workers.

I built this project as part of my Python and Django learning journey, focusing on working with models, views, templates, authentication, and CRUD operations.

## What you can do

- View and search for tasks
- Filter tasks by available criteria
- Create, edit, and delete tasks
- Set task priorities and deadlines
- Assign tasks to team members
- Mark tasks as completed or reopen them
- Manage tasks and workers through Django Admin

## Built with

- Python
- Django
- SQLite
- Bootstrap 5
- HTML

## Getting started

Clone the repository:

```bash
git clone https://github.com/brit2pac/websiteproject.git
cd websiteproject
```

Create a virtual environment and activate it:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python manage.py migrate
```

Create an admin account:

```bash
python manage.py createsuperuser
```

Run the development server:

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Admin panel

To manage tasks, workers, positions, and task types, open `http://127.0.0.1:8000/admin/` and log in with your superuser account.

## A note

This project is a learning project, so there is still room to improve and add new features.
