#!/usr/bin/env bash

python gen_metadata.py $1 > metadata.json
third-party/svgs2ttf/svgs2ttf metadata.json
