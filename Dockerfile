# image
FROM python:3

WORKDIR /app

COPY . .

EXPOSE 80


CMD ["python", "app/TCPServer.py"]
