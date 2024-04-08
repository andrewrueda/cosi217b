"""Simple Web interface to spaCy entity recognition

To see the pages point your browser at http://127.0.0.1:5000.

"""


from flask import Flask, request, render_template

import ner
import dep

app = Flask(__name__)


# For the website we use the regular Flask functionality and serve up HTML pages.

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html', input=open('input.txt').read())
    else:
        text = request.form['text']

        ner_doc = ner.NERSpacyDocument(text)
        dep_doc = dep.DEPSpacyDocument(text)

        ner_markup_paragraphed = get_markup_paragraphed(ner_doc.get_entities_with_markup())
        dep_markup_paragraphed = get_markup_paragraphed(dep_doc.get_dependencies_with_markup())

        return render_template('result.html', ner_markup=ner_markup_paragraphed, dep_markup=dep_markup_paragraphed)


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

    ner_doc = ner.NERSpacyDocument(text)
    dep_doc = dep.DEPSpacyDocument(text)

    ner_markup_paragraphed = get_markup_paragraphed(ner_doc.get_entities_with_markup())
    dep_markup_paragraphed = get_markup_paragraphed(dep_doc.get_dependencies_with_markup())

    return render_template('result2.html', ner_markup=ner_markup_paragraphed, dep_markup=dep_markup_paragraphed)


if __name__ == '__main__':
    app.run(debug=True)
