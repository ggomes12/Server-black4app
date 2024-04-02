FROM python:3.9-slim

WORKDIR /Server-black4app

COPY . . 

EXPOSE 8080
ENV PORT 8080

CMD ["python", "./server.py"]
