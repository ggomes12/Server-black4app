FROM python:3.9-slim

WORKDIR .

COPY . .

EXPOSE 8080

CMD ["python", "server.py"]
