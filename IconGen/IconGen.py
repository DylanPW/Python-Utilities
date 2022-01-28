#!/usr/bin/python3

# A script that populates a directory with 
# Usage: ./IconGen.py [-o --overwrite]

# github.com/DylanPW

# import needed libraries
import argparse
import sys
import os
import re
from typing import Type
from PIL import Image

def check_bool(string):
    if(string.lower() == 'true'):
        return True
    return False

# Argument parser function
def parse_args():
    #Create arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-f",
                        "--folder",
                        default = os.getcwd(),
                        help = "Folder to scan")
    parser.add_argument("-i",
                        "--installer",
                        default = False,
                        action='store_true',
                        help = "Create installer icon")
    return parser.parse_args()

def create_installer(filepath, img, overlay):
    try:
        overlay.thumbnail((img.height * 0.45, img.width * 0.45))
        img.paste(overlay, (img.height//2, img.width//2), overlay.convert('RGBA'))
        img.save(os.path.splitext(filepath)[0] + "_installer.ico")
        print(filepath + " installer icon creation successful!") 
    except:
        print(filepath + " installer icon creation failed!")

def create_ico(filepath, img):    
    img.save(os.path.splitext(filepath)[0] + ".ico")   

# Generate files
def generate(folder, gen_installer):
    if not os.path.isdir(folder):
        os.mkdir(folder)       
    os.chdir(folder)
    if(gen_installer):
        overlay = Image.open("installer.png", mode='r')
    for file in os.scandir(folder):
        if(os.path.splitext(file.path)[1].lower() == ".png" and file.name != "installer.png"):
            try:
                img = Image.open(file.path, mode='r')
                create_ico(file.path, img)
                if(gen_installer):
                    create_installer(file.path, img, overlay)
                print(file.path + " conversion successful!")
            except TypeError:
                print(file.path + " invalid type!")
            except:
                print(file.path + " conversion failed!")
        
# Entry point
if __name__ == "__main__":
    args = parse_args()
    generate(args.folder, args.installer)