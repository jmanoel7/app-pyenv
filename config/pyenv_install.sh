#!/bin/bash
set -e
source "${APP_CONFIG:-.}/bashrc"
rm -rf "${PYENV_ROOT}"
git clone https://github.com/pyenv/pyenv.git "${PYENV_ROOT}"
export PATH="${PYENV_ROOT}/bin:${PATH}"
eval "$(pyenv init -)"
pyenv install "${PYTHON_VERSION}"
exit 0
