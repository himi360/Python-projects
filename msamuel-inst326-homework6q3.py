#Mihrete Samuel
#10/16/17
#Homework 6
#Question 3


def intersection(x,y):
    list3 = []
    for i in range(len(x)):  #for loop from 0 to length of x minus 1
        for z in range(len(y)):   #for loop from 0 to length of y minus 1
            if x[i] == y[z] and x[i] not in list3:  #Makes sure number didn't pop up already
                list3.append(x[i])
    return list3


print(intersection([2,3,7,7,7,7,5,5,5,55,5,5], [7,2,7,7,7,7,77,3]))






