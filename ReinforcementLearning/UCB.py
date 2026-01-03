import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dataset= pd.read_csv('Ads_CTR_Optimisation.csv')

N=10000
d=10
ads_selected=[]
numberOfSelections=[0]*d
sum_of_rewards=[0]*d
total_rewards=0


import math
for n in range(0,N):
    ad=0
    max_upper_bound=0
    for i in range(0,10):
        if(numberOfSelections[i]>0):
            avg_reward=sum_of_rewards[i]/numberOfSelections[i]
            delta_i=math.sqrt((3/2)*math.log(n+1)/numberOfSelections[i])
            ucb=avg_reward+delta_i
        else:
            ucb=1e400
        if(ucb>max_upper_bound):
            max_upper_bound=ucb
            ad=i
    ads_selected.append(ad)
    numberOfSelections[ad]=numberOfSelections[ad]+1
    sum_of_rewards[ad]= sum_of_rewards[ad]+dataset.values[n,ad]
    total_rewards=total_rewards+dataset.values[n,ad]



print(ads_selected)
sumas=dataset.sum()
print(sumas)
print(total_rewards)
plt.hist(ads_selected)
plt.show()
