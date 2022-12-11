matA=[[9,8,6],
      [5,7,5],
      [3,1,3]]
matB=[[6,7,8],
       [9,9,9],
       [5,6,7]]       
matC=[[0,0,0],
       [0,0,0],
       [0,0,0]]


for i in range(len(matA)):
    for j in range(len(matA[0])):
        
        for k in range(len(matA)):
            matC[i][j] = matC[i][j] + matA[i][k] * matB[k][j]
        




for i in matC:
    print(i)            

