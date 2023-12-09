FROM python:3.10-slim
WORKDIR /network
COPY ./ ./
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "./src/network_main.py"]