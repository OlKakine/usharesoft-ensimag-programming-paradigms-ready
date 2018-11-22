#!/usr/bin/env python3

# my_criteria='Gout'
# criteria_len=len(my_criteria)

# name="Nom"
# name_len=len(name)

# names=[]
# criteria_values=[]
# with open("beer_list.json",'r') as dataset:
#     for line in dataset:
#         line=line.strip()
#         if line[1:name_len+1]==name:
#             names.append(line[name_len+4:-1])
#         elif line[1:criteria_len+1]==my_criteria:
#             criteria_value=line[criteria_len+4:-1]
#             if criteria_value== 'null':
#                 criteria_value=0
#             criteria_values.append(float(criteria_value))

# ind_max=criteria_values.index(max(criteria_values))
# print(names[ind_max],criteria_values[ind_max])

import json

with open('beer_list.json', 'r') as f:
    beer_dict = json.load(f)

criteria="Gout"
criteria_value=0
for beer in beer_dict:
    beer_criteria_value=beer[criteria]
    if beer_criteria_value != None and float(beer_criteria_value) > criteria_value:
        name=beer["Nom"]
        criteria_value=float(beer[criteria])
    
print(name,criteria_value)
