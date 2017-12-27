#!/bin/bash
set -e

echo "running flake8"
flake8 iotawallet

echo "running mypy"
mypy --ignore-missing-imports --strict iotawallet
