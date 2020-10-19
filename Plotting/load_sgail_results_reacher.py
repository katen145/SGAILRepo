from scipy import stats
from matplotlib import pyplot as plt
from agent import *
import statsmodels.api as sm
import scipy
import math
import numpy as np
from scipy import stats
import seaborn as sns
from matplotlib import pyplot as plt
from numpy import load

proj_path = '/home/novikova/thesis/'
reacher_agent_name='3step_30k'#3step_30k 5step_26k

# poses from 10 episodes
def get_episode_data(i):
    agent_file = proj_path + "vid_reacher_"+reacher_agent_name + str(i) + ".npz"
    data = load(agent_file, allow_pickle=True)
    episode_poses = data['qpos']
    return episode_poses


reacher_expert = proj_path + "reacher_short_05.npz"
sample_size = 150

if (__name__ == '__main__'):
    sns.set()
    data_comparison = list()
    traj_data = np.load(reacher_expert, allow_pickle=True)
    qpos_list = traj_data['qpos']
    qpos_list = qpos_list[0]
    reacher_expert_data = qpos_list[:sample_size, :]

    pk = reacher_expert_data

    for episode in range(10):
        eps = "_ep" + str(episode) + "_"
        agent_reacher = get_episode_data(episode)
        reacher_agent_data = agent_reacher[:, :]
        reacher_agent_data = reacher_agent_data[:sample_size-20, :]
        reacher_agent_data = scipy.signal.resample(reacher_agent_data, sample_size)

        qk = reacher_agent_data

        pk_x = pk[:, 0]
        qk_x = qk[:, 0]
        pk_y = pk[:, 1]
        qk_y = qk[:, 1]


        print('=======================================================')
        print('agent x '+eps)
        min_agent_degrees = min(qk_x) * 180 / math.pi
        max_agent_degrees = max(qk_x) * 180 / math.pi
        print('min ', min_agent_degrees)
        print('max ', max_agent_degrees)
        ROM = max_agent_degrees - min_agent_degrees
        print('rom x', ROM)
        print('expert x '+eps)
        min_expert_degrees = min(pk_x) * 180 / math.pi
        max_expert_degrees = max(pk_x) * 180 / math.pi
        print('min ', min_expert_degrees)
        print('max ', max_expert_degrees)
        ROM = max_expert_degrees - min_expert_degrees
        print('rom x', ROM)

        print('agent y ' + eps)
        min_agent_degrees = min(qk_y) * 180 / math.pi
        max_agent_degrees = max(qk_y) * 180 / math.pi
        print('min ', min_agent_degrees)
        print('max ', max_agent_degrees)
        ROM = max_agent_degrees - min_agent_degrees
        print('rom y', ROM)
        print('expert y ' + eps)
        min_expert_degrees = min(pk_y) * 180 / math.pi
        max_expert_degrees = max(pk_y) * 180 / math.pi
        print('min ', min_expert_degrees)
        print('max ', max_expert_degrees)
        ROM = max_expert_degrees - min_expert_degrees
        print('rom y', ROM)

        plt.figure()
        plt.plot(pk_x, color="g", label="expert")
        plt.plot(qk_x, color="y", label="agent")

        plt.axhline(y=max(pk_x), color='r', linestyle='-',label="expert max")
        plt.axhline(y=min(pk_x), color='b', linestyle='-',label="expert min")
        plt.axhline(y=max(qk_x), color='m', linestyle='--',label="agent max")
        plt.axhline(y=min(qk_x), color='c', linestyle='--',label="agent min")

        plt.legend(loc="best")
        plt.title('1-DOF joint in the x axis (g = 3 step)')
        plt.savefig(proj_path +eps+  '_reacher_'+reacher_agent_name+'__x.png')

        plt.figure()
        plt.plot(pk_y, color="g", label="expert")
        plt.plot(qk_y, color="y", label="agent")

        plt.axhline(y=max(pk_y), color='r', linestyle='-',label="expert max")
        plt.axhline(y=min(pk_y), color='b', linestyle='-',label="expert min")
        plt.axhline(y=max(qk_y), color='m', linestyle='--',label="agent max")
        plt.axhline(y=min(qk_y), color='c', linestyle='--',label="agent min")

        plt.legend(loc="best")
        plt.title('1-DOF joint in the y axis (g = 3 step)')
        plt.savefig(proj_path +eps+  'reacher_'+reacher_agent_name+'__y.png')

        #plt.figure()
        #plt.plot(pk[:, 2])
        #plt.axhline(y=max(pk[:, 2]), color='r', linestyle='-')
        #plt.axhline(y=min(pk[:, 2]), color='b', linestyle='-')
        #plt.title('1DOF joint vx axis')
        #plt.savefig(proj_path + 'reacher_3step_30k_pk_vx.png')
#
        #plt.figure()
        #plt.plot(pk[:, 3])
        #plt.axhline(y=max(pk[:, 3]), color='r', linestyle='-')
        #plt.axhline(y=min(pk[:, 3]), color='b', linestyle='-')
        #plt.title('1DOF joint vy axis')
        #plt.savefig(proj_path + 'reacher_3step_30k_pk_vy.png')
