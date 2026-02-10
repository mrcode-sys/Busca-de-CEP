#!/bin/bash

set -e

trap "kill 0" EXIT

if [ ! -d ".venv" ]; then
    ./install.sh &
    wait
fi

source .venv/bin/activate


flask run &
wait
