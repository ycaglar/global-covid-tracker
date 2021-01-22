import pandas as pd
from regions import regions
from countries import countries
from country_codes import iso_2_iso_3_codes as iso_codes

#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', None)

population = pd.read_csv('https://population.un.org/wpp/Download/Files/1_Indicators%20(Standard)/CSV_FILES/WPP2019_TotalPopulationBySex.csv', low_memory = False)
population = population[population['Time'] == 2020]
population = population[['Location', 'PopTotal']].drop_duplicates()
population = population[population['Location'] != 'Micronesia']
population = population.astype({'PopTotal': 'int32'})
population = population.rename(columns={'Location':'Country', 'PopTotal':'Population'})
population['Country'].replace(countries, inplace = True)
# population.to_csv('~/Downloads/DataFrames/population.csv')
# breakpoint()

dataframe = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-data.csv', low_memory = False)
dataframe['Date_reported'] = pd.to_datetime(dataframe['Date_reported'])
dataframe = dataframe[dataframe['WHO_region'] != 'Other']
dataframe = dataframe[dataframe['New_cases'] >= 0]
dataframe['WHO_region'] = dataframe['WHO_region'].apply(lambda abbrevation:regions[abbrevation])
dataframe = dataframe.rename(columns = {'WHO_region':'Region'})
dataframe['Country'].replace(countries, inplace = True)
dataframe.loc[dataframe['Country'] == 'Namibia', 'Country_code'] = 'NA'

#dataframe['Country_code'].replace(iso_codes, inplace = True)
dataframe['Country_code'] = dataframe['Country_code'].apply(lambda code:iso_codes[code])
dataframe = pd.merge(dataframe, population, on = 'Country', how = 'left')

dataframe = dataframe[dataframe['Population'].isnull() == False]
dataframe = dataframe[dataframe['Population'] > 0]
dataframe = dataframe.astype({'Population': 'int32'})
