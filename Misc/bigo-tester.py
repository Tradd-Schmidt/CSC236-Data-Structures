'''This program is designed to explore big o notion and algorithms by Dr. Jan Pearce of Berea College
    Licensed under a Creative Commons Attribution-Share Alike 3.0 United States License'''

def looponconstant(n):
    ''' looponconstant demonstrates O(1) behavior
    pre: n is a positive integer
    post: returns an integer count of the number of iterations'''

    count = 0
    for i in range(1):
        count=count+1   #we are interested in how often this line executes
    return count

def looponconstant2(n):
    ''' looponconstant2 also demonstrates O(1) behavior
    pre: n is a positive integer
    post: returns an integer count of the number of iterations'''

    count = 0
    for i in range(10):
        count=count+1   #we are interested in how often this line executes
    return count

def loopwn(n):
    ''' loopwn demonstrates O(n) behavior
    pre: n is a positive integer
    post: returns an integer count of the number of iterations'''

    count = 0
    for i in range(n):
        count=count+1   #we are interested in how often this line executes
    return count

def loopmanycount(n):
    ''' loopmanycount also demonstrates O(n) behavior
    pre: n is a positive integer
    post: returns an integer count of the number of iterations'''

    count = 0
    for i in range(n):
        count=count+10   #we are interested in how often this line executes
    return count

def sequential(n):
    ''' sequential also demonstrates O(n) behavior
    pre: n is a positive integer
    post: returns an integer count of the number of iterations'''

    count = 0
    for i in range(n):
        count=count+1   #we are interested in how often this line executes    for i in range(n):
    for i in range(n):
        count=count+1   #we are interested in how often this line executes
    return count

def nestedwconstant(n):
    ''' twonested demonstrates O(n**2) behavior
    pre: n is a positive integer
    post: returns an integer count of the number of iterations'''

    count = 0
    for i in range(n):
        for j in range(10):
            count=count+1   #we are interested in how often this line executes
    return count

def twonested(n):
    ''' twonested demonstrates O(n**2) behavior
    pre: n is a positive integer
    post: returns an integer count of the number of iterations'''

    count = 0
    for i in range(n):
        for j in range(n):
            count=count+1   #we are interested in how often this line executes
    return count

def threenested(n):
    ''' loopwn demonstrates O(n**3) behavior
    pre: n is a positive integer
    post: returns an integer count of the number of iterations'''

    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                 count=count+1   #we are interested in how often this line executes
    return count

def halving(n):
    ''' twonested demonstrates O(log(n)) behavior
    pre: n is a positive integer
    post: returns an integer count of the number of iterations'''

    count = 0
    loopcounter=n
    while (loopcounter>1):
        count=count+1   #we are interested in how often this line executes
        loopcounter=loopcounter//2
    return count

def raw_input(strng):
    x = input(strng)
    return x

def main():

    strn=raw_input("Please enter n: ")
    n=int(strn)
    while n>0:
        print ("for n = "+strn+":")
        print ("\tlooponconstant("+strn+") = "+str(looponconstant(n)))
        print ("\tlooponconstant2("+strn+") = "+str(looponconstant2(n)))
        print ("\tloopwn("+strn+") = "+str(loopwn(n)))
        print ("\tloopmanycount("+strn+") = "+str(loopmanycount(n)))
        print ("\tsequential("+strn+") = "+str(sequential(n)))
        print ("\tnestedwconstant("+strn+") = "+str(nestedwconstant(n)))
        print ("\ttwonested("+strn+") = "+str(twonested(n)))
        print ("\tthreenested("+strn+") = "+str(threenested(n)))
        print ("\thalving("+strn+") = "+str(halving(n)))

        strn=raw_input("Please enter another n (entering -1 to stop): " )
        n=int(strn)

main()
