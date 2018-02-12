#Mihrete Samuel
#10/16/17
#Homework 6
#Question 2


def isSorted(a):
    i =0

    if len(a) == 0:   #handles edge case of none
        return None

    elif len(a) == 1:   #handles edge case of 1 input
        return True

    elif a[i] < a[i + 1]:     #Checking the ascending case
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                return False
        return True


    elif a[i] > a[i + 1]:     #Checking the descending case
        for i in range(len(a)-1):
            if a[i] < a[i+1]:
                return False
        return True



print(isSorted([5]))



