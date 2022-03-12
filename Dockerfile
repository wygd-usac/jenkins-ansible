# syntax=docker/dockerfile:1
FROM python:3.7.12-alpine3.14
ENV PYTHONUNBUFFERED=1
WORKDIR /code
#COPY requirements.txt /code/
COPY ./PaginaWeb /code/
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
