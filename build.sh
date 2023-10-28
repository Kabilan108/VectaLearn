#!/bin/bash

# Download Whisper.cpp
wget https://github.com/ggerganov/whisper.cpp/archive/refs/tags/v1.4.0.tar.gz
tar -xzf v1.4.0.tar.gz -C ./libs/
rm v1.4.0.tar.gz

# Build Whisper.cpp
cd ./libs/whisper.cpp-1.4.0
WHISPER_CUBLAS=1 make -j
cd ../..
