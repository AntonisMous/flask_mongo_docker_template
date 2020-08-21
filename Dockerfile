FROM python:3.7

# Tell Python to not generate .pyc
ENV PYTHONDONTWRITEBYTECODE 1

# Turn off buffering
ENV PYTHONUNBUFFERED 1

ADD . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 5000
