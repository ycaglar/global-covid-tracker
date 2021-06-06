"""
This is the 'covid_data_global' module.

The covid_data_global module supplies a Pandas DataFrame consisting of Covid-19
statistics on a global scale. It fetches raw data from The World Health
Organization then reduces it to a four columned DataFrame as such:
    New_cases
    Cumulative_cases
    New_deaths
    Cumulative_deaths
"""

import pandas as pd

df = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-table-data.csv',
                 low_memory = False)
df = df[df['Name'] == 'Global']
df = df[['Cases - cumulative total',\
         'Cases - newly reported in last 24 hours',\
         'Deaths - cumulative total',\
         'Deaths - newly reported in last 24 hours']]
df = df.rename(columns = {'Cases - cumulative total':'Cumulative_cases',\
                          'Cases - newly reported in last 24 hours':'New_cases',\
                          'Deaths - cumulative total':'Cumulative_deaths',\
                          'Deaths - newly reported in last 24 hours':'New_deaths'})
df = df.astype({'New_cases':'int64',\
                'Cumulative_cases':'int64',\
                'New_deaths':'int64',\
                'Cumulative_deaths':'int64'})
