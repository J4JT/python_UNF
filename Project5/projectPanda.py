import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None  
df = pd.read_csv('items.csv')
print('first seven')
print(df.head(7))
print('last seven')
print(df.tail(7))
print('INFO')
#describe shape
rows=df.shape[0]
columns=df.shape[1]

print(f'Item dataframe has {rows} rows and {columns} columns')
print('Descriptive statistics for Bottle_Cost')
print(df.describe())
#add colunmn
df['Bottle_profit_margin']=(df.Bottle_Retail_Price - df.Bottle_Cost)/df.Bottle_Retail_Price
df.head()
#drop rows
df.iloc[5:15]
print(df.describe())
#Display of BottleVolume, Pack, BotteProfit
print('items with greater than 750ml, 12 pack, and profit margins of greater than 0.3')
print(df[(df['Bottle_Volume_ml']> 750) & (df['Pack']>12) & (df['Bottle_profit_margin'] > 0.3) ])
print('Energy Drinks')
energy=df[df['Category']=='Energy Drink']

energyNumber=energy.shape[0]
print(f'The number of Energy Drinks is {energyNumber} ')


#new dataframe

items2= df[['Item_id', 'Item_Description','Bottle_Retail_Price', 'Bottle_profit_margin']] 
print(items2.head())

items2['QTY']=np.random.randint(0,1000,size=4159)
print(items2.head())

