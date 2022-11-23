
from subprocess import run
run("gunicorn -k geventwebsocket.gunicorn.workers.GeventWebSocketWorker -w 1 -b 0.0.0.0:8000 main:app --reload".split(' '))