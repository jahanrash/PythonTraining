import quandl
import pandas as pd

api_key = open('quandlapikey.txt', 'r').read()
df = quandl.get('FMAC/HPI_MN', authtoken=api_key)
print(df.head())


print('*************************************')
print(df.tail())

print('*************************************')
fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
#this is a list.
print(fiddy_states)

print('*************************************')
#this is a dataset
print(fiddy_states[0])

print('*************************************')
#this is a column
print(fiddy_states[0][1])


print('*************************************')
#this is a column
for abbv in fiddy_states[0][1][1:]:
    print("FMAC/HPI_"+str(abbv))
