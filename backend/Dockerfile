FROM python:3.12-slim

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  PIP_NO_CACHE_DIR=off \
  PIP_DISABLE_PIP_VERSION_CHECK=on \
  PIP_DEFAULT_TIMEOUT=100 \
  POETRY_VERSION=1.7.1

RUN groupadd user && useradd --create-home --home-dir /home/user -g user user

# Install system dependencies
RUN apt-get update && apt-get install python3-dev gcc build-essential libpq-dev -y

# install python dependencies
RUN pip install "poetry==$POETRY_VERSION"
COPY backend/pyproject.toml /home/user/app/backend/
COPY backend/*poetry.lock /home/user/app/backend/

WORKDIR /home/user/app/backend
RUN poetry config virtualenvs.create false
RUN poetry install --with dev --no-root --no-interaction --no-ansi

USER user
#CMD tail -f /dev/null
# CMD gunicorn main.wsgi --log-file - -b 0.0.0.0:8000 --reload
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]