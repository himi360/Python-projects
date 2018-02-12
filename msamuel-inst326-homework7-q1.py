#Mihrete Samuel
#11/02/17
#Homework 7
#Question 1


def histogram(grades):
    results= ""   #Make new string
    failing = "0-69: "
    c = "70-79: "
    b = "80-89: "  #This creates the template for the string that will be concatenated
    a = "90+ "

    for i in range(len(grades)):
        if not 0<=grades[i] <=100:
            return ("ERROR: Values in list must be between range 0-100")
        if 0 <= grades[i] <=69:  #Ranges for different grades from A-F
            failing += "*"
        elif 70 <= grades[i] <=79:
            c += "*"
        elif 80 <= grades[i] < 89:
            b += "*"    #If range fulfilled add a *
        elif 90 <= grades[i] <= 100:
            a += "*"

    failing += "\n"  # \n adds a space after the string, helps create mulitline string
    c += "\n"
    b += "\n"
    a += "\n"

    return(failing + c + b + a)  #After adding a space after every string, concatenate them all together


print(histogram([94,87,65,14,29,62,98,85,88]))

