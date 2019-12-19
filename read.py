import random
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

#df = pd.read_excel('a.csv' , sheetname='Sheet1')
df = pd.read_csv('a.csv')
data_f = pd.DataFrame(data=df)
#print(data_f)
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
    else:
        print(data_f.values[x,1], "does not have a correct Gender preference or format please review\n this is what is in the prefence field:", print(data_f.values[x,3]))
#    print(x)
    x+=1
#    print(data_f.values[x,1], " wants to call", data_f.values[x,3])

class rand_sort:
    def __init(self, array_index):
        self.array_index = array_index
    def rand_num(self):
        for x in len(self.array_index):
            print(array_index[x])


#print("BEHOLD THE DATA!",MALE, FEMALE, BOTH)
#print("Here is a Random Values from the MALE Group", random.choice (MALE))
#print("Here is a Random Values from the FEMALE Group", random.choice (FEMALE))
#print("Here is a Random Values from the BOTH Group", random.choice (BOTH))

print("---------------------------\n\n")

for y in range(len(MALE)):
    print("y is = to", y)
    temp_array = MALE
    print("Male = ", MALE)
#    del temp_array[y]
    print(temp_array)
    for x in range(data_f.values[MALE[y], 4]):
        print(data_f.values[MALE[y],1], "Will call", data_f.values[random.choice (temp_array), 1])
    
print("---------------------------\n\n")

for y in range(len(FEMALE)):
    for x in range(data_f.values[FEMALE[y], 4]):
        print(data_f.values[FEMALE[y],1], "Will call", data_f.values[random.choice (FEMALE), 1])
   

print("---------------------------\n\n")

for y in range(len(BOTH)):
    for x in range(data_f.values[BOTH[y], 4]):
        print(data_f.values[BOTH[y],1], "Will call", data_f.values[random.choice (BOTH), 1])

#print(data_f.values[0])

#print("colum headings:")
#print(pd.DataFrame.equals(df))

#print("welcome to the call around program")
#print("press ENTER to start")
