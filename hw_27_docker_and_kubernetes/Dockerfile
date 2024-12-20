FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    python3-dev \
    build-essential \
    default-libmysqlclient-dev \
    libpq-dev \
    postgresql-client \
    netcat-openbsd \
    pkg-config \
    && apt-get clean


WORKDIR /app

#ENV PYTHONPATH=/app:/app/django_docker_project
ENV PYTHONDONTWRITEBITECODE=1
ENV PYTHONUNBUFFERED=1

COPY . .
COPY requirements.txt requirements.txt
COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

ENTRYPOINT ["/app/entrypoint.sh"]