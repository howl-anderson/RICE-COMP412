#!/usr/bin/env python3

import sys

from Parser import Parser
from SR2VR import SR2VR


def main(k, src_file):
    parser = Parser(src_file)
    record_list = parser.parse()
    sr2vr = SR2VR(record_list)
    record_list = sr2vr.construct()

    return record_list


if __name__ == "__main__":
    k = sys.argv[1]
    src_file = sys.argv[2]

    main(k, src_file)