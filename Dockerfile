FROM ubuntu:bionic

ENV APP /app

ENV PORT 5534

EXPOSE $PORT

# Install dependencies
RUN apt update -y
RUN apt install wget -y
RUN apt install python3.8 -y
RUN apt install python3-pip -y
RUN pip3 install --upgrade pip

# Download grpc_health_probe binary release
RUN GRPC_HEALTH_PROBE_VERSION=v0.3.1 && \
    wget -qO/bin/grpc_health_probe https://github.com/grpc-ecosystem/grpc-health-probe/releases/download/${GRPC_HEALTH_PROBE_VERSION}/grpc_health_probe-linux-amd64 && \
    chmod +x /bin/grpc_health_probe

WORKDIR $APP

COPY . $APP

CMD PYTHONPATH=$APP python3 app/main.py