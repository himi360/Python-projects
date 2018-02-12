file = open('words.txt', 'r')
for i in file:
    i = i.rstrip()
    print(i)


file = open('words.txt', 'r')
count =0
for i in file:
    count += 1
print(count)


def more_than_twenty():
    file = open('words.txt', 'r')
    count = 0
    for i in file:
        i = i.rstrip()
        if not len(i) > 20:
            continue
        print(i)

more_than_twenty()

def more_than_twenty():
    file = open('words.txt', 'r')
    count =0
    for line in file:
        if (len(line.rstrip()) > 20):
            print(line)
            count+= 1
        print(count)



def is_abecedarian(word):
    word = word.lower()
    for i in range(len(word)):
        if i ==0:
            continue
        if(word[i] < word[i-1]):
            return False
    return True


print(is_abecedarian("dog"))

