FROM python:3.9-slim

WORKDIR /app

COPY server.py /app

RUN pip install Flask

ENV FLASK_APP=server.py


EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
