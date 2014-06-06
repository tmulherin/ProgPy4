#!python
# cd c:\Users\tmulher\Documents\_dev\Python\PP4E\Preview
# cd /c/Users/tmulher/Documents/_dev/Python/PP4E/Preview

# PP4E\Preview\make_db_classes.py

import shelve
from person import Person
from manager import Manager

bob = Person('Bob Smith', 42, 30000, 'software')
sue = Person('Sue Jones', 45, 40000, 'hardware')
tom = Manager('Tom Doe', 50, 50000)

db = shelve.open('people-class-shelve')

db['bob'] = bob
db['sue'] = sue
db['tom'] = tom
db.close

