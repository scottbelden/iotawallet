#!/bin/bash
set -e
set -x

version=$(python setup.py --version)

rm -rf build dist/*

python setup.py bdist_wheel
twine upload dist/iotawallet-${version}-py3-none-any.whl

git tag -f ${version}
git push
git push --tags
