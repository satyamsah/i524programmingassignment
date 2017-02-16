import pandas as pd
import pygal
import math
data = pd.read_csv('2016-first-quarter-citations.csv')
ages = data['Cited Person Age']
# print  ages

ageFreqDict ={}
line_chart=pygal.Bar()

for age in ages:
    if(math.isnan(age)):
        continue
    count=0
    if ageFreqDict.has_key(age):
        count=ageFreqDict.get(age)
        ageFreqDict[age]=count+1
    else:
        ageFreqDict[age]=count+1


arrayofUniqueAge=[]
arrayofCountofPeopleofSameAge=[]
for key,value in ageFreqDict.items():
    arrayofUniqueAge.append(int(key))
    arrayofCountofPeopleofSameAge.append(int(value))


line_chart.x_labels=arrayofUniqueAge
line_chart.add('age',arrayofCountofPeopleofSameAge)
line_chart.render_to_file('abcd.svg')


# print type(range(min(arrayofUniqueAge),max(arrayofUniqueAge)))
# for i in range(min(arrayofUniqueAge),max(arrayofUniqueAge)):
#     if(i in ageFreqDict):
#       line_chart.add('age',ageFreqDict.get(i))
#     else:
#       line_chart.add('age',0)


