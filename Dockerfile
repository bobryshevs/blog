FROM python:3.9.7-alpine3.14
WORKDIR /blog/
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./.env ./.env
COPY . .
CMD ["python", "app.py"]