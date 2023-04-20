FROM python:3.9-slim

workdir /app

COPY . .

ENTRYPOINT ["python"]