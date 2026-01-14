FROM python:3.7
COPY ./app
WORKDIR /app
RUN pip install -r requirement.txt
EXPOSE $PORT
CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app

# the --bind we have written above is crucial, as it binds the port with the IP address