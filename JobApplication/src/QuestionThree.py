import random

xMin = 1
yMin = 1
zMin = 1

xMax = 6
yMax = 6
zMax = 6

aMin = xMin + yMin + zMin
aMax = xMax + yMax + zMax

print "The range of possible values would be between the combined minimum values and combined max values of x, y and z"
print "Therefore : "
print "Minimum for a is : " + str(aMin)
print "Maximum for a is : " + str(aMax)

print "As an example : "
print " "

x = random.randint(1,6)
y = random.randint(1,6)
z = random.randint(1,6)

print "x = " + str(x)
print "y = " + str(y)
print "z = " + str(z)

print " "

print "This means a = " + str(x + y + z)

'''
I tried making this program very versatile because I didn't fully understand the question

I used 6 different variables for the min and max ranges because if the user wanted to change the range of either x, y or z, then they could just edit one number
Whereas if I had a universal min or max value, you would have to create a new variable

I also ran an example
'''
