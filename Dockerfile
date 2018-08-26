FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN pip install psycopg2

COPY ./app /app