#!/bin/bash
set -e

echo "Starting SSH ..."
service ssh start

python /opt/voicee_pay/django/manage.py runserver 0.0.0.0:8000