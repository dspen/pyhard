def my_function(arg):
    # write the body of your function here
    ind=[];
class FibClass(object):
    def __init__(self):
        self.memo = {}; #dict creation

    def fib(self,n):
        if n<0: raise ValueError;
        if n in self.memo:
            return self.memo[n];
        elif n==0: result = 0;
        elif n==1: result = 1;
        else:
            result = self.fib(n-2)+self.fib(n-1);

        self.memo[n] = result;

        return result;
def fib2(n):
    if n<0: raise ValueError;
    if n in [0,1]:
        return n;
    else:
        prev2 = 0;
        prev = 1;
        for ii in range(n-1):
            curr = prev + prev2;
            prev2 = prev;
            prev = curr;
        return curr;

    #for ii in range(2,int(arg)+1):
        #ind.append(ind[1]+ind[-2]);

# run your function through some test cases here
# remember: debugging is half the battle!
#print my_function(5)
n=1000;
obj = FibClass();
print(obj.fib(n)) #max of 1000 recursion depth!
print(fib2(n))
# print fib(5)
