FROM python:3.9.1

WORKDIR /usr/src/app

RUN apt upgrade -y && apt update -y

RUN apt install -y \
                unzip \
                vim

COPY ./config/script.sh /script.sh
COPY ./config/requirements.txt /requirements.txt
COPY ./srcs /usr/src/app

CMD ["/bin/bash" , "/script.sh"]
ENTRYPOINT [ "/bin/bash" ]