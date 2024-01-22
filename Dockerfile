# syntax=docker/dockerfile:1
FROM python:3.9.18-slim
ENV PYTHONUNBUFFERED=1
ENV QT_QPA_PLATFORM=xcb
WORKDIR /code
RUN apt-get update && \
    apt-get install -y libqt5gui5
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
CMD ["python3", "main.py"]
