FROM tiangolo/meinheld-gunicorn-flask:python3.7

COPY ./main.py /app/main.py
COPY ./gunicorn_conf.py /app/gunicorn_conf.py

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
