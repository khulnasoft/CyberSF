#!/bin/sh -e
set -x

ruff check cybersf scripts --fix
ruff format cybersf scripts