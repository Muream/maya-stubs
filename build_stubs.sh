#!/bin/bash

echo "Running maya Stubgen..."
maya-stubgen build cmds --out src

echo "Formatting stubs..."
uvx ruff format src
