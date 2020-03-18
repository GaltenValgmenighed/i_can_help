FROM tiangolo/meinheld-gunicorn-flask:python3.7

COPY ./gunicorn_conf.py /app/gunicorn_conf.py
COPY ./main.py /app/main.py

COPY ./templates/index.html /app/templates/index.html
COPY ./templates/tak.html /app/templates/tak.html

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
