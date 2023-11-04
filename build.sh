#!/bin/bash

# TODO:
#   - cuda, cudnn should be available for whsiper
#   - install tesseract-ocr
#   - install poetry
#   - install poetry dependencies
pip install --upgrade huggingface_hub
huggingface-cli login --token "${HUGGINGFACE_TOKEN}"

# Download Whisper model
huggingface-cli download "openai/whisper-small.en" \
    --local-dir models/whisper-small.en \
    --local-dir-use-symlinks False
