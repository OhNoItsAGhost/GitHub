
current = 1

for x in range(1, 31):
    if x%6 == 0:
        print ("")
        current = current + 1
    else :
        print (current),
        
'''
Using one loop. Every 6 steps I just move the print to a new line and also increment the counter

In the steps between the intervals, i just print the current value without pushing to a new line
'''