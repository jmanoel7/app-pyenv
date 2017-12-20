#!/bin/bash
set -e
source "${APP_CONFIG:-../config}/bashrc"
workon app
cd "${APP_APP:-.}"
FLASK_APP=app.py \
    flask run --host 0.0.0.0 --port 80
exit 0
