import pandas as pd

df = pd.read_csv('ZILLOW-Z55436_ZRISFRR.csv')
print(df.head())
print("***************************************")

df.set_index('Date', inplace=True)
print(df.head())
print("***************************************")
df.to_csv('newcv2.csv')

df = pd.read_csv('newcv2.csv')
print(df.head())
print("***************************************")

df = pd.read_csv('newcv2.csv', index_col=0)
print(df.head())
print("***************************************")

df.columns = ['Edina_HP!']
print(df.head())
print("***************************************")

df.to_csv('newcsv3.csv')
print(df.head())
print("***************************************")

df.to_csv('newcsv4.csv', header=False)
print(df.head())
print("***************************************")

df = pd.read_csv('newcsv4.csv', names=['Date', 'Edina_HPI'], index_col=0)
print(df.head())
print("***************************************")

df.to_html('example.html')
print("***************************************")

df = pd.read_csv('newcsv4.csv', names=['Date', 'MSP_HPI'])
print(df.head())
print("***************************************")
df.rename(columns={'MSP_HPI':'SLP_HPI'}, inplace=True)
print(df.head())
print("***************************************")