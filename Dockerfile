FROM python:3

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /it-software

COPY requirements.txt /it-software/

RUN pip3 install -r requirements.txt

COPY . /it-software/