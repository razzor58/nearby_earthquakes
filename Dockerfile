FROM python:3.11-slim-bullseye

WORKDIR /usr/local/src

COPY requirements.txt /usr/local/src

RUN pip install -r requirements.txt

COPY . /usr/local/src

CMD ['python', 'main.py']