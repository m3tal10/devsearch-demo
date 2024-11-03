FROM python:3.12.2-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app
RUN python manage.py collectstatic --noinput
EXPOSE 8000
