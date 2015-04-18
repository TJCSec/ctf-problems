# TJCTF Problems

In order to prepare for TJCTF, we need to get all problems into the proper format. This requires two main things, a manifest and a grader. First the grader, in the root directory of your problem, create a folder named `grader/`. Inside `grader/`, create a file named `grader.py`. This should be a python file with a function grade. For example, a problem with only one correct answer would look like

```python
def grade(arg, key):
  if "this_is_the_flag" in key:
    return True, "Correct"
  else:
    return False, "Incorrect"
```

As you can see, it should return a tuple with the first item being the "correctness" of the problem, and the second being a message to the player after they submit. Now, again in the root directory of your project create a file named `problem.json` it should be of the format:

```json
{
  "name": "<<Problem Name>>",
  "score": <<this will be finalized after testing>>,
  "category": "<<Crypto || Web || Binary || Misc>>" ,
  "grader": "<<foldername>>/grader.py",                   //note the absence of the /grader/ directory. This is INTENTIONAL
  "description": "Problem text. HTML can be used here.",
  "threshold": 0,                                         //we will not use these unless we want to have multiple "levels"
  "weightmap": {},
  "hint": "Hint text. HTML can be used here"
}
```

If you have any questions, reference https://github.com/picoCTF/picoCTF-Platform-2
