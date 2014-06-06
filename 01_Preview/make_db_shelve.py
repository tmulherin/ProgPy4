#!python

# PP4E\Preview\make_db_shelve.py
from Initdata import bob, sue
import shelve

db = shelve.open('people-shelve')
db['bob'] = bob
db['sue'] = sue

db.close


