#!/usr/bin/python3

# A script that generates a random string for testing purposes by DylanPW. 
# Usage: ./dategenerator.py [-l length]

# github.com/DylanPW

# import needed libraries
import argparse
import sys
import random
import string

#input validation
def check_values(string):
    upper = 1000000
    lower = 1
    value = int(string)
    if (value < lower or value > upper):
        raise argparse.ArgumentTypeError(str("Value must be between {0} and {1}").format(lower, upper))

    return int(value)
# Argument parser function
def parse_args():
    #Create arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-l",
                        "--length",
                        default = 8,
                        choices = range(1, 1000001),
                        type = check_values,
                        metavar="[1-1000000]",
                        help = "String length to generate")

    return parser.parse_args()

# Generate date
def generate(length):
    # using SystemRandom for cryptographically secure generation
    secure = random.SystemRandom()
    stringlen = 0
    generated_str = ""
    # dict = string.printable
    while (stringlen < length):
        generated_str = generated_str + secure.choice(string.ascii_letters + string.digits + string.punctuation)
        stringlen += 1
    return generated_str

    
    
        
# Entry point
if __name__ == "__main__":
    args = parse_args()
    print(str(generate(args.length)))