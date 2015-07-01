def removeDup(words):
    
    mylist = []
    
    for w in words:
        if w not in mylist:
            mylist.append(w)
    return mylist
    
wo =  ['one', 'one', 'two', 'three', 'three', 'two']

fin = removeDup(wo)

print fin

'''
Fairly straightforward. Given an array argument, The function loops through the array and then checks each value to see if it exists in our new array. If it doesn't, it gets added

prints out the final no duplicates array at the end
'''