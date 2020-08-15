# set base image (host OS)
FROM python:3.8

WORKDIR /app
COPY . /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
ENV REDIS_SERVICE=$REDIS_SERVICE
EXPOSE 8000

CMD [ "python", "server/app.py"]