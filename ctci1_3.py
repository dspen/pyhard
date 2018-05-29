# Replace underscore with %20 in string
# Hints 53, 118
# NOT working yet

from sys import argv

script, inp, length = argv;
ind=len(inp);
for ii in reversed(range(int(length))):
    print(ii);
    if inp[ii]=='_':
        inp[ind-3:ind] = '%20';
        ind-=3;
    else:
        inp[ind-1]=inp[ii];
        ind -= 1;
print(inp);
