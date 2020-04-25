FROM python:3

RUN apt update
RUN apt upgrade -y

RUN mkdir /code

ADD requirements.txt /code/requirements.txt

RUN pip3 install -r /code/requirements.txt

WORKDIR /code
# Nos paramos en "/code"

CMD [ "python", "app.py" ] 