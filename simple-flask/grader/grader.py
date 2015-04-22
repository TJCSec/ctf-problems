def grade(arg, key):
    if "do_it_right_dont_store_passwords_in_the_session" in key:
        return True, "Correct"
    else:
        return False, "Incorrect"
