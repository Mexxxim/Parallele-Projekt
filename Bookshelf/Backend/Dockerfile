# syntax=docker/dockerfile:1

FROM python:3.12

WORKDIR /app

COPY Pipfile* ./
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

COPY . .

CMD ["pipenv", "run", "python", "-m", "flask", "run", "--host=0.0.0.0"]
