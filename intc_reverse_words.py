def reverse_words(arg):
    # if len(arg)%2==0:
    #     midpoint = len(arg)/2;
    # else:
    #     midpoint = len(arg)/2 - 1;
    # stor = arg[0];
    # arg[0] = arg[-1];
    # arg[-1]=stor;
    # print(midpoint);
    #
    # for ii in range(1,int(midpoint)):
    #     stor = arg[ii];
    #     arg[ii] = arg[-ii-1];
    #     arg[-ii-1] = stor;

    ind1 = 0; #track start of words

    reverse_chars(arg,0,len(message)-1);

    for ii in range(len(arg)+1):
        if (ii==len(arg)) or (arg[ii]==' '):
            reverse_chars(arg,ind1,ii-1);
            ind1 = ii+1;

def reverse_chars(arg, ind1, ind2):
    print('reversing %d, %d' %(ind1, ind2))
    while ind1 < ind2:
        arg[ind1], arg[ind2] = arg[ind2], arg[ind1];
        ind1 +=1;
        ind2 -=1;

message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]
# reverse_chars(message,0,len(message)-1)

reverse_words(message);
print(''.join(message));
