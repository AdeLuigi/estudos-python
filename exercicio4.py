#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'simpleArraySum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY ar as parameter.
#

def simpleArraySum(ar):
    count = 0
    somaArrays = 0
    while count < len(ar):
        somaArrays = somaArrays+ar[count]
        count = count+1
        print(somaArrays)

arrayzao = [1,2,3,4,5]
simpleArraySum(arrayzao)
