FROM tiangolo/uwsgi-nginx-flask:python3.6

RUN pip install psycopg2
RUN pip install pandas

COPY ./app /app