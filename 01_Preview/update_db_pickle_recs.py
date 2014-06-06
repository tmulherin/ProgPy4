#!python

# PP4E\Preview\update_db_pickle_recs.py

import pickle

suefile = open('sue.pkl', 'rb')
sue = pickle.load(suefile)
suefile.close

sue['pay'] *= 1.25
suefile = open('sue.pkl', 'wb')
pickle.dump(sue, suefile)
suefile.close