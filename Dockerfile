FROM python:3.12.7-alpine

ENV PYTHONUNBUFFERED 1
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ADD .env.docker /app/.env

CMD sleep 10; python manage.py makemigrations; python manage.py migrate; python manage.py collectstatic --no-input; \
gunicorn rishat_assignment.wsgi:application --bind 0.0.0.0:8000 --workers 4
