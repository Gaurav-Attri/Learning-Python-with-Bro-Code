name = "gaurav"

string_length = len(name)
print("The length of the string " + name + " is: " + str(string_length))

print()

find_result = name.find('G') # find method return -1 if the character is not found in the string
print("The index of the character 'G' is: " + str(find_result))

print()

capitalized_string = name.capitalize()
print(capitalized_string)

print()

uppercassed_string = name.upper()
print(uppercassed_string)

print()

lowercassed_string = name.lower()
print(lowercassed_string)

print()

str1, str2, str3 = "123", "Gaurav", "12G"
print("str1 is a digit string? ", str1.isdigit())
print("str2 is a digit string? ", str2.isdigit())
print("str3 is a digit string? ", str3.isdigit())

print()

print("str1 is a alpha string? ", str1.isalpha())
print("str2 is a alpha string? ", str2.isalpha())
print("str3 is a alpha string? ", str3.isalpha())

print()

print("There are", name.count('a'), "a's in the string 'gaurav'")

print()

print("if you replace all a's in the string", name, "with e's then it is", name.replace('a', 'e'))