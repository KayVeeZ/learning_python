# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 18:17:46 2023

@author: Kshitij Vashisth
"""
import os
import time
timestamp = time.strftime('%H:%M:%S')
hour = time.strftime('%H')
min = time.strftime('%M')
if (int(hour)<12 and int(hour)>=00):
    print("Good Morning, Sir! The time is:", timestamp)
elif (int(hour)==12 and int(min)==00):
    print("Good Noon, Sir!")
elif (int(hour)>=12 and int(hour)<17):
    print("Good Afternoon, Sir! The time is:", timestamp)
elif (int(hour)>16):
    print("Good Evening, Sir! The time is:", timestamp)
else:
    print("Good Night, Sir! The time is:", timestamp)
os.system("python --version")    