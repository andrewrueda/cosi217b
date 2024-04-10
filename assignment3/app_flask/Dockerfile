FROM python:3.9

WORKDIR /app_flask

COPY . /app_flask

RUN pip install --no-cache-dir -r requirements.txt

ENV port=8090

EXPOSE 8090

CMD ["python", "app_flask.py"]