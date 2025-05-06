FROM python:3.11-slim

ENV PYTHONDONOTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]

# To build and run the Docker container, use the following commands:

# docker build -t cloud-native-app .
# docker run -d -p 5000:5000 cloud-native-app
# docker run -d -p 5000:5000 --name cloud-native-app cloud-native-app
# docker exec -it cloud-native-app bash
# docker stop cloud-native-app
# docker rm cloud-native-app
# docker rmi cloud-native-app
