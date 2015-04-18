def grade(arg, key):
  if "pitassembly" in key:
    return True, "Nice Job!"
  else:
    return False, "Nope, Incorrect."
