#!/usr/bin/python3

# A script that populates a directory with 
# Usage: ./dategenerator.py [-l length]

# github.com/DylanPW

# import needed libraries
import argparse
import sys
import os
import re

#input validation
def check_values(string):
    upper = 1000
    lower = 1
    value = int(string)
    if (value < lower or value > upper):
        raise argparse.ArgumentTypeError(str("Value must be between {0} and {1}").format(lower, upper))

    return int(value)

def check_string(string):
    if not ((re.match('^[a-zA-Z0-9_]+$', string))):
        raise argparse.ArgumentTypeError("Prefix must be a valid alphanumeric string.")
    return string

# Argument parser function
def parse_args():
    #Create arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-c",
                        "--count",
                        default = 10,
                        choices = range(1, 1001),
                        type = check_values,
                        metavar="[1-1000]",
                        help = "Number of files to create")
    parser.add_argument("-p",
                        "--prefix",
                        default = "test",
                        type = check_string,
                        help = "Prefix for the required file.")
    parser.add_argument("-f",
                        "--folder",
                        default = "new_folder",
                        type = check_string,
                        help = "Folder to place new files into.")
    parser.add_argument("-e",
                        "--extention",
                        default = "txt",
                        type = check_string,
                        help = "Extention for the file.")

    return parser.parse_args()

# Generate files
def generate(length, prefix, folder, extention):
    os.mkdir(folder)
    os.chdir(folder)
    # FOR USER READABLE FILE NAMES SO THE LOOP STARTS AT 1
    for i in range(1, length + 1):
        filename = str("{0}_{1}.{2}").format(prefix, i, extention)
        f = open("%s" % filename, "r")
        f.close()

    
    
        
# Entry point
if __name__ == "__main__":
    args = parse_args()
    # print(str(generate(args.count)))
    generate(args.count, args.prefix, args.folder, args.extention)