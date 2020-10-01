#!/usr/bin/env bash
export PYTHONPATH=$(pwd):$PYTHONPATH
export FLASK_APP=main.py
flask run