#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import libdice
import sys

if len(sys.argv) > 5:
    libdice.main(sys.argv)
else:
    help()
