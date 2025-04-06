FROM python:3.9-slim-buster

ENV PYTHONBUFFERED=1

WORKDIR /project_dir

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt


EXPOSE 8000 5679
