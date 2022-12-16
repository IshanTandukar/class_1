for n in range(1,100):                #Use of for loop
    count = 0
    for i in range( 1 , n+1) :
        if n%i == 0:
            count = count + 1

    if count == 2:
        print(n)