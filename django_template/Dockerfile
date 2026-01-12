# Dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy project
COPY . .

# Collect static files
#RUN python manage.py collectstatic --noinput

EXPOSE 8000

# Run with Gunicorn
#CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]

# Use entrypoint script to start container
ENTRYPOINT ["/app/entrypoint.sh"]
