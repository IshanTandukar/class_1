my_string = "Hello World from our first python"

next_string = '''This is a "multi-dimensional" commment'''
print(next_string)

#print("This is a "muli line" comment")(error occurs)

my_string1=my_string[2:5:2]
print(my_string1)

my_string2=my_string[::2]
print(my_string2)

my_string3=my_string[:-1]
print(my_string3)

my_string4=my_string[::-1]
print(my_string4)

my_string5=my_string[::3]  
print(my_string5)

my_string6=my_string.index("H")
print(my_string6) 

my_string7=my_string.index("Hello")
print(my_string7)

my_string8=my_string.index(" ")
print(my_string8)  

my_string9=my_string.index("")
print(my_string9)  