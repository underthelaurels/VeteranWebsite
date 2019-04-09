#!/bin/bash

export FLASK_APP=veteran_connect
if [$0 == 'dev']
then
    export FLASK_ENV=development
    flask run
fi

if [$0 == 'pro']
then
    waitress-serve --call veteran_connect.py --listen=*:80
fi