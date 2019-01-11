### Data Structures
#### 1. More on Lists 
- [join,split](D2_list.py) 
- [shopping list](D3_shopping_list.py)

- list.append(x) 
> Add item to the end of the list
- list.extend(List)
> Extend the list by appending all the items in the given List
- list.insert(i,x)
> Insert an item at a given position. i = index 
- list.remove(x)
> Remove the first item from the list whose value is x. error if x is not exist in the List
- del list[i]
> removing items from iterable or deleting whole variables
- list. pop([i])
> Remove the item at the given position index i, and return it. I index is not specified, list.pop() will 
removes and returns the last item in the list. 
- list.index(x)
> return the index in the list of the first item whose value is x. error if x not exist in the list
- list.count(x)
> return the number of times x appears in the list
- list.sort()
> sort the items of the list, in place
- list.reverse()
> reverse the elements of the list, in place.


#### 2. Using Lists as Stacks
**Stacks** "last-in, first-out"  
- list.append() : where the last element added
- list.pop()  : last element first out

#### 3. Using Lists as Queues
**Queue** "first-in, first-out"  However, lists are not efficient for queue purpose. While appends and pops from the 
end of list are fast, doing insert or popleft from the beginning of the list is slow **(Because all of other elements 
have to be shifted by one)**
> To implement a queue, use **collection.deque** which was designed to have hast appends and pops from both ends.
```python
from collections import deque
queue = deque(["A", "B", "C"])
queue.append("D") # D added last
queue.append("E") # E added last
queue.popleft() # First A removed
queue # deque(["B", "C", "D", "E"])

```

### Pythonic loops 

#### Call a function until sentinel value, Distinguish multiple exit points in loops...
 **[Very helpful video](https://www.youtube.com/watch?v=OSGv2VnC0go&ab_channel=NextDayVideo)**
#### There is no numerical for loop in python
```python
# There is no such concept in Python:

# data = [1, 7, 11]
# for i = 0; i<len(data); i++:
#     print("Now i is " + i)
#     print("The value is {}".format(data[i]))

# Often new comers attempt to build one:

data = [1, 7, 11]

# NOT pythonic: faking it with a while
i = 0
while i < len(data):
    print("Now i is {}".format(i))
    print("The value is {}".format(data[i]))
    i += 1

# write loops like this! 
for item in data:
    print("The value is {}".format(item))
```
> If the goal is just go through a collection, use the for-in loop.

> If really want to use step numbers, use range (python2 will generate list, so use xrange)
 technically generator .. 

```python
# but sometimes, fairly rarely, you really need just an
# increasing number of integers.

for i in range(0, 10):
    print(i, end=', ')

print(range(1, 7))

# think of the above as:
# for i = 0; i<10; i++:
#     print(i, end=', ')

# So, use range to model for int loops
```
> There is Pythonic way to do numerical for loop. **enumerate**
```python
# More often, you need the index and the value. use enumerate for this!

# How would you actually accomplish this? With range? No.
# for idx = 0; idx<len(data); idx++:
#     val = data[idx]
#     print(" {} --> {}".format(idx, val))

data = [1, 7, 11]

for idx, value in enumerate(data):
    print(" {} --> {}".format(idx+1, value))
```
> Pythoic recommendation: Do not use else clause on loops. 
- Loops have an else block, don't use it! Bad example below
- confuse concept... [Learn More](https://python-notes.curiousefficiency.org/en/latest/python_concepts/break_else.html)
```python
print("Running through the while: ", end='')
count = 0
while count < 5:
    print('.', end='')
    count += 1
else:
    print("In the else clause of the while loop.")

# >>> .....In the else clause of the while loop.
print("Breaking out of the while: ", end='')
count = 0
while count < 5:
    print('.', end='')
    count += 1
    if count > 3:
        break
else:
    print("In the else clause of the early break loop.")

# >>> ....

```
