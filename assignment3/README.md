# Use SpaCy NER with FastAPI, Flask, and Streamlit using Docker

The code requires Python version 3.9 or higher.

### Setup
1. Install Docker:

```
https://docs.docker.com/get-docker/
```
   
### Compose and Run

To run:

```bash
$ docker-compose up
```

The web apps will point to these addresses:

# FastAPI:
```
http://127.0.0.1:8000
```

Accessing the API:

```bash
$ curl http:/127.0.0.1:8000

$ curl  http:/127.0.0.1:8000/ner -H 'Content-Type: application/json' -d@input.json

$ curl  http:/127.0.0.1:8000/dep -H 'Content-Type: application/json' -d@input.json
```

Make it Pretty:

```bash
$ curl http:/127.0.0.1:8000?pretty=true

$ curl  http:/127.0.0.1:8000/ner?pretty=true -H 'Content-Type: application/json' -d@input.json

$ curl  http:/127.0.0.1:8000/dep?pretty=true -H 'Content-Type: application/json' -d@input.json
```

# Flask:
```
http://127.0.0.1:5000
```

# Streamlit:
```
http://127.0.0.1:8501
```
