p = (1,2,3,4,5)

# Using Star Expression to leave first and last value
f, *mid, l = p

print(sum(mid))



# Using Star Expression to leave last two values
val1, val2, val3, *val = p
print(val1)
print(val2)
print(val3)
print(val)



# Using Star Expression to leave first one and last two values
first, *val, sec_last, last = p
print("first value is " +str(first), "but sum of star values are " + str(sum(val)))


contacts = [
('IITB', 'dinesh', 986768, 67689734),
('IITBHU', 'vivek', 89696895),
('IITKanpur', 'motuuu', 4, 78796868),
('IITB', 'pushpak'),
]

for tag, *person in contacts:
    name, *numbers = person
    print(name, 'is having', len(numbers), 'phone numbers')
    
