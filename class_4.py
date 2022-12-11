#my_list=[1,2,3,4,5,"hey",7,"suiiii",9,"python",11]
#my_lis1=[0,1,2,3,4,5,6,7,8,9,10]
#sum=0
#for element in my_list:
#    if type (element) == int:
 #       sum += element
 #       print (sum)

#for i in range(len(my_list)):
#    print(my_list[i])
    

#my_list1 = my_list[0:-1:2]
#print("first list",my_list1)    
#    
#my_list1 = my_list[::2]
#print("Second list",my_list1)    
#        
#my_list1 = my_list[2:5:2]
#print("Third list",my_list1)    
#
#my_list1= my_list1[1:9:2]
#print("Fourth list",my_list1)        
#
#my_list2=my_list[-1:-5:-2]
#print(my_list2)
    



mat_A=[[1,2,3],
       [4,5,6],
       [7,8,9]]
mat_B=[[1,0,0], 
       [0,1,0], 
       [0,0,1]]

mat_C=[[0,0,0],
       [0,0,0],
       [0,0,0]]       


for i in range( len( mat_A )):
    for j in range( len( mat_B )):
        mat_C[i][j]= mat_A[i][j] +mat_B[i][j]

for i in mat_C:
        print(i)


