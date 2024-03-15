# Access spaCy with custom APIs. Includes SQLite DB Backend

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


### Flask server

To run:

```bash
$ python app_flask.py
```

To access the website point your browser at [http://127.0.0.1:5000](http://127.0.0.1:5000). In `app_flask.py` there are two ways to implement the server, one with a single resource `'/'` and one with two resources: `/get` and `/post`.

Enter text input, and receive both entity and dependency information.
Dependencies associated with Entities are stored in the database. You may also view this.
