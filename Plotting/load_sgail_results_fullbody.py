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
import os

proj_path = '/home/novikova/thesis/'
result_path = '/home/novikova/thesis/SeptemberResults/SGAIL_FB/'
if not os.path.exists(result_path):
    os.makedirs(result_path)


# poses from 10 episodes
def get_episode_data(i):
    agent_file = proj_path + "vid_cmu_55k" + str(i) + ".npz"
    data = load(agent_file, allow_pickle=True)
    episode_poses = data['qpos']
    return episode_poses


cmu_expert = proj_path + "cmu_mocap.npz"


def plot_right_hip_data(pk, qk):
    pk_x = pk[:, 2]
    pk_y = pk[:, 1]
    pk_z = pk[:, 0]
    qk_x = qk[:, 2]
    qk_y = qk[:, 1]
    qk_z = qk[:, 0]

    fig = plt.figure()
    plt.plot(pk_x, color="g", label="expert")
    plt.plot(qk_x, color="y", label="agent")
    plt.axhline(y=max(pk_x), color='r', linestyle='-', label="expert max")
    plt.axhline(y=min(pk_x), color='b', linestyle='-', label="expert min")
    plt.axhline(y=max(qk_x), color='m', linestyle='--', label="agent max")
    plt.axhline(y=min(qk_x), color='c', linestyle='--', label="agent min")
    plt.legend(loc="best")
    plt.ylabel('Joint angle (degrees)')

    plt.title('Right hip movement along the saggital plane')
    plt.savefig(result_path + eps + 'cmu_mocap_r_hip_saggital.png')
    plt.close(fig)

    fig = plt.figure()
    plt.plot(pk_y, color="g", label="expert")
    plt.plot(qk_y, color="y", label="agent")
    plt.axhline(y=max(pk_y), color='r', linestyle='-', label="expert max")
    plt.axhline(y=min(pk_y), color='b', linestyle='-', label="expert min")
    plt.axhline(y=max(qk_y), color='m', linestyle='--', label="agent max")
    plt.axhline(y=min(qk_y), color='c', linestyle='--', label="agent min")
    plt.legend(loc="best")
    plt.ylabel('Joint angle (degrees)')
    plt.title('Right hip movement along the frontal plane')
    plt.savefig(result_path + eps + 'cmu_mocap_r_hip_frontal.png')
    plt.close(fig)

    fig = plt.figure()
    plt.plot(pk_z, color="g", label="expert")
    plt.plot(qk_z, color="y", label="agent")
    plt.axhline(y=max(pk_z), color='r', linestyle='-', label="expert max")
    plt.axhline(y=min(pk_z), color='b', linestyle='-', label="expert min")
    plt.axhline(y=max(qk_z), color='m', linestyle='--', label="agent max")
    plt.axhline(y=min(qk_z), color='c', linestyle='--', label="agent min")
    plt.legend(loc="best")
    plt.ylabel('Joint angle (degrees)')

    plt.title('Right hip movement along the transversal plane')
    plt.savefig(result_path + eps + 'cmu_mocap_r_hip_transversal.png')
    plt.close(fig)

    print_out_ROM(qk_x, pk_x, 'right hip saggital', eps)
    print_out_ROM(qk_y, pk_y, 'right hip frontal', eps)
    print_out_ROM(qk_z, pk_z, 'right hip transversal', eps)


def print_out_ROM(samples_qk, samples_pk, text, ep):
    file1 = open(
        result_path + "/_rom_ep_" + ep + ".txt", "a")
    file1.write("======================================================= \n")
    file1.write(text + " \n")
    min_agent_degrees = min(samples_qk)* 180 / math.pi
    max_agent_degrees = max(samples_qk)* 180 / math.pi
    ROM = max_agent_degrees - min_agent_degrees
    file1.write('agent rom ' + str(ROM) + "\n")
    min_expert_degrees = min(samples_pk)* 180 / math.pi
    max_expert_degrees = max(samples_pk)* 180 / math.pi
    ROM = max_expert_degrees - min_expert_degrees
    file1.write('expert rom ' + str(ROM) + "\n")
    file1.close()  # to change file access modes


def plot_left_hip_data(pk, qk):
    pk_x = pk[:, 2]
    pk_y = pk[:, 1]
    pk_z = pk[:, 0]
    qk_x = qk[:, 2]
    qk_y = qk[:, 1]
    qk_z = qk[:, 0]

    fig = plt.figure()
    plt.plot(pk_x, color="g", label="expert")
    plt.plot(qk_x, color="y", label="agent")
    plt.axhline(y=max(pk_x), color='r', linestyle='-', label="expert max")
    plt.axhline(y=min(pk_x), color='b', linestyle='-', label="expert min")
    plt.axhline(y=max(qk_x), color='m', linestyle='--', label="agent max")
    plt.axhline(y=min(qk_x), color='c', linestyle='--', label="agent min")
    plt.ylabel('Joint angle (degrees)')

    plt.legend(loc="best")
    plt.title('Left hip movement along the saggital plane')
    plt.savefig(result_path + eps + 'cmu_mocap_l_hip_saggital.png')
    plt.close(fig)

    fig = plt.figure()
    plt.plot(pk_y, color="g", label="expert")
    plt.plot(qk_y, color="y", label="agent")
    plt.axhline(y=max(pk_y), color='r', linestyle='-', label="expert max")
    plt.axhline(y=min(pk_y), color='b', linestyle='-', label="expert min")
    plt.axhline(y=max(qk_y), color='m', linestyle='--', label="agent max")
    plt.axhline(y=min(qk_y), color='c', linestyle='--', label="agent min")
    plt.ylabel('Joint angle (degrees)')

    plt.legend(loc="best")
    plt.title('Left hip movement along the frontal plane')
    plt.savefig(result_path + eps + 'cmu_mocap_l_hip_frontal.png')
    plt.close(fig)

    fig = plt.figure()
    plt.plot(pk_z, color="g", label="expert")
    plt.plot(qk_z, color="y", label="agent")
    plt.axhline(y=max(pk_z), color='r', linestyle='-', label="expert max")
    plt.axhline(y=min(pk_z), color='b', linestyle='-', label="expert min")
    plt.axhline(y=max(qk_z), color='m', linestyle='--', label="agent max")
    plt.axhline(y=min(qk_z), color='c', linestyle='--', label="agent min")
    plt.ylabel('Joint angle (degrees)')

    plt.title('Left hip movement along the transversal plane')
    plt.savefig(result_path + eps + 'cmu_mocap_l_hip_transversal.png')
    plt.close(fig)

    print_out_ROM(qk_x, pk_x, 'left hip saggital', eps)
    print_out_ROM(qk_y, pk_y, 'left hip transversal', eps)
    print_out_ROM(qk_z, pk_z, 'left hip transversal', eps)


if (__name__ == '__main__'):
    sns.set()
    data_comparison = list()
    samples = 100
    traj_data = np.load(cmu_expert, allow_pickle=True)
    qpos_list = traj_data['qpos']
    qpos_list = qpos_list[0][:, :]
    qpos_list_cmu_expert = qpos_list[:samples, :63]
    cmu_expert_l_hip = qpos_list_cmu_expert[:, 7:10]
    cmu_expert_r_hip = qpos_list_cmu_expert[:, 14:17]

    for episode in range(9):
        eps = "_ep" + str(episode) + "_"
        cmu_agent = get_episode_data(episode)
        cmu_agent = cmu_agent[:samples, :]
        qpos_list_cmu_agent = cmu_agent[:samples, :63]

        # got the full data from agent and expert humanoid data
        # need to get the hip ROM, knee ROM, foot ROM

        cmu_agent_l_hip = qpos_list_cmu_agent[:, 7:10]
        cmu_agent_r_hip = qpos_list_cmu_agent[:, 14:17]
        rhip_agent,lhip_agent=[],[]
        rhip_expert,lhip_expert=[],[]

        for i in range(cmu_agent_l_hip.shape[0]):
            rhip_agent.append(radian_to_degree(np.array(cmu_agent_r_hip[i, :])))
            lhip_agent.append(radian_to_degree(np.array(cmu_agent_l_hip[i, :])))

        for i in range(cmu_expert_l_hip.shape[0]):
            lhip_expert.append(radian_to_degree(np.array(cmu_expert_l_hip[i, :])))

        for i in range(cmu_expert_r_hip.shape[0]):
            rhip_expert.append(radian_to_degree(np.array(cmu_expert_r_hip[i, :])))



        plot_right_hip_data(np.array(rhip_expert), np.array(rhip_agent))
        plot_left_hip_data(np.array(lhip_expert), np.array(lhip_agent))
