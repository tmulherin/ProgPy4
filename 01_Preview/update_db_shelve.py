#!python

# PP4E\Preview\update_db_shelve.py

from Initdata import tom

import shelve
db = shelve.open('people-shelve')
sue = db['sue']
sue['pay'] *= 1.5
db['sue'] = sue
db['tom'] = tom
db.close
