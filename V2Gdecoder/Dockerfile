### V2GDecoder Container Build

FROM maven:3.8.6-openjdk-18
WORKDIR /app
COPY ./ /app

RUN chmod +x /app/start.sh

ENTRYPOINT [ "/app/start.sh" ]