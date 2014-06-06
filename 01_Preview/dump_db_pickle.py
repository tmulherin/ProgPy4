#!python

# PP4E\Preview\dump_db_pickle.py

import pickle
import os

os.system('cls')

dbfile = open('people-pickle', 'rb')
db = pickle.load(dbfile)

for key in db:
    print(key, '=>\n', db[key])

print('\n\n')

for key in db['sue']:
    print(key, ' => ', db['sue'][key])

print('\n\n')

for key in db:
    outstring = ""
    print(key)
    print('----')
    for key2 in db[key]:
        outstring += key2 + ': ' + str(db[key][key2]) + ', '
    print(outstring[:-2], '\n')

