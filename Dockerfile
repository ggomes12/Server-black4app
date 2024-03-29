# image
FROM python:3.10.12

WORKDIR /app

COPY . . 


CMD ["python", "app/TCPServer.py"]
