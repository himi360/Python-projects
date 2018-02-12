#Mihrete Samuel
#Question 1
# Midterm 2
#11/5/17

def encrypt(plaintext, password):
    new_word = ""
    count = 0
    plaintext = plaintext.upper()
    if password != password.lower():
        print("ERROR: Password must be all lowercase letters")
    for i in range(len(plaintext)):
        if ord(plaintext[i]) < 65 or  ord(plaintext[i]) > 90:
            continue
        if count == len(password):
            count = 0
        shift = ord(password[count])
        shift -= 97
        num = ord(plaintext[i])
        if num + shift > 90:
            new_num = (num + shift) - 26
        else:
            new_num = num + shift
        new_letter=chr(new_num)
        new_word+=new_letter
        count += 1
    return new_word


print(encrypt("OB!JECT!", "inst"))
print(encrypt("DIMITRI", "pass"))
