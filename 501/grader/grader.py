def grade(arg, key):
    if "totp_is_best_otp" in key:
        return True, "Correct"
    else:
        return False, "Incorrect"
