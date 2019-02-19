x = True
y = False
z = False

# False OR True == True
# True OR False == True
# True OR True == True
# False OR False == False

# True AND True = True
# True AND False = False
# False AND True = False
# False AND False = False

# False XOR True == True
# True XOR False == True
# True XOR True == False
# False XOR False == False

if not x or y:
    # False or False == False
    print(1)
elif not x or not y and z:
    # False or True and False == False
    print(2)
elif not x or y or not y and x:
    # False or False or True and True == True
    print(3)
else:
    print(4)
    