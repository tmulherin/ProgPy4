#!python

# PP4E\Preview\dump_db_pickle_recs.py

import os
os.system('cls')

import pickle, glob

for filename in glob.glob('*.pkl'):
    recfile = open(filename, 'rb')
    record = pickle.load(recfile)
    print(filename, '=>\n', record)

suefile = open('sue.pkl', 'rb')
print('\n\n', pickle.load(suefile)['name'])
