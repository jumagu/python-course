# There are different ways to import packages/libraries/modules

# ? Import the whole package
import math

# ? Import an specific function
from datetime import datetime

# ? Import with alias
# The whole package
import re as regex
# An specific function
from random import randint as rand_int

# Import multiple things
from uuid import uuid4, uuid1

# Import all (not recommended)
# from typing import *

print(math.sqrt(16))
print(datetime.now())
print(regex.compile(""))
print(rand_int(1, 100))

print(uuid4())
print(uuid1())


