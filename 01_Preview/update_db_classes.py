#!python

# PP4E\Preview\update_db_classes.py

import shelve

db = shelve.open('people-class-shelve')
sue = db['sue']
sue.giveRaise(.25)
db['sue'] = sue

tom = db['tom']
tom.giveRaise(.20)
db['tom'] = tom

db.close
