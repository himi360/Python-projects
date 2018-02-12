#Mihrete Samuel
#11/02/17
#Homework 7
#Question 2


def assignLetters(grades):

    dict = {'A':0, 'B':0, 'C':0, 'D':0, 'F':0 }  #Template for new dictionary created, 0 as placeholder for each value
    for i in range(len(grades)):
        if not 0<=grades[i] <=100:
            return ("ERROR: Values in list must be between range 0-100")
        if 0 <= grades[i] <=65:   # ranges for different grades A-F
            dict["F"] +=1   #If fulfilled, add 1 to the value
        elif 66 <= grades[i] <=74:
            dict["D"] += 1
        elif 75 <= grades[i] <=79:
            dict["C"] += 1
        elif 80 <= grades[i] < 89:
            dict["B"] += 1
        elif 90 <= grades[i] <= 100:
            dict["A"] += 1
    return dict         #return new dictionary


print(assignLetters([94,87,65,14,29,62,98,85,88]))

