#!python

# PP4E\Preview\make_db_pickle_recs.py
from Initdata import bob, sue, tom
import pickle

for (key, record) in [('bob', bob), ('tom', tom), ('sue', sue)]:
    recfile = open(key + '.pkl', 'wb')
    pickle.dump(record, recfile)
    recfile.close