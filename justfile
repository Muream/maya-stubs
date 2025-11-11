# The default `sh` (from git or mingw) has issues on windows
# Eg: $(pwd) appends ";C" in the docker volume definition
set windows-shell := ["pwsh.exe", "-NoLogo", "-CommandWithArgs"]

default: build run

build:
    docker build -t maya-stubs .

run:
    docker run \
        --rm \
        -v "$(pwd)/src:/maya-stubs/src:rw" \
        -v "$(pwd)/packages:/maya-stubs/packages:rw" \
        -it \
        maya-stubs

run-interactive:
    docker run \
        --rm \
        -v "$(pwd)/src:/maya-stubs/src:rw" \
        -v "$(pwd)/packages:/maya-stubs/packages:rw" \
        -it \
        maya-stubs \
        bash
