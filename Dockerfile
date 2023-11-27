FROM dashpool/basecontainer:slim

COPY app /usr/src/app

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "app:server", "--workers", "2", "--timeout", "600"  ]