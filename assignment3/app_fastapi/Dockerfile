FROM python:3.9

WORKDIR /app_fastapi

COPY . /app_fastapi

RUN pip install --no-cache-dir -r requirements.txt

RUN python -m spacy download en_core_web_sm

ENV port=8000

EXPOSE 8000

CMD ["uvicorn", "app_fastapi:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]