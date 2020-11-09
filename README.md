# Python Modules
**Python Libraries and built-in functions** 
```python
# Few ways to import modules
# Not good to import * as it congests the namespace
import <mod name>
from <mod name> import <name>
from <mod name> import *
```

**Task 1**
```python
# This will round a number appropriately
def round_task():
    choice = input("Input a number to check: ")
    checker = float(choice) % 1
    if checker >= 0.5:
        return print(math.ceil(float(choice)))
    else:
        return print(math.floor(float(choice)))
```