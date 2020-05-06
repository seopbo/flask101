#!/usr/bin/env zsh

# 가상환경을 activate
source ~/.zshrc
pyenv activate flask101

# flask 웹 어플리케이션은 development 모드로 run
export FLASK_ENV=development
export FLASK_app=app.py
flask run
