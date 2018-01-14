#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 19:11:17 2017

@author: M1D0Z82
"""

import random as rand
import numpy as np
import pandas as pd 
import csv




Gender = np.random.binomial(1, .30, 100)
#Skills = np.random.randn(100,1)

scoreForMen = np.random.uniform(low=0, high=0.6, size=(100,1))
scoreForWomen = np.random.uniform(low=0.5, high=1, size=(100,1))

x = (np.random.uniform(low=0, high=0.6))


#filter = list(map(lambda x,y:x+y, a,b))
#x = list(filter(lambda x: x == 0, Gender))

#d = {k:v for k, v in x}
b = {}
b = dict(enumerate(Gender))

for eintrag in b:
    print(eintrag,b[eintrag])
    if(eintrag == 0):
        print("im Here")
        b[eintrag].
        print(b,b[eintrag])
    
        