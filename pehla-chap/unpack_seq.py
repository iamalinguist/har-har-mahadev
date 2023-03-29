p = (1,2,3)

# unpacking using variables
# following x, y, z can be given as list [x,y,z], tuple(x,y,z) or just simple x,y,z
x, y, z = p 
print(x, y, z)

# throwing some variables
_, y, _ = p
print("only printing one value", y)

# unpacking specific value is done by using index
a = p[1]
print (a)

# printing 
size_of_p = len(p)
print("Size of p is " + str(size_of_p )) # print by concatenation
print(f"New Size of p is {size_of_p}") # print by f-value
print("New New Size of p is", size_of_p ) # print by comma method
