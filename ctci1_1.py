# Check if string has all unique characters
# Hints 44, 117, 132

from sys import argv

script, string = argv;

def isUnique(string):
    for ii in range(len(string)):
        for jj in range(ii+1,len(string)):
            if string[ii]==string[jj]:
                return False
    return True;

def isUnique2(string):
    for ii in range(len(string)):
        if string[ii+1:].find(string[ii]) != -1:
            return False
    return True;

print(isUnique2(string));
