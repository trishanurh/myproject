FROM python:3.8.5
ENV PYTHONUNBUFFERED 5
RUN mkdir /app
# masuk container
COPY requirements.txt /app/




RUN pip install -r requirements.txt
RUN pip install gunicorn
RUN pip install urllib3
RUN pip install django-sslify

RUN apt update

COPY . /app/