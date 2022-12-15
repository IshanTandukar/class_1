#Tuple 

my_tuple = (1,2,3,"Hello","BYEBYE")
#f#or i in my_tuple:
#    print(i)

my_list = list(my_tuple)  #Listing tuple
print(my_list)


my_list.append("ereeeeeeeeeeh")  
my_list.append("ereeeeeeeeeeh") #inserting an element
print(my_list)

tup = tuple(my_list)
print(tup)
print(tup.count("ereeeeeeeeeeh"))  #Counts the number of repetitions of given element



#Dictionary
dictionary = {'a':'1','b':'2','c':'None'}   #a vaneko key ra 1 vaneko value ---key jaile pani string ma rakhni

for k,v in dictionary.items():
    print(k,v)

print(dictionary.values())
print(dictionary.keys())
print(dictionary.items())
print(dictionary["c"])
