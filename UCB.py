# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:13:54 2020

@author: kingslayer
"""

#Upper Confidence bound

#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

#importing the dataset
dataset=pd.read_csv(r"Ads_CTR_Optimisation.csv")
 
#Appling UCB
N=10000
d=10
ads_selected=[]
sums_of_rewards=[0]*d
numbers_of_selections=[0]*d
total_reward=0
for n in range(0,N):
    ad=0
    max_upper_bound=0
    for i in range(0,d):
        if numbers_of_selections[i]>0:
            average_reward=sums_of_rewards[i]/numbers_of_selections[i]
            delta_i=math.sqrt(3/2 * math.log(n+1)/numbers_of_selections[i])
            upper_bound=average_reward+delta_i
            
        else:
            upper_bound=1e400
        if upper_bound>max_upper_bound:
            max_upper_bound=upper_bound
            ad=i
    ads_selected.append(ad)
    reward=dataset.values[n,ad]
    sums_of_rewards[ad]+=reward
    numbers_of_selections[ad]+=1
    total_reward+=reward
    
#Visualising results
plt.hist(ads_selected)
plt.xlabel("Ads")
plt.ylabel("No.of selections")
plt.title("UCB")
plt.show()
