FROM python:3.10-slim
WORKDIR /memory
COPY ./ ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./src/memory_main.py"]