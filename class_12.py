
# f = lambda x : x**2 + 5*x + 1
# print(f(4))

# my_list = [1,2,3,4,5,6,7,8,9,10]
my_list = (1,2,3,4,5,6,7,8,9,10,11) 
my_tuple = (2,4,6,8,10)     #This is tuple
next_list = list(my_list[::-1])
jpt_list = list(zip(my_list,next_list))
lis = [11,11,11,11,11,11,11,11,11]
jpt_list = list(zip(my_list, next_list, lis))

print(jpt_list)
print(next_list)

def sum_of_num(a,b,c,d):
    return a + b + c + d

print(sum_of_num(1,2,3,5))
sum = map(sum_of_num, my_list, next_list, lis, my_tuple)               #Using map funstion
print(list(sum))

NEWLIST = []
for index in range (len(my_list)):                      #Adding two lists using loop
    NEWLIST.append(my_list[index] + next_list[index])
# print(NEWLIST)    

NEW_LIST = list(map(lambda x,y : x + y, my_list, next_list))
print(NEW_LIST)


def evenodd(x):  #Define function
    if (x%2 == 0):
        print('even')
    else:
        print('odd')  
 
x = int(input("Enter value:"))
evenodd(x)    #call

#Filter function
new_list = list(filter(evenodd, my_list))
print(new_list)

new_list = list(filter(lambda x : x % 2 != 0, my_list ))
print(new_list)