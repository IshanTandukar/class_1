#Dictionary 
my_dict = {1:"one","two":2}
 
my_dict ["three"] = 3               #Adding keys and values in dictionary

my_dict ["two"] = 0                 #changing values

a = (my_dict ["two"] == 0)          #changing values of keys
print (a)   

my_dict.pop(1)                      #Popping out keys
print(my_dict)

my_dict ["one"] = 1
print(my_dict)

my_dict.popitem()                   #Mechanism of Last In First Out in pop items
print(my_dict)

print(len(my_dict))                 #Length of dictionary


my_dict.update({"four":4})          #Updating the dictionary
print(my_dict)

print(my_dict.get("two"))           #Getting value of key two


Sagarmtha = {                       #Nested dictionary
    "Education Department" : {
        "BCT" : {
            "HOD" : "Bharat Bhatta",
            "No_of_students" : 48
        },

        "BCE" : {
            "HOD" : "Sudip Lamsal",
            "No_of_students" : 48

        }
    },

    "Admin Department" : {
        "Accounts" : {
            "HOD" : "Chatturbhujha",
            "No_of_clients" : 60
        }
    }
}

print(Sagarmtha["Education Department"]["BCT"]["HOD"])       #Output in nested dictionary
print(Sagarmtha["Admin Department"]["Accounts"]["HOD"])
print(Sagarmtha["Education Department"]["BCE"]["No_of_students"])    

