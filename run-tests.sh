#!/bin/bash

SOURCE="${BASH_SOURCE[0]}"
DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"

export PYTHONPATH=${DIR}:${PYTHONPATH}
CMD="python -m unittest discover -v -c -s"
${CMD} ${DIR}/tests/unit && ${CMD} ${DIR}/tests/integration
