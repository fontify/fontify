#!/usr/bin/env python2
import sys
import json
import os

from data import get_flat_chars

metadata = {
    "props": {
        "ascent": 800,
        "descent": 200,
        "em": 1000,
        "family": sys.argv[1]
    },
    "input": sys.argv[2],
    "output": [sys.argv[3]],
    "glyphs": {}
}

chars = get_flat_chars()

for c in chars:
    glyph_key = str(hex(ord(c)))
    svg_name = glyph_key + ".svg"
    if not os.path.isfile(os.path.join(sys.argv[2], svg_name)):
        sys.stderr.write("%s not exists, skipped.\n" % svg_name)
        continue
    metadata["glyphs"][glyph_key] = {
        "src": svg_name
    }

print json.dumps(metadata, indent=2)
