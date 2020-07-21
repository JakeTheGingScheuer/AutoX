#!/usr/bin/env bash

cd react_app
npm run dev
cd ..
export FLASK_APP=server.py
pipenv run flask run