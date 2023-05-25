FROM python:3.9-alpine

RUN pip3 install --no-cache-dir flask

COPY app.py /app/app.py

# je m'attends à ce qu'il y ait un volume monté dans
# /data cette ligne ne fait rien, elle avertit juste
# (meta données)
VOLUME /data

EXPOSE 5000

CMD LOGDIR=/data python /app/app.py
