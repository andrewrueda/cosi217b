# Access spaCy with custom APIs

The code assumes Python version 3.8 or higher.


### FastAPI

To run:

```bash
$ uvicorn app_fastapi:app --reload
```

Accessing the API:

```bash
$ curl http:/127.0.0.1:8000

$ curl  http:/127.0.0.1:8000/ner -H 'accept: application/json' \
       -d@input.json

$ curl  http:/127.0.0.1:8000/dep -H 'accept: application/json' \
       -d@input.json
```

Make it Pretty:

```bash
$ curl http:/127.0.0.1:8000?pretty=true

$ curl  http:/127.0.0.1:8000/ner?pretty=true -H 'accept: application/json' \
       -d@input.json

$ curl  http:/127.0.0.1:8000/dep?pretty=true -H 'accept: application/json' \
       -d@input.json
```


### Flask server

To run:

```bash
$ python app_flask.py
```

To access the website point your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000). In `app_flask.py` there are two ways to implement the server, one with a single resource `'/'` and one with two resources: `/get` and `/post`. This is to illustrate how the HTML form accesses the resource.


### Streamlit

To run:

```bash
$ streamlit run app_streamlit.py
```
