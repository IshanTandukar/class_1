#paragraph = "I am learning python and it is a great language"
#print(paragraph.find('l'))
#print(paragraph.find('q'))
#

#capitalize using for loop
my_string = "Hello world from new python script"
#for i in my_string:
 #   print (i)#
 #   if i=="l"  :
 #       i=i.upper()

#strip
my_string1="           Hello from new python"
print(my_string1.strip())



#formatting a string
a = "Ram Bahadur"
#b = f"mero nam {a} haina"
c = f"mero naam {a} ho {my_string}"
b = "mero nam {2} ho {2}, {1}, {2}".format(a,my_string,c)

print(b)
print(c)

#replacing a string
my_string = my_string.replace("Hello","bye")
print(my_string)

#counting number of string
my_string2="aaabcdefaaaabababababaababaabaabbba"
my_string2=my_string2.count("ab")
print(my_string2)