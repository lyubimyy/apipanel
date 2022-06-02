FROM python:3.8

WORKDIR /apipanel

RUN pip install -r /tmp/requirements.txt
EXPOSE 5000

CMD ["python3"]