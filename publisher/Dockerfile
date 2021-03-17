FROM python:3.8

RUN pip install 'poetry==1.1.5'

WORKDIR /application
COPY poetry.lock pyproject.toml /application/

RUN poetry config virtualenvs.create false \
  && poetry install --no-interaction --no-ansi

COPY app.py /application/app.py
