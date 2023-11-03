# syntax=docker/dockerfile:1

FROM python:3.12-slim-bookworm


WORKDIR /src

COPY ../src/requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY ../src /src

ENV FLASK_APP=server.py
ENV FLASK_HOST=0.0.0.0

CMD ["python", "./server.py"]
