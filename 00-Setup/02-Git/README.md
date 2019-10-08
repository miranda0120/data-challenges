Let's recap the `git` commands you need to remember to work on the challenges during the bootcamp.

## Status

First, let's make sure that our working directory is **clean**:

```bash
git status
```

If you get the following result, then all good, you can start working on this challenge:

```text
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
```

If you don't get this message, you need first to commit / clean some other challenges before you can start. Do not hesitate to raise a ticket to get some help from a TA over the first few days. `git` can be hard, so please ask!

## First commit

Let's create a Python file:

```bash
touch today.py
```

Open this file in your text editor and declare + implement a function `my_name_is` which takes no parameter and returns a `str`: your GitHub nickname. Run `make` until one test passes (no need for the second one to be successful).

```text
tests/test_git.py::TestGit::test_hi_my_name_is PASSED
tests/test_git.py::TestGit::test_my_buddy_is   FAILED
```

Good, you made some progress. It's time to pause and save your progression like a checkpoint!

```bash
git add today.py
git commit -m "Implement my_name_is function"
git push origin master
```

Kitt should pick up the change and show you a 50% progress. Good job!

## Second commit

Let's start solving the second test. To do so, you need to declare + implement a function `my_buddy_is` which takes no parameter and returns a `str`: Your buddy's GitHub nickname.

You can use this useful command to check what has changed in the file:

```bash
git diff
```

If you are satisfied, you can now commit & push to GitHub:

```bash
git add today.py
git commit -m "Implement my_buddy_is function"
git push origin master
```

## Making `pylint` happy

At this point of the challenge, you should have 3 style errors:

```text
today.py:1:0: C0114: Missing module docstring (missing-module-docstring)
today.py:1:0: C0116: Missing function or method docstring (missing-function-docstring)
today.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
```

You are missing [docstrings](https://www.python.org/dev/peps/pep-0257/). One for the module, and one for each function. A docstring gives context / documentation to a module or function.

To fix the first error, add a docstring at the **first line** of `today.py`:

```python
"""A module computing buddy pair names for the day"""
```

Run `make` again, you should have one less style error.

Repeat this by adding a [one-line docstring](https://www.python.org/dev/peps/pep-0257/#one-line-docstrings) for the two functions.


When you are done, time to perform the third commit of the challenge:

```bash
git diff
````

```bash
git add today.py
git commit -m "Fix style issues, should get a 'Good Style' now :pray:"
git push origin master
```

## Conclusion

You now know how to navigate Kitt, position yourself on a challenge, open it in a text editor and work on it, switching to the terminal to run `make` and some git commands. Congratulations!

The day is now over, check with a TA but you should be able to leave early today. If you want to stay a bit, you can:

- Finish the [Python CodeCademy track](https://www.codecademy.com/learn/learn-python-3) if not already done
- Start reading [Learn Enough Command Line to Be Dangerous](https://www.learnenough.com/command-line-tutorial/basics), as a developer can't know too much of command-line magic 😉