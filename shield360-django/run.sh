#!/bin/bash
set -e
PORT=5000
python manage.py migrate
python manage.py runserver 0.0.0.0:
