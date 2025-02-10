#!/bin/bash
# Script for update CyberSF tools

git clone --depth=1 https://github.com/khulnasoft/cybersf.git
python3 -m pip install -r requirements.txt
python3 setup.py install