integer = 1
floating = 2.3
string = '33'

print("Type of integer is:", type(integer))
print("Type of floating is:", type(floating))
print("Type of string is: ", type(string))

print()

integer = float(integer)
floating = str(floating)
string = float(string)

print("Type of integer is:", type(integer))
print("Type of floating is:", type(floating))
print("Type of string is: ", type(string))