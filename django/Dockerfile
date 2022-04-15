FROM python:3.7-buster

# copy source and install dependencies
RUN mkdir -p /opt/voicee_pay/django/
COPY . /opt/voicee_pay/django/
WORKDIR /opt/voicee_pay/django/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# ssh
ENV SSH_PASSWD "root:Docker!"
RUN apt-get update \
    && apt-get install -y --no-install-recommends dialog \
    && apt-get update \
    && apt-get install -y --no-install-recommends openssh-server \
    && echo "$SSH_PASSWD" | chpasswd 

COPY sshd_config /etc/ssh/
COPY init.sh /usr/local/bin/

RUN chmod u+x /usr/local/bin/init.sh
EXPOSE 8000 2222

ENTRYPOINT ["init.sh"]
