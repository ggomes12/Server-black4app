FROM python:3.9-slim

WORKDIR /app

COPY app/server.py /app/

EXPOSE 80

CMD ["python", "server.py"]

