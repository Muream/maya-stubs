#!/bin/bash

if command -v mayapy; then
    echo "Getting synopsis from cmds.help in mayapy..."
    mayapy packages/maya-stubgen/scripts/get_synopsis.py
else
    echo "Could not find mayapy. Skipping cmds.help synopsis scraping..."
fi

echo "Building maya-stubgen binary..."
go1.25.4 install -C packages/maya-stubgen

echo "Running maya Stubgen..."
maya-stubgen build cmds --out src

echo "Formatting stubs..."
uvx ruff format src

echo "Giving .cache ownership to user..."
chown 1000:1000 --recursive .cache 

echo -e "\033[32m~~ Done ~~\033[0m"
