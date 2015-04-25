import subprocess
def c(b):
    for char in b:
        if char not in "0123456789":
            return False
    d = 0
    for char in b[:-1:2]:
        d += ord(char) - ord("0")
    for char in b[1:-1:2]:
        d += (ord(char) - ord("0")) * 3
    e = 10 - d % 10
    f = 0
    for i in range(5):
        f += ord(b[i]) - ord("0")
    g = 1
    for i in range(1, 5):
        g *= ord(b[i]) - ord("0")
    h = ord(b[1]) - ord("0")
    l = ord(b[2]) - ord("0")
    m = ord(b[3]) - ord("0")
    n = ord(b[4]) - ord("0")
    if b[5:11] != "914323":
        return False
    if abs(h + l - m) != 1 or abs(h + l - n) != 1:
        return False
    if "0" not in b:
        return False
    if ord(b[-1]) - ord("0") != e:
        return False
    if f != 21:
        return False
    if g != 480:
        return False
    return e == 9

def grade(arg, flag):
    if c(flag):
        return True, "You are very good at the compute box codes"
    else:
        return False, "Wrong"
    """
    if '0528691432349' in flag or '025869143231899' in flag:
        return True, 'You either know how to bytecode or found a program that does'
    else:
        return False, 'Incorrect'
    """
