# syntax=docker/dockerfile:1

FROM python:3.10

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD python csv_to_bd.py && python csv_to_elastic.py && python run.py
