#!/usr/bin/env bash

python gen_metadata.py > metadata.json
third-party/svgs2ttf/svgs2ttf metadata.json
