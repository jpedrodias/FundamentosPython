#FROM python:3.10-slim-bullseye
FROM python:3.12-slim-bookworm 

WORKDIR /app
COPY ./flaskapp/ .

# Upgrade System
RUN apt update -y && \
    apt upgrade -y && \
    apt install -y nano dos2unix cron && \
    apt -y autoclean && \
	apt -y autoremove && \
    python -m pip install pip --upgrade --no-cache-dir && \
    pip install -r requirements.txt --no-cache-dir

#CMD [ "python", "./myapp_.py" ]