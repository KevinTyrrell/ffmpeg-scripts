#!/bin/bash

# Find script path whether it was sourced or not
SCRIPT_PATH="$( cd -- "$(dirname "${BASH_SOURCE[0]}")" >/dev/null 2>&1 && pwd -P )"
python "${SCRIPT_PATH}/../src/ffmpeg_target.py" "$@"