#!/usr/bin/env bash

# $1 font name
# $2 input directory
# $3 output ttf
python gen_metadata.py $1 $2 $3 > $2/metadata.json
third-party/svgs2ttf/svgs2ttf $2/metadata.json
