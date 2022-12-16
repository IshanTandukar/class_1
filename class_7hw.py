#Adding two matrices using list comprehension 

matA = [[2,3,4],
         [3,1,3],
         [7,8,9]]

matB = [[4,7,8],
        [7,7,7],
        [2,1,8]]

matC=[[0,0,0],[0,0,0],[0,0,0]]

result = [[matA[i][j] + matB[i][j] for j in range (len(matA[0]))] for i in range (len(matA))]
for r in result:
        print (r)