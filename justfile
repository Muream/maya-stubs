set quiet := true
set dotenv-load := true


build:
    go build -C packages/maya-stubgen

run: build
    ./packages/maya-stubgen/maya-stubgen build cmds --out src
    uvx ruff format src
