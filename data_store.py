import pandas as pd
from regions import regions
from country_names import names
from country_codes import codes

#pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
# pd.set_option('display.width', None)
# pd.set_option('display.max_colwidth', None)

population_df = pd.read_csv('https://population.un.org/wpp/Download/Files/1_Indicators%20(Standard)/CSV_FILES/WPP2019_TotalPopulationBySex.csv', low_memory = False)
population_df = population_df[population_df['Time'] == 2020]
population_df = population_df[['Location', 'PopTotal']].drop_duplicates()
population_df = population_df[population_df['Location'] != 'Micronesia']
population_df = population_df.astype({'PopTotal': 'int32'})
population_df = population_df.rename(columns={'Location':'Country', 'PopTotal':'Population'})
population_df['Country'].replace(names, inplace = True)
# population.to_csv('~/Downloads/DataFrames/population.csv')
# breakpoint()

covid_df = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-data.csv', low_memory = False)
covid_df['Date_reported'] = pd.to_datetime(covid_df['Date_reported'])
covid_df = covid_df[covid_df['WHO_region'] != 'Other']
covid_df = covid_df[covid_df['New_cases'] >= 0]
covid_df = covid_df[covid_df['New_deaths'] >= 0]
covid_df['WHO_region'] = covid_df['WHO_region'].apply(lambda abbrevation:regions[abbrevation])
covid_df = covid_df.rename(columns = {'WHO_region':'Region'})
covid_df['Country'].replace(names, inplace = True)
covid_df.loc[covid_df['Country'] == 'Namibia', 'Country_code'] = 'NA'
#covid_df['Country_code'].replace(iso_codes, inplace = True)
covid_df['Country_code'] = covid_df['Country_code'].apply(lambda code:codes[code])

dataframe = pd.merge(covid_df, population_df, on = 'Country', how = 'left')

dataframe = dataframe[dataframe['Population'].isnull() == False]
dataframe = dataframe[dataframe['Population'] > 0]
dataframe = dataframe.astype({'Population': 'int32'})
