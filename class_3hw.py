my_list = [1,2,"hello",4.5]         #Giving values in a list called my_list
print(my_list)


my_list.append("bye bye")       #Adding element in th list
print(my_list)

my_list.pop(3)                  #Popping out the 4th element in the list
print(my_list)

my_list.pop()                   #Poppin gout the last element in the list
print(my_list) 

print(len(my_list))              #Length of the list

my_list.append(5) 
my_list.append(5)
my_list.append(5)
my_list.append(5)
print(my_list)
print(my_list.count(5))           #Counting the number of elements present in the list

my_list.insert(1,"Yo")            #Inserting the element in the provided order in the list
print(my_list)

print(my_list[-1])                #Printing the list from reverse order