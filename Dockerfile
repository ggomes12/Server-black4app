FROM python:3.9-slim

WORKDIR /app

COPY app/server.py /app/

EXPOSE 8080

CMD ["python", "app/server.py"]
