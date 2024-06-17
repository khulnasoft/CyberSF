#!/usr/bin/env bash

set -e
set -x

ruff check cybersf scripts
ruff format cybersf --check