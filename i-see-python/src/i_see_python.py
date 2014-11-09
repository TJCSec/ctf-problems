def scramble(x):
    return [chr(i) for i in x]

def flippity(x):
    return "".join(["".join(i) for i in zip(x[1::2], x[0::2])])

def go():
    password = raw_input("Password: ")
    if len(password) != 8:
        return False
    if ord(password[1]) != 52  or \
       ord(password[3]) != 36  or \
       ord(password[0]) != 112 or \
       ord(password[7]) != 100 or \
       ord(password[6]) != 114 or \
       ord(password[2]) != 115 or \
       ord(password[5]) != 48  or \
       ord(password[4]) != 119:
           return False

    return flippity(scramble([106, 116, 116, 99, 123, 102, 121, 112, 104, 116, 110, 111, 105, 95, 95, 115, 117, 102, 125, 110]))

print(go())
