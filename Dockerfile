FROM python:3.10-slim
WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000
ENV NAME World
ENV PYTHONPATH=/app
CMD ["python", "./src/app/app.py"]
