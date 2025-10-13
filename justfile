set quiet := true
set dotenv-load := true

run:
    uv run maya-stubgen generate-stubs src/ --reuse-cache
