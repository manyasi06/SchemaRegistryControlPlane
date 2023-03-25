# syntax=docker/dockerfile:1.4

FROM python:3.10.7-alpine AS builder
EXPOSE 8000
WORKDIR /opt/app
COPY requirements.txt /opt/app
RUN apk update && apk add postgresql gcc postgresql-client libc-dev libpq-dev

RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app 
ENTRYPOINT ["python3"] 
CMD ["manage.py", "runserver", "0.0.0.0:8000"]

FROM builder as dev-envs
RUN apk update && apk add git htop vim jq


RUN addgroup -S docker && adduser -S --shell /bin/bash --ingroup docker vscode

# install Docker tools (cli, buildx, compose)
COPY --from=gloursdocker/docker / /
CMD ["manage.py", "runserver", "0.0.0.0:8000"]