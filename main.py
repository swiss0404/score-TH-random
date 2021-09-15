import pandas as pd
import random
from time import sleep
from datetime import datetime

seat = pd.read_csv("csv_file/TEST_Quota_Bidding - Sheet1.csv")
data = pd.read_csv("csv_file/[DL_16_09] Quota Bidding (Responses) - Sheet3.csv")
seat = seat[["Country",'# Contracts']]
list_school = data.columns.to_list()[1:]
data = data.drop(columns=['University'])
round = 1
results =[]
while seat['# Contracts'].sum() > 1:
    random.seed(str(datetime.now))
    random.shuffle(list_school)
    print('')
    print('Round: ' + str(round))
    none_control = True
    for school in list_school:
        for sel in data[school]:
            if sel:
                if seat.loc[seat['Country'] == sel,'# Contracts'].values[0] > 0:
                    sleep(1)
                    seat.loc[seat['Country'] == sel,'# Contracts'] -= 1
                    results.append(sel + ': ' + school)
                    print(school + ': ' + sel)
                    none_control = False
                    data[school] = False
                break
    round += 1
    for taken_country in seat['Country'].where(seat['# Contracts'] == 0):
        data = data.applymap(lambda x: False if taken_country == x else x)
    if none_control:
        print('None')
    sleep(1)
print('')
print('FINISH')
print('')
