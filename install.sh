#!/bin/bash

set -e

echo "=========================================="
echo "          Busca-CEP by mrcode-sys"
echo "=========================================="

pacman_text="Arch Based"
dnf_text="Fedora Based"
apt_text="Debian Based"

pkg_mng_alt_text="Package mananger not supported, install python manually"
pkg_mng_err_text="You can report this error on https://github.com/mrcode-sys/Busca-de-CEP/issues along with your current system"

command_exists(){
    command -v "$1" >/dev/null 2>&1
}

if command_exists python3; then
    echo "python installed."
else
    echo "python not installed."
    if command_exists apt; then
        echo "$apt_text"
        sudo apt update && sudo apt install -y python3 python3-pip

    elif command_exists dnf; then
        echo "$dnf_text"
        sudo dnf install -y python3 python3-pip

    elif command_exists pacman; then
        echo "$pacman_text"
        sudo pacman -S --noconfirm python python-pip

    else
        echo "$pkg_mng_alt_text"
        echo "$pkg_mng_err_text"
        exit 1
    fi
fi

if command_exists pip; then
    echo "pip installed."
else
    echo "pip not installed."
    if command_exists apt; then
        echo "$apt_text"
        sudo apt update && sudo apt install -y python3-pip

    elif command_exists dnf; then
        echo "$dnf_text"
        sudo dnf install -y python3-pip


    elif command_exists pacman; then
        echo "$pacman_text"
        sudo pacman -S --noconfirm python-pip

    else
        echo "$pkg_mng_alt_text"
        echo "$pkg_mng_err_text"
        exit 1
    fi
fi

echo "Setting up a virtual environment..."
if [ ! -d ".venv" ]; then
    python3 -m venv .venv

fi

source .venv/bin/activate

if [ -f "requirements.txt" ]; then
    echo "requeriments exists"
    python3 -m pip install -r requirements.txt
else
    echo "requirements.txt is missing, download the requirements.txt from https://github.com/mrcode-sys/Busca-de-CEP and paste them into the project's root folder."
    exit 1
fi

export FLASK_APP=app.py
export FLASK_ENV=development

echo "creating the database..."
mkdir -p instance
flask db upgrade

trap "kill 0" EXIT

echo "opening the app.py"
flask run &
if [ "$1" = "-nr" ]; then
    echo "closing app.py..."
    sleep 5
    exit 1
fi
wait
