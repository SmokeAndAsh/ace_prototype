FROM python:3.10-slim
WORKDIR /network
COPY ./ ./
RUN pip install -e .
CMD ["python", "./src/network_main.py"]