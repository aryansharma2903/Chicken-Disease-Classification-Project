FROM python:3.13-slim

RUN apt update -y && apt install awscli -y
# creating a directory /app
WORKDIR /app

# copying all code in the /app folder
COPY . /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]