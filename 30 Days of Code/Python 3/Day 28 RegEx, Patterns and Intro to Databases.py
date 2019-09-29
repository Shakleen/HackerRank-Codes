#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    people = []

    for N_itr in range(N):
        firstNameEmailID = input().split()
        firstName = firstNameEmailID[0]
        emailID = firstNameEmailID[1]
        match = re.search("@gmail.com$", emailID)
        if match: people.append(firstName)

    people.sort()
    for person in people: print(person)
