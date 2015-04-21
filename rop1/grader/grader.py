def grade(arg, key):
    if "isnt_ret_a_nice_instruction" in key:
        return True, "You really are oriented towards returns"
    else:
        return False, "Incorrect"

