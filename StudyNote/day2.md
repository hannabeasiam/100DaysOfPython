### Exception
- [D2_suggestinator.py](D2_suggestinator.py)
- [D2_purchase_ticket.py - wrap exception with loop](D2_purchase_ticket.py)


### While loop 
- [D2_password_checker.py](D2_password_checker.py)
* good for condition based looping 
* [D2_password_checkers](D2_check_please.py)

**sys** this module provides access to some variables used or maintained by the interpreter and to functions that
interact strongly with the interpreter. It is always available [Learn More](https://docs.python.org/3.6/library/sys.html#sys.exit) 
> sys.exit([arg]) 
> exit from Python. This is implemented by rasing the SystemExit exception, so clean up actions specified by finally
clauses of try statements are honored, and it is possible to intercept the exit attempt at an outer level.


### for loop
* traditionally used when you have a block of code which you want to repeat a fixed number of times. The Python for
statement iterates over the members of sequence in order, executing the block each time. Contrast the for 
statement with the "while loop", used when a condition needs to be checked each iteration, or to repeat a block of code 
forever. [Learn More](https://wiki.python.org/moin/ForLoop) 


### List
> String are immutable, cannot be changed, but Lists are mutable. Can be changed. String methods return a brand new 
string entirely since they can't change. List method do not return a new list. Instead, they modify existing list.

```python
bool(["me", "myself", "I"])
```
>This following list coerce to True : any non-empty list is True

- indexing in Python is Zero based
- You can access a specific character on a String by using an index, but you cannot change it.

**PEP8 When to use trailing commas?** 
>  The main advantages are that it makes multi-line lists easier to edit and that it reduces clutter in diffs.
Trailing commas are usually optional, except they are mandatory when making a tuple of one element (and in Python 2 they 
have semantics for the print statement). For clarity, it is recommended to surround the latter in (technically redundant)
 parentheses. [Learn More](https://www.python.org/dev/peps/pep-0008/#when-to-use-trailing-commas)
 