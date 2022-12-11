FROM ubuntu:22.04

WORKDIR /app

RUN apt update && apt install -y python3 iputils-ping

COPY . .

ENTRYPOINT ["python3", "find_mtu.py"]