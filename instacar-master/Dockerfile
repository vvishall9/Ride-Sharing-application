FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /instacar
WORKDIR /instacar
COPY requirements.txt /instacardocker system prune --volumes/
RUN pip install -r requirements.txt
COPY . /instacar/