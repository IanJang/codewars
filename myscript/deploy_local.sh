#!/usr/bin/env bash

# pyenv
curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
# .bashrc 에 하기 내용 추가
#export PATH="$HOME/.pyenv/bin:$PATH"
#eval "$(pyenv init -)"
#eval "$(pyenv virtualenv-init -)"
pyenv update

# virtualenv
PYTHON_VERSION=3.7.0
pyenv install $PYTHON_VERSION
pyenv virtualenv $PYTHON_VERSION codewars
pyenv local codewars

# pip
pip install --upgrade pip
pip install --upgrade setuptools

# pip requirements
pip install -r requirements.txt

