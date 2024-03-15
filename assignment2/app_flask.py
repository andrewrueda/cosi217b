"""Simple Web interface to spaCy entity recognition, with SQLite backend.

To see the pages point your browser at http://127.0.0.1:5000.

"""

from flask import Flask, request, render_template
from flask_table import Table, Col
from markupsafe import Markup
from flask_sqlalchemy import SQLAlchemy
import os

import ner

app = Flask(__name__)

path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'database')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + path + '/flask_ner.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entity = db.Column(db.String)
    head = db.Column(db.String)
    dependency = db.Column(db.String)
    child = db.Column(db.String)

    def __init__(self, entity, dependency):
        self.entity = entity['text']
        self.head = dependency['head']
        self.dependency = dependency['dependency']
        self.child = dependency['token']

    def __repr__(self):
        return f"Entity: {self.entity}, Dependency: {self.head} --> {self.child}, {self.dependency}"

    def to_dict(self):
        return {'id': self.id, 'entity': self.entity, 'head': self.head,
                'dependency': self.dependency, 'child': self.child}


class DataTable(Table):
    id = Col('id')
    entity = Col('entity')
    head = Col('head')
    dependency = Col('dependency')
    child = Col('child')


if not os.path.exists('database'):
    os.makedirs('database')


try:
    with app.app_context():
        if not os.path.exists('database/flask_ner.db'):
            db.create_all()
            print("Database created successfully.")
        else:
            db.init_app(app)
            print("Initialized successfully.")
except Exception as e:
    print(f"Error accessing database: {e}")


# For the website we use the regular Flask functionality and serve up HTML pages.

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html', input=open('input.txt').read())
    else:
        text = request.form['text']

        doc = ner.SpacyDocument(text)
        data = entity_dependency_data(doc.get_entities(), doc.get_dependencies())

        with app.app_context():
            for entry in data:
                db.session.add(entry)
                db.session.commit()

        ner_markup_paragraphed = get_markup_paragraphed(doc.get_entities_with_markup())
        dep_markup_paragraphed = get_markup_paragraphed(doc.get_dependencies_with_markup())

        return render_template('result.html', ner_markup=ner_markup_paragraphed, dep_markup=dep_markup_paragraphed)


@app.route('/data', methods=['GET'])
def get_data():
    query = db.session.execute(db.select(Entry))
    items = [item[0].to_dict() for item in query]
    return render_template('database.html', data=items)


def entity_dependency_data(entities, dependencies):
    data = []
    for dependency in dependencies:
        for entity in entities:
            if entity['start_char'] <= dependency['head_index'] <= entity['end_char']:
                data.append(Entry(entity, dependency))
    return data


def get_markup_paragraphed(markup):
    markup_paragraphed = ''
    for line in markup.split('\n'):
        if line.strip() == '':
            markup_paragraphed += '<p/>\n'
        else:
            markup_paragraphed += line
    return markup_paragraphed


# alternative where we use two resources


@app.get('/get')
def index_get():
    return render_template('form2.html', input=open('input.txt').read())


@app.post('/post')
def index_post():
    text = request.form['text']

    doc = ner.SpacyDocument(text)
    data = entity_dependency_data(doc.get_entities(), doc.get_dependencies())

    with app.app_context():
        for entry in data:
            db.session.add(entry)
            db.session.commit()

    ner_markup_paragraphed = get_markup_paragraphed(doc.get_entities_with_markup())
    dep_markup_paragraphed = get_markup_paragraphed(doc.get_dependencies_with_markup())

    return render_template('result.html', ner_markup=ner_markup_paragraphed, dep_markup=dep_markup_paragraphed)


if __name__ == '__main__':
    app.run(debug=True)
