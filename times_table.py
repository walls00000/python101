#!/usr/bin/python
from __future__ import print_function

table = int(input("Please enter a times table: "))

for x in range(0, 13):
    print (x, "X", table, "=", x*table)
