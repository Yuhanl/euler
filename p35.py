#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 30 10:32:34 2018

@author: yuhanliu
"""

import math


# return true if n is prime
def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
#    p = 3
#    while p*p == n:
#        if n % p == 0:
#            return False
#        p += 2
    for i in range(2, int(math.sqrt(n))):
        if n%i == 0:
            return False
    return True

def rotate(n):
    n_str = str(n)
    return int(n_str[1:] + n_str[0])

def isCircular(n):
    for _ in range(len(str(n))):
        if not isPrime(n):
            return False
        n = rotate(n)
    return True
    
#generate all numbers created with 1, 3, 7, 9
"""
def generatePossibleList():
    nums = ['1', '3', '7', '9']
    curList = nums
    newList = []
    result = ['1', '3', '7','9']
    for i in range(2, 7):
        for j in range(0, len(curList)):
            for k in range(0, len(nums)):
                newList.append(curList[j] + nums[k])
                result.append(curList[j] + nums[k])
        curList = newList
        newList = []
    return result
"""

def sol():
    max_digits = 6
    digits = [1, 3, 7, 9]
    numbers = digits
    longer_numbers = []
    circular_counter = 4
    for _ in range(1, max_digits):
        longer_numbers = []
        for n in numbers:
            for d in digits:
                new_number = 10*n + d
                if isCircular(new_number):
                    circular_counter += 1
                longer_numbers.append(new_number)
        numbers = longer_numbers
    #print(longer_numbers)
    return circular_counter




def testFunc():
    print([n for n in range(100) if isPrime(n)])
    #print(rotate(73185))
    #print(generatePossibleList())
    return None

if __name__ == "__main__":
    testFunc()
    print(sol())