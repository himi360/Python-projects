#Mihrete Samuel
#10/16/17
#Homework 6
#Question 1



def greatest_Pair(x):
    max = 0
    z=0
    for i in range(len(x)-1):    #Makes sure it doesnt go out of bounds
        sum = x[i] + x[i+1]
        if sum > max:
            max =sum      #change what max is equal to everytime its bigger than before
            z=i
    return z     #return place found



print(greatest_Pair([5,6,6,7,3834038408]))



