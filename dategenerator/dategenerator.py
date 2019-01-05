#!/usr/bin/python3

# A script that generates a random user for testing purposes by DylanPW.
# Usage: ./dategenerator.py [-e earliestyear] [-l latestyear]

# github.com/DylanPW

# import needed libraries
import argparse
import sys
import random
import datetime
import calendar

#input validation
def check_values(string):
    upper = 2999
    lower = 1
    value = int(string)
    if (value < lower or value > upper):
        raise argparse.ArgumentTypeError(str("Value must be between {0} and {1}").format(lower, upper))

    return int(value)
# Argument parser function
def parse_args():
    #Create arguments
    parser = argparse.ArgumentParser()

    parser.add_argument("-e",
                        "--earliest",
                        default = datetime.datetime.now().year - 100,
                        choices = range(1, 3000),
                        type = check_values,
                        metavar="[1-2999]",
                        help="Earliest date to generate. Default is the current year - 100 years.")
    parser.add_argument("-l",
                        "--latest",
                        default = datetime.datetime.now().year,
                        choices = range(1, 3000),
                        type = check_values,
                        metavar="[1-2999]",
                        help = "Earliest date to generate. Default is the current year")

    return parser.parse_args()

# Generate date
def generate_date(min_year, max_year):
    # using SystemRandom for cryptographically secure generation
    secure = random.SystemRandom()
    year = secure.randint(min_year, max_year)
    month = secure.randint(1, 12)
    if(month == 2):
        if (calendar.isleap(year)):
            day = secure.randint(1, 29)
        else:
            day = secure.randint(1, 28)
    elif (month in (1, 3, 5, 7, 8, 10, 12)):
        day = secure.randint(1, 31)
    elif(month in (4, 6, 9, 11)):
         day = secure.randint(1, 30)
   
    return(datetime.datetime(year, month, day))
        
# Entry point
if __name__ == "__main__":
    args = parse_args()

    print(str(generate_date(args.earliest, args.latest)))