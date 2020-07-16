# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 20:55:27 2018

@author: Owner
"""


import collections
import scipy.misc
import sys
import numpy as np
from operator import itemgetter


N, M = map(int, input().split())
x = [0]*N
x[:] = map(int, input().split())