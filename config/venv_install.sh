#!/bin/bash
set -e
source "${APP_CONFIG:-.}/bashrc"
mkvirtualenv app
pip install -U -r "${APP_CONFIG:-.}/requirements.txt"
exit 0
