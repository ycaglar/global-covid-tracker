import pandas as pd
from regions import regions
from country_names import names
from country_codes import codes
import population_data
import covid_data

#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', None)

global_df = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-table-data.csv', low_memory = False)
global_df = global_df[global_df['Name'] == 'Global']
global_df = global_df[['Cases - cumulative total', 'Cases - newly reported in last 24 hours', 'Deaths - cumulative total', 'Deaths - newly reported in last 24 hours']]
global_df = global_df.rename(columns = {'Cases - cumulative total':'Cumulative_cases',\
                                        'Cases - newly reported in last 24 hours':'New_cases',\
                                        'Deaths - cumulative total':'Cumulative_deaths',\
                                        'Deaths - newly reported in last 24 hours':'New_deaths'})
global_df = global_df.astype({'New_cases':'int64',\
                              'Cumulative_cases':'int64',\
                              'New_deaths':'int64',\
                              'Cumulative_deaths':'int64'})

dataframe = pd.merge(covid_data.df, population_data.df, on = 'Country', how = 'left')
dataframe = dataframe[dataframe['Population'].isnull() == False]
dataframe = dataframe[dataframe['Population'] > 0]
dataframe = dataframe.astype({'Population':'int64'})

# dataframe = dataframe[dataframe['Date_reported'] == pd.Timestamp.today().normalize() - pd.Timedelta(days = 1)]
# print(dataframe[dataframe['Country'] == 'United States'])
