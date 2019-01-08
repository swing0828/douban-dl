#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re


def number1(s):
    m = re.search('\d+', s)
    if m:
        return m.group(0)
