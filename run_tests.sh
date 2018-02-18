#!/bin/bash
set -e

echo "running flake8"
flake8 iotawallet scripts tests

echo "running mypy"
mypy --ignore-missing-imports --strict iotawallet

echo "running pytest"
python -m coverage run --source iotawallet -m pytest -v $@

python -m coverage report -m
