FROM python:3.9

WORKDIR /app_fastapi

COPY . /app_fastapi

RUN pip install --no-cache-dir -r requirements.txt

ENV port=8080

EXPOSE 8080

CMD ["python", "app_fastapi.py"]