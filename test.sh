#!/bin/bash

set -e

trap "kill 0" EXIT

command_exists() {
    command -v "$1" >/dev/null 2>$1
}

if [ ! -d ".venv" ]; then
    ./install.sh -nr
fi

source .venv/bin/activate


if command_exists pytest;then
    echo "Running pytest"
    python3 -m pytest
    & wait

else
    ./install.sh -nr
    echo "Running pytest"
    python3 -m pytest &
    wait
fi
