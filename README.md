# IT Task Manager

A Django task manager for IT teams. Team members can create tasks, assign one or more workers, set a priority and deadline, and track completion.

## Features

- Sign in and sign out with Django authentication.
- Create, view, edit, delete, search, filter, and paginate tasks.
- Assign tasks to multiple workers and mark them completed or reopen them.
- Review workers, positions, task types, and each worker's open and completed tasks.
- Manage team members, positions, and task types in Django Admin.
- Responsive pages styled with Bootstrap 5.

## Data model

The database contains `Worker`, `Position`, `TaskType`, and `Task` models. A worker may have one position, and each position may have many workers. Each task has one task type and may be assigned to many workers. See the editable [database structure diagram](docs/database-structure.drawio).

## Requirements

- Python 3.12 or newer
- pip

## Setup

Clone the repository and switch to the implementation branch:

```bash
git clone https://github.com/brit2pac/websiteproject.git
cd websiteproject
git switch develop
```

Create and activate a virtual environment, then install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Create your local environment file from the example and set a private secret key:

```bash
cp .env.example .env
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

Copy the printed value into `SECRET_KEY` in `.env`. The `.env` file and local SQLite database are ignored by Git. For deployment, set `SECRET_KEY`, `DEBUG=False`, and `ALLOWED_HOSTS` in the hosting platform's environment settings.

Create the database and an administrator account:

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open <http://127.0.0.1:8000/>. Sign in with the superuser account, then add workers, positions, and task types at <http://127.0.0.1:8000/admin/> before creating tasks.

## Main pages

- `/` — task list, search, filters, and pagination
- `/tasks/create/` — create a task
- `/workers/` — team directory
- `/positions/` — position directory
- `/task-types/` — task type directory
- `/admin/` — administrative setup

## Project structure

```text
config/       Django project configuration
tasks/        models, forms, views, URLs, and templates
docs/         project documentation and database diagram
```
