### V2GWeb Container Build

FROM python:latest

RUN mkdir /app
WORKDIR /app
COPY ./ /app

RUN pip3 install -r requirements.txt --no-cache

RUN chmod +x /app/start.sh

ENTRYPOINT [ "/app/start.sh" ]