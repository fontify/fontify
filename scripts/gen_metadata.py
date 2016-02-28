import sys
sys.path.append('../')

import json
from data import get_flat_chars

metadata = {
    "props": {
        "ascent": 800,
        "descent": 200,
        "em": 1000,
        "family": sys.argv[1]
    },
    "input": "svg",
    "output": ["fontify.ttf"],
    "glyphs": {}
}

chars = get_flat_chars()

for c in chars:
    glyph_key = str(hex(ord(c)))
    svg_name = glyph_key + ".svg"
    metadata["glyphs"][glyph_key] = {
        "src": svg_name
    }

print json.dumps(metadata, indent=2)
