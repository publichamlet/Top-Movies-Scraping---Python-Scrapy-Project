from asyncore import write
import os, sys
import json, csv
import pandas as pd

if sys.platform.startswith('linux'):
    os.chdir(os.path.dirname(__file__))

with open('MovieList-Generated.json', 'r') as j:
    json_obj = json.load(j)
keyorder = ['Release Year', 'Movie Title',  'Sl No:']


df = pd.DataFrame(json_obj, columns=keyorder)
print(df)
df.to_csv('test.csv', index=False)
