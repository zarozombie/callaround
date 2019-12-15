import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

#df = pd.read_excel('a.csv' , sheetname='Sheet1')
df = pd.read_csv('a.csv')
data_f = pd.DataFrame(data=df)
print(data_f)
x = 1
for x in len(data_f.values):
    print(X)
    x+1

#print(data_f[0])

#print("colum headings:")
#print(pd.DataFrame.equals(df))

#print("welcome to the call around program")
#print("press ENTER to start")
