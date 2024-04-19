FROM python:3.7-alpine3.8
RUN apk update
RUN pip install --upgrade pip

WORKDIR /app
ENV PYTHONPATH = "${PYTHONPATH}:/app/"

COPY . .