FROM python:3.11.3-slim-bullseye

ADD . /root

WORKDIR /root

RUN apt-get update && apt-get install -y libpq-dev gcc netcat

RUN pip install -r requirements.txt

ENTRYPOINT ["./entrypoint.sh"]