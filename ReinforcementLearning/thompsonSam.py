import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random
dataset= pd.read_csv('Ads_CTR_Optimisation.csv')

N=10000
d=10
reward_1=[0]*d
reward_0=[0]*d
selected_ads=[]
ads_fre=[0]*d
total_rewards=0

for x in range(0,N):
    ad=0
    max_bound=0
    for i in range(0,d):
        bound=random.betavariate(reward_1[i]+1,reward_0[i]+1)
        if(bound>max_bound):
            max_bound=bound
            ad=i
    reward=dataset.values[x,ad]
    if reward==0 :
        reward_0[ad]+=1
    else:
        reward_1[ad]+=1
    selected_ads.append(ad)
    ads_fre[ad]+=1
    total_rewards +=reward

plt.hist(selected_ads)
plt.show()

