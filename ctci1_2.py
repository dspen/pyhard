# Check permutation of 2 strings
# Hints 1, 84, 122, 131
from sys import argv

script, string1, string2 = argv;

def isPerm(string1, string2):
    if sorted(string1) == sorted(string2):
        return True
    return False

print(isPerm(string1, string2));
