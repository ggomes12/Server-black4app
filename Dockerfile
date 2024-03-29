# image
FROM python:3.10.12

WORKDIR /app

COPY . . 

RUN pip install socket

CMD ["python", "app/TCPServer.py"]
