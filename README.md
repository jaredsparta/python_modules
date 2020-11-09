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
def round_task(number):
    checker = number % 1
    if checker >= 0.5:
        return math.ceil(number)
    else:
        return math.floor(number)
```