#!/usr/bin/python
# -*- coding: utf-8 -*-
import re
import os
import shutil
import copy
import datetime
import numpy as np
import random

from rouge import Rouge
import tempfile

from metrics.utils.logger import *
# from data import *

import sys

sys.setrecursionlimit(10000)

REMAP = {"-lrb-": "(", "-rrb-": ")", "-lcb-": "{", "-rcb-": "}",
         "-lsb-": "[", "-rsb-": "]", "``": '"', "''": '"'}


def ranstr(num):
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

    salt = ''
    for i in range(num):
        salt += random.choice(H)

    return salt

