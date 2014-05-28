#!python

# PP4E\Preview\Initdata.py

#==> Initialize data to be stored in files, pickles, shelves

import os
os.system('cls')

#-> records
bob = {'name': 'Bob Smith', 'age': 42, 'pay': 30000, 'job': 'Dev'}
sue = {'name': 'Sue Jones', 'age': 45, 'pay': 40000, 'job': 'hdw'}
tom = {'name': 'Tom',       'age': 50, 'pay': 0,     'job': 'None'}

if __name__ == '__main__':
    print('Data initialized')

#-> Initialize database
db = {}
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

if __name__ == '__main__':
    print ('Database Initialized')
    print ("\n\n")