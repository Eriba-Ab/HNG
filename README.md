# HNG Django Project

This repository contains a Django project. The instructions below are tailored for Windows PowerShell (PowerShell v5.1). They show how to set up a virtual environment, install dependencies, run migrations, create a superuser, run the development server, and run tests.

## Requirements

- Python 3.10+ (3.8+ may work but 3.10+ recommended)
- pip (bundled with Python)
- Git (optional)

This project uses a local SQLite database (`db.sqlite3`) by default and includes `manage.py` and `requirements.txt` at the repository root.

## Quick setup (PowerShell)

Open PowerShell in the project root (where `manage.py` is). Then run the commands below.

1. Create and activate a virtual environment

```powershell
python -m venv venv
# If you get an execution policy error when activating, run this first to allow activation for this session:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force
# Activate the virtualenv in PowerShell
.\venv\Scripts\Activate.ps1
```

(Alternative for cmd.exe)

```cmd
venv\Scripts\activate
```

2. Upgrade pip and install dependencies

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

3. Apply database migrations

```powershell
python manage.py migrate
```

4. (Optional) Create a superuser for the admin interface

```powershell
python manage.py createsuperuser
```

5. Run the development server

```powershell
# Bind to 127.0.0.1:8000 (default)
python manage.py runserver
# OR bind to all interfaces for testing on network:
python manage.py runserver 0.0.0.0:8000
```

6. Run the test suite

```powershell
python manage.py test
```

## Environment variables and secrets

This repo may expect certain environment variables in production (for example: `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`, or an external `DATABASE_URL`). For local development with the included `db.sqlite3` you typically don't need to set anything.

If you want to keep secrets out of source control, create a `.env` file and load it from `settings.py` (for example, using `python-dotenv` or `django-environ`). Example `.env` content:

```
SECRET_KEY=replace_with_a_secure_value
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

Note: If you add `python-dotenv` or `django-environ`, add it to `requirements.txt` and load the `.env` in `settings.py`.

## Procfile / Deployment notes

A `Procfile` is included for Heroku-like deployments. Example `Procfile` entry for production using Gunicorn:

```
web: gunicorn profile_api.wsgi:application --log-file -
```

- Install `gunicorn` (and any production dependencies) if you intend to deploy to Heroku or a similar service.
- Heroku runs on Linux; the Windows-specific steps above are for local development only.

## Troubleshooting

- "Activate.ps1 cannot be loaded because running scripts is disabled on this system": run

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force
.\venv\Scripts\Activate.ps1
```

- If `python` points to Python 2.x, use `python3` or provide the full path to the Python 3 executable.
- If `pip install -r requirements.txt` fails, inspect the failing package and consult its build dependencies (Windows may require build tools for some packages).

## Useful commands (copy-paste)

```powershell
# Create venv, activate, install deps, migrate, create superuser, runserver
python -m venv venv; Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force; .\venv\Scripts\Activate.ps1; python -m pip install --upgrade pip; pip install -r requirements.txt; python manage.py migrate; python manage.py createsuperuser; python manage.py runserver

# Run tests
python -m venv venv; .\venv\Scripts\Activate.ps1; pip install -r requirements.txt; python manage.py test
```

## Contributing

If you want to contribute, fork the repo, create a feature branch, make changes, add tests, and open a pull request. Ensure tests pass locally before submitting.

## License

Add license information here if applicable.

---

If you'd like, I can also:
- add a `.env.example` file,
- add a dev `requirements-dev.txt` or a `Makefile`/PowerShell script for common tasks,
- or validate the current `requirements.txt` and run the test suite.

