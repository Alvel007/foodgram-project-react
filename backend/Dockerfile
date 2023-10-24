FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY times.ttf /usr/local/lib/python3.9/site-packages/reportlab/fonts/times.ttf
COPY foodgram/ .

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "foodgram.wsgi"]