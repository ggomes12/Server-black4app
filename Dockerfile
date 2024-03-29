FROM python:3.9-slim

COPY app/server.py /app/

WORKDIR /app


EXPOSE 80

CMD ["python", "server.py"]

