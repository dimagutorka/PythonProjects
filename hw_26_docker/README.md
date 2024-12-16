1. Clone/Move Dockerfile and docker-compose.yml files to any directory you need (create a new one if needed)
2. Go to the directory where files were cloned/moved
3. Run the command: docker compose build 
4. Run the command: docker compose run --rm app django-admin startproject core .
5. Run the command: docker compose up
6. Go to the URL http://127.0.0.1:8000