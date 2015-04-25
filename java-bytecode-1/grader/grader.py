def grade(arg, flag):
    if '0528691432349' in flag or '025869143231899' in flag:
        return True, 'You either know how to bytecode or found a program that does'
    else:
        return False, 'Incorrect'
