FROM python:3.10-slim
WORKDIR /cognition
COPY ./ ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./src/cognition_main.py"]