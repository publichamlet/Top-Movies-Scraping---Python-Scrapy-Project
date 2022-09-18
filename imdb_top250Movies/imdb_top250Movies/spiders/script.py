import os, sys
import json
import pandas as pd
from time import perf_counter

start = perf_counter()

if sys.platform.startswith('linux'):
    os.chdir(('/'.join(os.path.dirname(__file__).split('/')[:-2])))



os.system('scrapy crawl imdbMovies -O MovieList-Generated.json')
with open('MovieList-Generated.json', 'r') as j:
    json_obj = json.load(j)

keyorder = ['Sl_No',
            'Movie_Title',
            'Release_Year',
            'Movie_Duration',
            'IMDb_Rating',
            'IMDb_Customer_votes',
            'Genre',
            'StoryLine',
            'Director',
            'Writers',
            'Stars',
            'Release_Date',
            'Country_of_Origin',
            'Languages',
            'Filming_Locations',
            'Production_Companies']

df = pd.DataFrame(json_obj, columns=keyorder)
df1 = df.sort_values(by=['Sl_No'])
df2 = df1.applymap(lambda x: ', '.join(x) if type(x) == type(list()) else x)

df2.to_csv('MovieList-Generated.csv', index=False)

print(f'Total time taken to complete the extraction is {perf_counter() - start:.2f}secs')