FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask openenv==0.1.13

CMD ["python", "-m", "server.app"]