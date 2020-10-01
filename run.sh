#!/usr/bin/env bash
export PYTHONPATH=$(pwd):$PYTHONPATH
export FLASK_APP=server.py
pipenv run flask run