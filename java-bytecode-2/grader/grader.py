def grade(arg, flag):
    if 'readclassy' in flag:
        return True, 'You really are classy'
    else:
        return False, 'Incorrect'