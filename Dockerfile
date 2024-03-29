FROM python:3.9-slim

WORKDIR /

COPY app/server.py /app/

EXPOSE 80

CMD ["python", "/app/server.py"]
