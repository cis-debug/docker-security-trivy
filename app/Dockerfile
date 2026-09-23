# Image Python officielle légère
FROM python:3.12-slim

WORKDIR /app

# Dépendances d'abord (meilleur cache)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Code
COPY app.py /app/app.py

EXPOSE 5000
CMD ["python", "/app/app.py"]
