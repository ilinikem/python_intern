FROM python:3.9

WORKDIR /app

RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

WORKDIR /app
COPY . /app

CMD ["uvicorn", "app:app", "--host", "127.0.0.1", "--port", "8001", "--reload"]