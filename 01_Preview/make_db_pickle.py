#!python

# PP4E\Preview\make_db_pickle.py

from Initdata import db
import pickle

dbfile = open('people-pickle', 'wb') #use binary mode files in 3.x
pickle.dump(db, dbfile) # data is bytes not alpha
dbfile.close

 