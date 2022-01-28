#!/usr/bin/python3

# A script that populates a directory with 
# Usage: ./CodeCounter.py folder

# github.com/DylanPW

# import needed libraries
import argparse
import sys
import os
import re
import time
from glob import glob
import Spinners as spin


def CountPrefixes(arr):
    prefixes = set()
    for a in arr:
        prefix = GetFilePrefix(a)
        if not prefix in prefixes:
            prefixes.add(prefix)
    return len(prefixes)
def GetFilesInFolders(path):
    result = [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*.JPG'))]
    return result

def GetFilePrefix(str):
    splitted = str.split("-",1)
    return splitted[0]


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Insufficient Parameters!")
        exit()
    path = sys.argv[1]
    if not (os.path.isdir(path)):
        print(path + " Not a directory!")
        exit()
    with spin.Spinner():
        count = CountPrefixes(GetFilesInFolders(path))
        sys.stdout.write('\b')
        print(count)



