"""ner.py

Run spaCy NER over an input string and insert XML tags for each entity.

"""

import io
import spacy

nlp = spacy.load("en_core_web_sm")


class SpacyDocument:
    def __init__(self, text: str):
        self.text = text
        self.doc = nlp(text)

    def get_tokens(self) -> list:
        return [token.lemma_ for token in self.doc]

    def get_entities(self) -> str:
        entities = []
        for e in self.doc.ents:
            entities.append((e.start_char, e.end_char, e.label_, e.text))
        return entities

    def get_dependencies(self) -> str:
        dependencies = []
        for token in self.doc:
            dependencies.append({"head": token.head.text, "head_index": token.head.idx,
                                 "dependency": token.dep_, "token": token.text})
        return dependencies

    def get_entities_with_markup(self) -> str:
        entities = self.doc.ents
        starts = {e.start_char: e.label_ for e in entities}
        ends = {e.end_char: True for e in entities}
        buffer = io.StringIO()
        for p, char in enumerate(self.text):
            if p in ends:
                buffer.write('</entity>')
            if p in starts:
                buffer.write('<entity class="%s">' % starts[p])
            buffer.write(char)
        markup = buffer.getvalue()
        return '<markup>%s</markup>' % markup

    def get_dependencies_with_markup(self) -> str:
        output = "<markup>"

        for dep in self.get_dependencies():
            output += f'<span style="color: green;">{dep["head"]}</span> '
            output += f'<span style="color: red;">{dep["dependency"]}</span> → '
            output += f'<span style="color: blue;">{dep["token"]}</span>\n\n'
        output += "</markup>"
        return output


if __name__ == '__main__':

    example = (
        "When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")

    doc = SpacyDocument(example)
    print(doc.get_tokens())

    for entity in doc.get_entities():
        print(entity)
    print(doc.get_entities_with_markup())

    for dependency in doc.get_tokens():
        print(dependency)
    print(doc.get_dependencies_with_markup())
