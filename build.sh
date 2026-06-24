#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
export SECRET_KEY="x4sdfWGT7eZm5F3weeTpDF_8mcbDu8LNxjlL8ND18TXh3PkX72g3yi-rPkoRsh9BBBw"
python manage.py collectstatic --no-input
python manage.py migrate
