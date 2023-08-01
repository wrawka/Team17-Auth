FROM python:3.10

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=.

RUN apt-get update && apt-get install -y netcat-openbsd

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY src/ utils tests entrypoint.sh ./

EXPOSE 5000

RUN chmod +x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]
