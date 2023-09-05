FROM python:3.10-slim-bullseye

WORKDIR /usr/src

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY app /usr/src/app

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "app:server", "--workers", "2" ]