
def consecSum(theArray, theSize):
    
    tot = len(theArray) 
    tot = tot - theSize
    
    largest = 0
    indexP = 0
    tempLargest = 0
    
    ''' Initialize all the variables. 
    largest will be used to store the largest sum we have found
    indexP stores the starting index for the largest sum
    tempLargest is used to test if a sum is larger than the currently stored largest sum  '''
    
    for x in range(0, tot+1):
        tempLargest = 0
        ''' Rest the temp largest so we can retest for the new starting index '''
        for y in range (x,x + theSize):   
            ''' Runs the loop from the current index. The number of times it runs is equal to the size of groups as stated by the user '''
            tempLargest = tempLargest + theArray[y]
        if tempLargest > largest:
            largest = tempLargest
            indexP = x
    
    print "The largest sum was : " + str(largest)
    print "Starting at index : " + str(indexP)
    

n = 2
m = [1,1,1,1,1,1,1,2]

consecSum(m, n)
