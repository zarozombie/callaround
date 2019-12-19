import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

#df = pd.read_excel('a.csv' , sheetname='Sheet1')
df = pd.read_csv('a.csv')
data_f = pd.DataFrame(data=df)
print(data_f)
x = 0
MALE = []
FEMALE = []
BOTH = []


#parsing while loop to sort 3 arrays (Male, Female, Both)
for x in range(int(len(data_f.values))-1):
    if data_f.values[x,5] == "M":
        MALE.append(x)                
#        x+=1
    elif data_f.values[x,5] == "F":
        FEMALE.append(x)
#        x+=1
    elif data_f.values[x,5] == "B":
        BOTH.append(x)
#        x+=1
    else:
        print(data_f.values[x,1], "does not have a correct Gender preference or format please review\n this is what is in the prefence field:", print(data_f.values[x,3]))
    print(x)
    x+=1
#    print(data_f.values[x,1], " wants to call", data_f.values[x,3])


print("BEHOLD THE DATA!", MALE, FEMALE, BOTH)
#print(data_f.values[0])

#print("colum headings:")
#print(pd.DataFrame.equals(df))

#print("welcome to the call around program")
#print("press ENTER to start")
