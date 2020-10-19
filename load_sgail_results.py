import json
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.stats import entropy
from scipy import stats
from scipy import special
from scipy.stats import norm
from matplotlib import pyplot as plt
import seaborn as sns
from scipy.stats.kde import gaussian_kde
from scipy.stats import norm
from agent import *

import scipy

import math

episode_path = '/home/novikova/thesis/'

from numpy import load
#poses from 10 episodes

def qet_qpos_i(index):
    for i in range(10):
        agent_file = "/home/novikova/thesis/vid_walker_3step_473k" + str(i) + ".npz"
        data = load(agent_file, allow_pickle=True)
        episode_poses = data['qpos']
        plt.figure()
        for timestamp, pose_arr in enumerate(episode_poses):
            plt.plot(timestamp, pose_arr[index], 'ro')
        plt.grid(True)
        plt.title('Qpos agent '+str(index))
        plt.xlabel('joint movement ')
        plt.ylabel('Likelihood occurence')
        plt.savefig(episode_path + 'ep_' + str(i) + 'qpos_data_'+str(index)+'.png')

for i in range(9):
    qet_qpos_i(i)



#n1,bins1,patches1 = plt.hist(samples_qk,n_bins,density = True, histtype= 'step',cumulative = True)

