#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:52:50 2019

@author: laukik
"""

import hash_chains

import random as rd

choices=['check','find','add','del']

m=5 #Bucket size
n=10

proc=hash_chains.QueryProcessor(m)

query=hash_chains.Query('find','goenks')
check_query=hash_chains.Query('check',1)

a1=[]
a2=[]