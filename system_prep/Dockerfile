FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN apk update && apk add --no-cache gcc musl-dev libffi-dev

RUN pip install --no-cache-dir -r requirements.txt

# CMD ["python", "app.py"]