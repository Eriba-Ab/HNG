# Production Dockerfile for the Django project
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libpq-dev netcat \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python deps
COPY Stage0/base/requirements.txt /app/requirements.txt
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /app/requirements.txt

# Copy project files
COPY . /app

# Switch to the Django project directory where manage.py lives
WORKDIR /app/Stage0/base

# Create static/media dirs and run collectstatic during build (best-effort)
RUN mkdir -p /vol/web/static /vol/web/media \
    && python manage.py collectstatic --noinput || true

# Create a non-root user and switch to it
RUN adduser --disabled-password --gecos "" appuser || true
RUN chown -R appuser:appuser /app
USER appuser

EXPOSE 8000

# Gunicorn process
CMD ["gunicorn", "profile_api.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
