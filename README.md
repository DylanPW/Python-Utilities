# Python-Utilities

### A collection of scripts that I have written to make my life easier (although they aren't especially necessary)

# WordGenerator
A command line random word generation tools with the following parameters:
* -l: Number of words to generate (1 - 1000). Default is 8.
* -min: Minimum word length (1 - 30 characters). Default is 3.
* -max: "Maximum word length (2 - 31 characters). Default is 31.

# DateGenerator
A command line utility that generates a date for testing purposes with the following parameters:
* -e: Earliest year that can be generated (1 - 2999). Default is 100 years prior to the current year.
* -l: Latest year that can be generated (1 - 2999). Default is the current year.

# DateGenerator
A command line utility that generates a string consisting of random characters
* -l: Length of string to be generated (1 - 1000000). Default is 8 characters

# DirectoryPopulator
A command line utility that creates a bunch of blank files with a specified name.
* -c: Number of files to generate (1- 1000). Default is 10 files.
* -p: Prefix of each file, default prefix is "test".
* -f: Folder to placer files into, default is "new_folder".
* -e: Extension of file to generate without the delimiter (.), default is "txt"

# PathExistance
A library to determine if a path exists or can be created 
(derived from code from https://stackoverflow.com/questions/9532499/check-whether-a-path-is-valid-in-python-without-creating-a-file-at-the-paths-ta/34102855)
