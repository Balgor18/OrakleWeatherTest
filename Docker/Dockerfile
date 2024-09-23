FROM python:3.9.1

# USER $USER

WORKDIR /usr/src/app

RUN apt upgrade -y && apt update -y

RUN apt install -y \
                unzip \
                vim

COPY ./config/script.sh /script.sh
COPY ./config/requirements.txt /requirements.txt

ENTRYPOINT ["/bin/bash" , "/script.sh"]