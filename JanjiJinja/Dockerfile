FROM python:3.7.2-stretch

COPY . /app

WORKDIR /app

RUN pip install Flask==2.0.2

USER www-data

CMD [ "python", "/app/ssti.py" ]