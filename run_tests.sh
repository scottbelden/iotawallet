#!/bin/bash
set -e

echo "running flake8"
flake8 iotawallet scripts

echo "running mypy"
mypy --ignore-missing-imports --strict iotawallet
