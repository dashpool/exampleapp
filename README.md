# Dashpool - Example App

A simple example app

## TEST
```
pip install -r requirements.txt
gunicorn --bind 0.0.0.0:5555 app:server --reload --log-level debug
```



## Build
```
docker build . -t dashpool/exampleapp
```