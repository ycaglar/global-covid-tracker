import pandas as pd
from country_names import names
from regions import regions
from country_codes import codes

df = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-data.csv', low_memory = False)
df['Date_reported'] = pd.to_datetime(df['Date_reported'])
df = df[df['WHO_region'] != 'Other']
df = df[df['New_cases'] >= 0]
df = df[df['New_deaths'] >= 0]
df['WHO_region'] = df['WHO_region'].apply(lambda abbrevation:regions[abbrevation])
df = df.rename(columns = {'WHO_region':'Region'})
df['Country'].replace(names, inplace = True)
df.loc[df['Country'] == 'Namibia', 'Country_code'] = 'NA'
#covid_df['Country_code'].replace(iso_codes, inplace = True)
df['Country_code'] = df['Country_code'].apply(lambda code:codes[code])


# df = df[df['Date_reported'] == pd.Timestamp.today().normalize() - pd.Timedelta(days = 1)]
# print(df[df['Country'] == 'United States'])
