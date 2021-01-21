FROM python:3.8


COPY ./src /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]