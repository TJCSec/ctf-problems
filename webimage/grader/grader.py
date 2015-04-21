def grade(arg, key):
  if "bashing_jpgs" in key.lower():
    return True, "Nice Job!"
  else:
    return False, "Nope, Incorrect."
