#Mihrete Samuel
#10/2/17
#Homework 5

def consChars(file_name):
    count =0    #Begining of counter
    read_file = open(file_name, 'r')
    write_file = open('consecutives.txt', 'w')
    for i in read_file:
        i=i.rstrip()  #This helps remove whitespace between strings
        if helper(i) == True:
            write_file.write(str(i) + '\n')  #Adds words w/ repeating letters to new file
            count +=1
    print("The total number of words is: " + str(count))


#Helper function helps determine if an individual word has repeating letters, returns true if so
def helper(word):
    word = word.lower()
    for i in range(len(word)):
        if i == 0:
            continue
        if word[i]==word[i-1]:
            return True
    return False


consChars('words.txt')


