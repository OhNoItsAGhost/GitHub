def evens(n):
    count = 0
    for x in range(0,n+1):
        if x%2 == 0:
            count = count + 1
            
    print count
            
evens(15)

'''
If the remainder is 0 when the number is divided by 2, add to the count

Based on the given example, I assume 0 counts. 
'''        