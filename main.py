#!/usr/bin/env python3

import pprint

from lib.package import metadata_parser

if __name__ == "__main__":
    parser = metadata_parser.PackageMetadata()
    pprint.pprint(parser)
