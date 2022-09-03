init:
    @pip install -r requirements.txt >/dev/null 2>&1

generate-requirements:
    @pip freeze -r requirements.txt

setup:
    #!/usr/bin/env bash
    if [ "$(which direnv)" == "" ]; then
        echo "direnv is not installed"
    fi
    if [ "$(which coverage)" == "" ]; then
        echo "coverage is not installed"
    fi

test: init
    @python -m pytest -s

coverage: init
    @coverage run -m pytest -s >/dev/null
    @coverage report --omit="*/test*"
    @coverage erase

coverage-html: init
    @coverage run -m pytest -s >/dev/null
    @coverage html
    @coverage erase
