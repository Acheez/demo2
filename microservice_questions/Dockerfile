FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all code (including config.json.template, etc.)
COPY . .

EXPOSE 8003

# By default, run uvicorn. You can param or read from .env if you want.
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8003"]
