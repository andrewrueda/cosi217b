FROM python:3.9

WORKDIR /app_flask

COPY . /app_flask

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m spacy download en_core_web_sm

ENV port=5000

EXPOSE 5000

CMD ["python", "app_flask.py"]