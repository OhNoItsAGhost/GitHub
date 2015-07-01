for x in range (1,101):
    
    if x%3 == 0 and x%5 == 0:
        print ("Foobar"), 
    elif x%3 == 0:
        print ("Foo"),
    elif x%5 == 0:
        print ("Bar"),
    else:
        print (x),

print ""

'''
It first checks of the number is divisible by both, then by just one of two. If it doesn't satisfy either, it just prints the number
'''
    