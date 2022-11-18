# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 15:12:11 2018

Python Script to test DRL envs without Tensorflow

@author: SB
"""

import chtrain_biped
#import matplotlib.pyplot as plt
import numpy as np

for i in range (2):
    env = chtrain_biped.Model(True)
    ac_dim = 1
    n_episodes = 2
    T=2
    trajectories = []
    
    for episode in range(n_episodes):
              done = False
              env.reset()  
              while not done:
                  ac = 2*(0.5-np.random.rand(ac_dim,))
                  state, reward, done, _ = env.step(ac)
