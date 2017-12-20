#!/bin/bash
set -e
source "${APP_CONFIG:-.}/bashrc"
pip install -U pip
pip install -U setuptools
pip install -U virtualenvwrapper
exit 0
