def my_function(arg):
    counts = {};
    for id in arg:
        if id in counts:
            counts[id] +=1;
        else:
            counts[id] = 1;
    for keys, hits in counts.items():
        if hits == 1:
            return keys;

def my_function2(arg):
    id = 0;
    for ids in arg:
        id ^= ids;
    return id;
arg1=[0,1,2,3,2,3,0,1,5,10,5,500,500]
print(my_function(arg1))
print(my_function2(arg1))
