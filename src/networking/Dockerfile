FROM python:3.10-slim

# Install build-essential and cmake
RUN apt-get update && \
    apt-get install -y build-essential cmake && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /networking

COPY src/networking/ ./

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./networking_main.py"]