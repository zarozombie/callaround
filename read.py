import random
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

df = pd.read_csv('a.csv')
data_f = pd.DataFrame(data=df)
MALE = []
FEMALE = []
BOTH = []

#print all data in table
#print(data_f)


#print("welcome to the call around program")
#print("press ENTER to start")dd
#parsing while loop to sort 3 arrays (group by preference Male, Female, Both)i
#possibally append to matrix array
for x in range(int(len(data_f.values))-1):
    if data_f.values[x,5] == "M":
        MALE.append(x)
    elif data_f.values[x,5] == "F":
        FEMALE.append(x)
    elif data_f.values[x,5] == "B":
        BOTH.append(x)
    else:
        print(data_f.values[x,1], "does not have a correct Gender preference or format please review\n this is what is in the prefence field:", print(data_f.values[x,3]))

#test Class not yet implamented
class rand_sort:
    def __init(self, array_index):
        self.array_index = array_index
    def rand_num(self):
        for x in len(self.array_index):
            print(array_index[x])


#output Options#####################################################################

#print output of all arrays
#print("BEHOLD THE DATA!",MALE, FEMALE, BOTH)

#print randon choices
#print("Here is a Random Values from the MALE Group", random.choice (MALE))
#print("Here is a Random Values from the FEMALE Group", random.choice (FEMALE))
#print("Here is a Random Values from the BOTH Group", random.choice (BOTH))

####################################################################################

#output Template for all random results
print("---------------------------\n\n")

for y in range(len(MALE)):
#    print("y is = to", y)
    temp_array = MALE
#    print("Male = ", MALE)
#    print(temp_array)

#Display Male Random Results
    for x in range(data_f.values[MALE[y], 4]):
        test = random.choice (temp_array)
        print(data_f.values[MALE[y],1], "Will call", data_f.values[random.choice (temp_array), 1])
print("---------------------------\n\n")

for y in range(len(FEMALE)):

#Display Female Random Rsults    
    for x in range(data_f.values[FEMALE[y], 4]):
        print(data_f.values[FEMALE[y],1], "Will call", data_f.values[random.choice (FEMALE), 1])
print("---------------------------\n\n")

for y in range(len(BOTH)):
#Display Both Random Results
    for x in range(data_f.values[BOTH[y], 4]):
        print(data_f.values[BOTH[y],1], "Will call", data_f.values[random.choice (BOTH), 1])

#########################################################################################################
#Need method of sending data to twillio##################################################################
#########################################################################################################

#test test test
#Other Output Options ####################################
#print(data_f.values[0])
#print("colum headings:")
#print(pd.DataFrame.equals(df))
#############################################################
