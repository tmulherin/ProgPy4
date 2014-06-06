#!python

# PP4E\Preview\dump_db_shelve.py

import shelve, os

os.system('cls')

db = shelve.open('people-shelve')
for key in db:
    print(key, '=>\n ', db[key])


print('\n\n', db['sue']['name'])