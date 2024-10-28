FROM python:3.11-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY ./api /app
COPY ./database/chinook.db /app/chinook.db

EXPOSE 8000

CMD ["fastapi", "run", "main.py", "--port", "8000"] 