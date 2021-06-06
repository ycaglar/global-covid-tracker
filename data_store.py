"""
This is the 'data_store' module.

The data_store module is the main data store of the app. It consists of a single
Pandas DataFrame which is essentially the disjunction of the Covid-19 data from
the covid_data_national helper module and the population data imported from the
population_data module.
"""

import pandas as pd
from regions import regions
from country_names import names
from country_codes import codes
import population_data
import covid_data_national

#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', None)

dataframe = pd.merge(covid_data_national.df,
                     population_data.df,
                     on = 'Country',
                     how = 'left')
dataframe = dataframe[dataframe['Population'].isnull() == False]
dataframe = dataframe[dataframe['Population'] > 0]
dataframe = dataframe.astype({'Population':'int64'})

# dataframe = dataframe[dataframe['Date_reported'] == pd.Timestamp.today().normalize() - pd.Timedelta(days = 1)]
# print(dataframe[dataframe['Country'] == 'United States'])
