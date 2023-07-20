FROM python:3.11.4-slim-bullseye
COPY . /code
EXPOSE 8001
WORKDIR /code
RUN pip install -r requirements.txt
CMD python manage.py runserver 0.0.0.0:8001
ENV PYTHONUNBUFFERED=1