import pandas as pd 

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_squirrels_pop = len(data[data['Primary Fur Color'] == 'Gray'])
cinnamon_squirrels_pop = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrels_pop = len(data[data['Primary Fur Color'] == 'Black'])

census_data = {
   'Fur Color' : ['Black', 'Grey', 'Cinnamon'],
   'Squirrel Population' : [black_squirrels_pop, gray_squirrels_pop, cinnamon_squirrels_pop]
}

df = pd.DataFrame(census_data)
df.to_csv('Shortened Squirrel Census data.csv')