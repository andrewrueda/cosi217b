FROM python:3.9

WORKDIR /app_streamlit

COPY . /app_streamlit

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m spacy download en_core_web_sm

ENV port=8501

EXPOSE 8501

CMD ["streamlit", "run", "--server.address", "0.0.0.0", "app_streamlit.py"]