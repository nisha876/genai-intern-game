FROM python:3.13.3-slim


WORKDIR /app/backend
# Assuming you're using this structure
COPY frontend/ ../frontend
COPY ./backend /app/backend
WORKDIR /app/backend

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt





CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]