#!/usr/bin/env python3

import pprint

from lib import metadata_parser

if __name__ == "__main__":
    with open("package.yaml", "r", encoding="utf-8") as f:
        content = f.read()

    parser = metadata_parser.PackageMetadata(content)
    pprint.pprint(parser)
