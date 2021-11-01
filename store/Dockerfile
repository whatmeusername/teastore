FROM python:3.9
ENV PYTHONUNBAFFERED = 1 && PYTHONDONTWRITEBYTECODE = 1
WORKDIR /app/store

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app/store