#!python

# PP4E\Preview\dump_db_classes.py

import shelve, os

os.system('cls')

db = shelve.open('people-class-shelve')
for key in db:
    print(key, '=>\n ', db[key].name, db[key].pay)

bob = db['bob']
print('\n\n', bob.lastName())
print(db['tom'].pay)
