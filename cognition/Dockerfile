FROM python:3.10-slim
WORKDIR /cognition
COPY src/cognition/ ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./cognition_main.py"]