def grade(arg, key):
  if "brainpyd" == key.lower():
    return True, "Nice Job!"
  else:
    return False, "Nope, Incorrect."
