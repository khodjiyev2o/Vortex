# syntax=docker/dockerfile:1
FROM  --platform=linux/amd64 python:3.8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY ./requirements.txt ./
RUN pip install -r requirements.txt
RUN apt update 
RUN apt install vim -y
RUN apt install awscli -y 


COPY ./ .
RUN python manage.py makemigrations
RUN python manage.py migrate



CMD ["python","manage.py","runserver","0.0.0.0:8000"]