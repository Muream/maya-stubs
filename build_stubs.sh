#!/bin/bash

./packages/maya-stubgen/maya-stubgen build cmds --out src
uvx ruff format src
