row=int(input("enter the rows of the matrice"))
coloumn=int(input("Enter the coloumn of the matrice"))
matrice=[]
rowan=[]
for i in range(0,row):
    #no. of iterations as the no. of rows will happen

    for j in range(0,coloumn):#in a row no. of iterations as a coloumn will collect 1 element at a time
        element=int(input("Enter the element"))
        rowan.append(element)# packing process to make a row set

        # after no. of iterations as coloumn is over it will come out of loop2
        
    print("one row completed")
    matrice.append(rowan) #one row that we made is added to matrice
    
    rowan=[]# rowan is emptied, or else our matrice will be a list!
    
    # the next iteration of loop 1 will take place
    
for i in matrice: 
    print(i)
