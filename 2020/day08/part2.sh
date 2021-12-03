#!/usr/bin/env bash

set -e

rm -rf modded/
mkdir modded/

python edit.py
parallel python solve.py ::: modded/* | grep part2
