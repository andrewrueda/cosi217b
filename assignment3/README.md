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

### FastAPI:
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

### Flask:
```
http://127.0.0.1:5000
```

To access the website point your browser at http://127.0.0.1:5000. In app_flask.py there are two ways to implement the server, one with a single resource '/' and one with two resources: /get and /post.

Enter text input, and receive both entity and dependency information. Dependencies associated with Entities are stored in the database. You may also view this at /data.

### Streamlit:
```
http://127.0.0.1:8501
```
Select entity view to display entity information and word frequency.

Select dependency view to display a graph dependency structure of the input, as well as a count of dependencies for each head.
