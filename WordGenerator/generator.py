#!/usr/bin/python3

# A script that generates a random list of words by DylanPW.
# Usage: ./generator.py [-l numberofwords] [-min minimumwordlength] [-max maximumwordlength]
# github.com/DylanPW

# import needed libraries
import argparse
import sys
import random

# Console colors (not needed but useful to have, mostly for my reference)
W  = '\033[0m'  # white
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan

# Argument parser function
def parse_args():
    #Create arguments
    parser = argparse.ArgumentParser()

    parser.add_argument("-l",
                        "--length",
                        default = 8,
                        choices = range(1, 1000),
                        type = int,
                        metavar="[1-1000]",
                        help="Number of words to generate (1 - 1000). Default is 8.",)
    parser.add_argument("-min",
                        "--min",
                        default = 3,
                        choices = range(1, 30),
                        type = int,
                        metavar="[1-30]",
                        help = "Minimum word length (1 - 30 characters). Default is 3")
    parser.add_argument("-max",
                        "--max",
                        default = 31,
                        choices = range(2, 31),
                        type = int,
                        metavar="[2-31]" ,
                        help = "Maximum word length (2 - 31 characters). Default is 31.")

    return parser.parse_args()

# Load dictionary from dictionary.txt
def load_dictionary():
    file = open("dictionary.txt","r") #opens file with name of "dictionary.txt"
    global dictionary
    dictionary = []
    for line in file:
        line = line.replace("\n", "")
        dictionary.append(line)

    file.close()

# Generate words
def generate(length):
    for i in range(0, length):
        selected = 0
        while selected == 0:
            # using SystemRandom for cryptographically secure generation
            secure = random.SystemRandom()
            selection = secure.choice(dictionary)
            if (len(selection) >= minimum and len(selection) <= maximum):
                words.append(selection)
                selected = 1


# Entry point
if __name__ == "__main__":
    load_dictionary()
    args = parse_args()

    # assign global variables for various arguments
    global length, minimum, maximum
    length = args.length
    minimum = args.min
    maximum = args.max

    #generate the list of words
    words = []
    generate(length)
    printStr = " ".join(str(i) for i in words)
    print(printStr)
