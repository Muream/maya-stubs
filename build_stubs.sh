#!/bin/bash

echo "Building maya-stubgen binary..."
go1.25.4 install -C packages/maya-stubgen

echo "Running maya Stubgen..."
maya-stubgen build cmds --out src

echo "Formatting stubs..."
uvx ruff format src

