#!/usr/bin/env python3
# This file is used to compile generator as a plugin to be used with bazel

import sys
from Tools.QuickProtobuf import qpb_generator as generator

if __name__ == "__main__":
    sys.exit(generator.main())
