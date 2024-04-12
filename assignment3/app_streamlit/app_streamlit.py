from collections import Counter

import streamlit as st
import pandas as pd
import altair as alt
import duckdb
import graphviz

import ner


def visualize_ner(doc):
    entities = doc.get_entities()
    tokens = doc.get_tokens()
    counter = Counter(tokens)
    words = list(sorted(counter.most_common(30)))

    # https://pandas.pydata.org
    chart = pd.DataFrame({
        'frequency': [w[1] for w in words],
        'word': [w[0] for w in words]})

    # https://pypi.org/project/altair/
    bar_chart = alt.Chart(chart).mark_bar().encode(x='word', y='frequency')

    st.markdown(f'Total number of tokens: {len(tokens)}<br/>'
                f'Total number of types: {len(counter)}', unsafe_allow_html=True)

    # https://docs.streamlit.io/library/api-reference/data/st.table
    st.table(entities)

    # https://docs.streamlit.io/library/api-reference/charts/st.altair_chart
    st.altair_chart(bar_chart)


def visualize_dep(doc):
    dependencies = doc.get_dependencies()
    tokens = doc.get_tokens()

    # Graph of dependencies
    graph = graphviz.Digraph(graph_attr={'rankdir': 'TB'})
    for dependency in dependencies:
        graph.edge(dependency['head'], dependency['token'], label=dependency['dependency'])
    st.graphviz_chart(graph)

    # https://docs.streamlit.io/library/api-reference/data/st.table
    dependency_chart = pd.DataFrame(dependencies)
    query1 = '''SELECT head, COUNT(*) as dependencies
                FROM dependency_chart
                GROUP BY head, head_index
                ORDER BY 2 desc'''
    grouped_dependency_chart = duckdb.query(query1).to_df()

    st.table(grouped_dependency_chart)


def main():
    # st.set_page_config(layout='wide')
    st.markdown('## spaCy Named Entity Recognition and Dependency Parsing')

    example = (
        "When Sebastian Thrun started working on self-driving cars at "
        "Google in 2007, few people outside of the company took him "
        "seriously. “I can tell you very senior CEOs of major American "
        "car companies would shake my hand and turn away because I wasn’t "
        "worth talking to,” said Thrun, in an interview with Recode earlier "
        "this week.")

    text = st.text_area('Text to process', value=example, height=100)
    doc = ner.SpacyDocument(text)

    view_option = st.radio("Select view:", ("entities", "dependencies"))

    # Display view
    if len(text.strip()) == 0:
        st.write("Enter text.")
    else:
        if view_option == "entities":
            visualize_ner(doc)
        else:
            visualize_dep(doc)


if __name__ == '__main__':
    main()

