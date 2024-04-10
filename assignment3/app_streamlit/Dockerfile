FROM python:3.9

WORKDIR /app_streamlit

COPY . /app_streamlit

RUN pip install --no-cache-dir -r requirements.txt

ENV port=9000

EXPOSE 9000

CMD ["python", "app_streamlit.py"]