FROM python:3.10-slim
WORKDIR /memory
COPY src/memory/ ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./memory_main.py"]