from scipy import stats
from matplotlib import pyplot as plt
from agent import *
import statsmodels.api as sm
import scipy
import math

episode_path = '/home/novikova/thesis/'

from numpy import load
#poses from 10 episodes
def qet_qpos_i(index):
    for i in range(1):
        agent_file = "/home/novikova/thesis/vid_walker_3step_473k" + str(i) + ".npz"
        data = load(agent_file, allow_pickle=True)
        episode_poses = data['qpos']

body_part_dict = {
    0: 'root0',
    1: 'root1',
    2: 'root2',
    3: 'right_hip',
    4: 'right_knee',
    5: 'right_foot',
    6: 'left_hip',
    7: 'left_knee',
    8: 'left_foot'
}

agent_file = "/home/novikova/thesis/vid_walker_3step_473k9.npz"
expert_file = "/home/novikova/thesis/yhealthy_zx_P05.npz"
ep="ep_9"
agent_data = load(agent_file, allow_pickle=True)
expert_data = load(expert_file, allow_pickle=True)
agent_episode_poses = agent_data['qpos']
expert_episode_poses = expert_data['qpos'][:,:,:9][0]
bin_amount=10
indexes_expert = [f for f in range(120)]
indexes_agent = [f for f in range(120)]
for qpos_ind in range(9):
    samples_qk=agent_episode_poses[:120,qpos_ind]
    samples_pk=expert_episode_poses[:120,qpos_ind]
    fig = plt.figure()
    bins = np.histogram(np.hstack((samples_qk, samples_pk)), bins=bin_amount)[1]  # get the bin edges
    plt.hist(samples_pk, bins, alpha=0.5, density=True, label='expert')
    plt.hist(samples_qk, bins, alpha=0.5, density=True, label='agent')
    plt.grid(True)
    plt.legend(loc="best")
    plt.title('Probability Distribution')
    plt.xlabel(
        'joint movement ' + str(body_part_dict[qpos_ind]))
    plt.ylabel('Likelihood occurence')
    plt.savefig(episode_path + '_PDF_'+ep+body_part_dict[qpos_ind]+'.png')



    # plot cdf for agent and expert
    fig = plt.figure()
    n1, bins1, patches1 = plt.hist(samples_qk, bin_amount, density=True, histtype='step', cumulative=True,
                                   label='agent')
    n2, bins2, patches2 = plt.hist(samples_pk, bin_amount, density=True, histtype='step', cumulative=True,
                                   label='expert')
    plt.grid(True)
    plt.legend(loc="best")
    plt.title('Cumulative step histograms')
    plt.xlabel(
        'joint movement ' + str(body_part_dict[qpos_ind]))
    plt.ylabel('Likelihood occurence')
    plt.savefig(
        episode_path + '_CDF_' +ep+ body_part_dict[qpos_ind] + '.png')
    plt.close(fig)

    # computing the perfect sample size for the k-s test
    supremum_of_cdfs_d = scipy.spatial.distance.minkowski(n1, n2, p=float('inf'))
    alpha = supremum_of_cdfs_d / 1.358
    sample_size = int(2 / (alpha * alpha))
    samples_pk_indexes = np.random.choice(indexes_expert, sample_size)
    samples_qk_indexes = np.random.choice(indexes_agent, sample_size)
    if sample_size > len(indexes_expert):
        tiler = math.ceil(sample_size / len(indexes_expert))
        samples_pk = np.tile(samples_pk, tiler)
    samples_pk = samples_pk[samples_pk_indexes]
    samples_qk = samples_qk[samples_qk_indexes]

    res = stats.ks_2samp(samples_pk, samples_qk)
    if res.pvalue < 0.05:
        print("significant difference, null hypothesis rejected ", res.pvalue)
        fig = plt.figure()
        bplot1 = plt.boxplot([samples_qk, samples_pk],
                             vert=True,  # vertical box alignment
                             patch_artist=True,  # fill with color
                             labels=['agent', 'expert'])  # will be used to label x-ticks
        colors = ['pink', 'lightblue']
        for patch, color in zip(bplot1['boxes'], colors):
            patch.set_facecolor(color)
        plt.ylabel('values')
        plt.title('Box plots of ' + body_part_dict[qpos_ind])
        plt.savefig(
            episode_path + '/box_plot_REJECTED_' +ep+ str(res.pvalue) + body_part_dict[qpos_ind] + '.png')
        plt.close(fig)
    else:
        print("hypothesis accepted, similar enough distributions ", res.pvalue)
        fig = plt.figure()
        bplot1 = plt.boxplot([samples_qk, samples_pk],
                             vert=True,  # vertical box alignment
                             patch_artist=True,  # fill with color
                             labels=['agent', 'expert'])  # will be used to label x-ticks
        colors = ['pink', 'lightblue']
        for patch, color in zip(bplot1['boxes'], colors):
            patch.set_facecolor(color)
        plt.ylabel('values')
        plt.title('Box plots of ' + body_part_dict[qpos_ind])
        plt.savefig(
            episode_path + '/box_plot_ACCEPTED_' +ep+ str(res.pvalue) + body_part_dict[qpos_ind] +'.png')
        plt.close(fig)

    # plot BA plot for agent and expert
    fig = plt.figure()
    sm.graphics.mean_diff_plot(samples_qk, samples_pk)
    plt.savefig(
        episode_path + '_BA_' +ep+  body_part_dict[qpos_ind] + '.png')
    plt.close(fig)
