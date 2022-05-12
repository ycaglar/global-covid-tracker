"""
This is the 'population_data' module.

Population information is displayed on various sections within the app such as
hover windows and country cards. The population information is pulled from the
United Nation's Database and cleaned/organized to fit the use case of the app.
"""

import pandas as pd
from country_names import names

df = pd.read_csv('https://population.un.org/wpp/Download/Files/\
                  1_Indicators%20(Standard)/CSV_FILES/\
                  WPP2019_TotalPopulationBySex.csv',
                 low_memory=False,
                 usecols=['Location', 'Time', 'PopTotal'])

df = df[df['Time'] == 2020]
df = df[['Location', 'PopTotal']].drop_duplicates()
df = df[df['Location'] != 'Micronesia']

df['PopTotal'] *= 1000
df = df.astype({'PopTotal': 'int64'})

# df = df[df['PopTotal'].isnull() == False]
# df = df[df['PopTotal'] > 0]

# import locale
# locale.setlocale(locale.LC_ALL, '')
# df['PopTotal'] = df['PopTotal'].apply(lambda value:f'{value:n}')

df = df.rename(columns={'Location': 'Country', 'PopTotal': 'Population'})
df['Country'].replace(names, inplace=True)
