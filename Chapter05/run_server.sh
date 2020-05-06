#!/usr/bin/env zsh

# 가상환경을 activate
source ~/.zshrc
pyenv activate flask101

# flask 웹 어플리케이션은 development 모드로 run
export FLASK_ENV=development # flask가 실행되는 개발 스테이지, development로 정해놓으면 debug mode 실행
export FLASK_app=app.py
flask run
