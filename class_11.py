price_of_item = {
            'apple': 120,
            'banana': 330,
            'orange': 210,
            'pear': 210,
            'grape': 410,
            'pineapple': 560,
            'strawberry': 770,
            'watermelon': 660
}


# item_dict = {}               #Empty Dictionary
# #for k,v in price_of_item.items():
#     # print(k,v)
#    #v = v + 0.13 * v
#     # print(k,v)
#     #price_of_item.update({k:v})    #Updating using update
#     #item_dict[k] = v             #Updating dictionary


# #print(item_dict)
# #print(price_of_item)    #for update

# item_dict = {f"{k}'s new price" : v + v * 0.13 for k , v in price_of_item.items()}         #Same operation but in same line  (Dictionary Comprehension)
# print(item_dict)

# item_dict = {k : v + v * 0.13 for k , v in price_of_item.items()}         #Same operation but in same line without formatting
# print(item_dict)

def get_price_of_items(item , tax_rate = 0.13) : 
    return {k : v + v * tax_rate for k , v in item.items()}

print(get_price_of_items(price_of_item , 0.15))     #Call by changing to 15%
print(get_price_of_items(price_of_item ))           #Default argument call


#def first(x):  #Define function
 #   f = x*x+ 5*x + 1
 #   print(f)
#x = int(input("Enter value:"))
#first(x)    #call


#def calculate_f(x):
 #   return x**2 + 5*x + 1

#print(calculate_f(1))

f = lambda x : x**2 + 5 * x + 1
print(f(1))

a = lambda name : name + "l"
print(a("bhupin"))

t = lambda x,y : x**2 + 5*x*y + 1
print(t(2,3))


