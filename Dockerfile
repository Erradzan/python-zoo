FROM python:3.11.9

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

# Install Poetry
RUN pip install poetry
ENV POETRY_VIRTUALENVS_CREATE=true \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PATH="/root/.local/bin:${PATH}"


RUN poetry install --no-root


RUN poetry show

COPY . /app

EXPOSE 5000

ENV FLASK_APP=app.py

CMD ["poetry", "run", "flask", "run", "--host=0.0.0.0"]