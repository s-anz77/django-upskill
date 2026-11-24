# UpSkill Course Platform

A Django website for browsing online courses and lessons, with user accounts, lesson comments, and free or full subscription plans.

**Live demo:** [my-upskill.up.railway.app](https://my-upskill.up.railway.app/)

## Features

- Browse the course catalogue and course detail pages.
- View lessons associated with a course.
- Register, sign in, update a profile, and request a password reset.
- Post comments on lessons while signed in.
- Access free courses without a subscription.
- Select the Full plan in the user profile to unlock access to premium courses; the code changes the selected plan and does not implement payment processing.
- Lifetime Full access does not expire.
- Manage course and lesson content through Django's admin site.


## Tech stack

- Python 3.15 (as declared in `runtime.txt`)
- Django 6.1
- SQLite
- Pillow for profile image handling
- WhiteNoise and Gunicorn for deployment

## Prerequisites

- Python 3.15
- pip

## Local setup

Run these commands from the repository root. Create and activate a virtual environment:

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Set the required Django secret key before running the application:

Windows PowerShell:

```powershell
$env:DJANGO_SECRET_KEY = "replace-with-a-local-secret"
$env:DJANGO_DEBUG = "true"
```

macOS/Linux:

```bash
export DJANGO_SECRET_KEY="replace-with-a-local-secret"
export DJANGO_DEBUG=true
```

Install dependencies, apply migrations, and start the development server:

```bash
python -m pip install -r requirements.txt
python -m courseswebsite.manage migrate
python -m courseswebsite.manage runserver
```

Open <http://127.0.0.1:8000/>.

## Configuration

- `DJANGO_SECRET_KEY` — required; the application stops during startup when it is missing.
- `DJANGO_DEBUG` — optional; defaults to `false`. Set it to `true` for local development.
- `DJANGO_ALLOWED_HOSTS` — optional comma-separated host list; defaults to `localhost,127.0.0.1`.
- `DJANGO_CSRF_TRUSTED_ORIGINS` — optional comma-separated list of trusted origins.
- `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_HOST_USER`, `EMAIL_HOST_PASSWORD`, `EMAIL_USE_TLS` and `DJANGO_EMAIL_BACKEND` — read into a `MAILERS` settings dictionary in the project configuration.
- `RAILWAY_PUBLIC_DOMAIN` — optional deployment value added to allowed hosts and trusted origins when present.

The local database is SQLite (`db.sqlite3`). Uploaded media is stored in `media/`.

## Project structure

- `courseswebsite/courses/` — course, lesson, and lesson-comment functionality.
- `courseswebsite/users/` — registration, login, profile, and subscription-plan functionality.
- `courseswebsite/courseswebsite/` — Django settings and URL configuration.
- `static/`, `templates/` — site assets and shared templates.
- `courseswebsite/manage.py` — Django management entry point.

