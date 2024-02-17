# Access spaCy with custom APIs

The code requires Python version 3.9 or higher.

### Setup
1. Install requirements:

```bash
$ pip install -r requirements.txt
```


2. Download spaCy ```en_core_web_sm```:

```bash
$ python -m spacy download en_core_web_sm
```

### FastAPI

To run:

```bash
$ uvicorn app_fastapi:app --reload
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


### Flask server

To run:

```bash
$ python app_flask.py
```

To access the website point your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000). In `app_flask.py` there are two ways to implement the server, one with a single resource `'/'` and one with two resources: `/get` and `/post`.

Enter text input, and receive both entity and dependency information.

### Streamlit

To run:

```bash
$ streamlit run app_streamlit.py
```
This should take you to http://localhost:8501.

Select entity view to display entity information and word frequency.

Select dependency view to display a graph dependency structure of the input, as well as a count of dependencies for each head.
