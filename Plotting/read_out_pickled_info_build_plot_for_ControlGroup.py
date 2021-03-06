import pickle

from DeepMimic_plotter_util import *
import matplotlib.lines as mlines
import matplotlib.pyplot as plt

blue_star = mlines.Line2D([], [], color='blue', marker='*', linestyle='None',
                          markersize=10, label='DM_LB_policy_H_GT_H')
red_square = mlines.Line2D([], [], color='red', marker='s', linestyle='None',
                           markersize=10, label='DM_LB_policy_perfect_fit_H_GT_H')



def plot_transversal_ROM_pelvis():
    fig = plt.figure()
    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB/rom_pelvis_' + str(gc_count) + '.pickle', 'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_transversal[1], ea_hip_ROM_symmetry_transversal[0], 'b*')
    expert_ROM_sym_transversal = ea_hip_ROM_symmetry_transversal[0]
    plt.axhline(y=ea_hip_ROM_symmetry_transversal[0], linewidth=0.3, color='black')
    plt.axvline(x=ea_hip_ROM_symmetry_transversal[0], linewidth=0.3, color='black')
    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_perfect_fit/rom_pelvis_' + str(gc_count) + '.pickle',
                  'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_transversal[1], expert_ROM_sym_transversal, 'rs')
    # plt.text(ea_hip_ROM_symmetry_transversal[0]+0.1,ea_hip_ROM_symmetry_transversal[0]+0.01, 'expert hip ROM symmetry',rotation=90)
    plt.legend(handles=[blue_star, red_square],loc='best')
    plt.ylabel('Expert Pelvis transversal ROM (degrees)')
    plt.xlabel('Agent Pelvis transversal ROM (degrees)')
    plt.title(' Pelvis transversal ROM (degrees) ')
    plt.savefig('/home/novikova/thesis/SeptemberResults/control_group_transversal_ROM_pelvis.png')
    plt.close(fig)


def plot_frontal_ROM_pelvis():
    fig = plt.figure()
    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB/rom_pelvis_' + str(gc_count) + '.pickle', 'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_frontal[1], ea_hip_ROM_symmetry_frontal[0], 'b*')
    expert_ROM_sym_frontal = ea_hip_ROM_symmetry_frontal[0]
    plt.axhline(y=ea_hip_ROM_symmetry_frontal[0], linewidth=0.3, color='black')
    plt.axvline(x=ea_hip_ROM_symmetry_frontal[0], linewidth=0.3, color='black')
    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_perfect_fit/rom_pelvis_' + str(gc_count) + '.pickle',
                  'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_frontal[1], expert_ROM_sym_frontal, 'rs')
    # plt.text(ea_hip_ROM_symmetry_frontal[0]+ 0.05,ea_hip_ROM_symmetry_frontal[0] +0.001, 'expert hip ROM symmetry',rotation=90)
    plt.legend(handles=[blue_star, red_square],loc='best')
    plt.ylabel('Expert Pelvis frontal ROM (degrees)')
    plt.xlabel('Agent Pelvis frontal ROM (degrees)')
    plt.title(' Pelvis frontal ROM (degrees) ')
    plt.savefig('/home/novikova/thesis/SeptemberResults/control_group_frontal_ROM_pelvis.png')
    plt.close(fig)


def plot_saggital_ROM_pelvis():
    fig = plt.figure()
    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB/rom_pelvis_' + str(gc_count) + '.pickle', 'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_saggital[1], ea_hip_ROM_symmetry_saggital[0], 'b*')
    expert_ROM_sym_sag = ea_hip_ROM_symmetry_saggital[0]
    plt.axhline(y=ea_hip_ROM_symmetry_saggital[0], linewidth=0.3, color='black')
    plt.axvline(x=ea_hip_ROM_symmetry_saggital[0], linewidth=0.3, color='black')
    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_perfect_fit/rom_pelvis_' + str(gc_count) + '.pickle',
                  'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_saggital[1], expert_ROM_sym_sag, 'rs')
    # plt.text(ea_hip_ROM_symmetry_saggital[0]-1,ea_hip_ROM_symmetry_saggital[0]+0.01, 'expert hip ROM symmetry',rotation=90)
    plt.legend(handles=[blue_star, red_square],loc='best')
    plt.ylabel('Expert Pelvis saggital ROM (degrees)')
    plt.xlabel('Agent Pelvis saggital ROM (degrees)')
    plt.title(' Pelvis saggital ROM (degrees) ')
    plt.savefig('/home/novikova/thesis/SeptemberResults/control_group_saggital_ROM_pelvis.png')
    plt.close(fig)

def plot_pelvis_ROM():
    plot_saggital_ROM_pelvis()
    plot_frontal_ROM_pelvis()
    plot_transversal_ROM_pelvis()



def plot_transversal_hip_ROM_symmetry():
    fig = plt.figure()
    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB/rom_' + str(gc_count) + '.pickle', 'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_transversal[1], ea_hip_ROM_symmetry_transversal[0], 'b*')
    expert_ROM_sym_transversal = ea_hip_ROM_symmetry_transversal[0]
    plt.axhline(y=ea_hip_ROM_symmetry_transversal[0], linewidth=0.3, color='black')
    plt.axvline(x=ea_hip_ROM_symmetry_transversal[0], linewidth=0.3, color='black')
    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_perfect_fit/rom_' + str(gc_count) + '.pickle',
                  'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_transversal[1], expert_ROM_sym_transversal, 'rs')
    # plt.text(ea_hip_ROM_symmetry_transversal[0]+0.1,ea_hip_ROM_symmetry_transversal[0]+0.01, 'expert hip ROM symmetry',rotation=90)
    plt.legend(handles=[blue_star, red_square],loc='best')
    plt.ylabel('Expert Hip transversal ROM symmetry(degrees)')
    plt.xlabel('Agent Hip transversal ROM symmetry(degrees)')
    plt.title(' Hip transversal ROM symmetry(degrees) ')
    plt.savefig('/home/novikova/thesis/SeptemberResults/control_group_transversal_ROM_symmetry.png')
    plt.close(fig)


def plot_frontal_hip_ROM_symmetry():
    fig = plt.figure()
    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB/rom_' + str(gc_count) + '.pickle', 'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_frontal[1], ea_hip_ROM_symmetry_frontal[0], 'b*')
    expert_ROM_sym_frontal = ea_hip_ROM_symmetry_frontal[0]
    plt.axhline(y=ea_hip_ROM_symmetry_frontal[0], linewidth=0.3, color='black')
    plt.axvline(x=ea_hip_ROM_symmetry_frontal[0], linewidth=0.3, color='black')
    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_perfect_fit/rom_' + str(gc_count) + '.pickle',
                  'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_frontal[1], expert_ROM_sym_frontal, 'rs')
    # plt.text(ea_hip_ROM_symmetry_frontal[0]+ 0.05,ea_hip_ROM_symmetry_frontal[0] +0.001, 'expert hip ROM symmetry',rotation=90)
    plt.legend(handles=[blue_star, red_square],loc='best')
    plt.ylabel('Expert Hip frontal ROM symmetry(degrees)')
    plt.xlabel('Agent Hip frontal ROM symmetry(degrees)')
    plt.title(' Hip frontal ROM symmetry(degrees) ')
    plt.savefig('/home/novikova/thesis/SeptemberResults/control_group_frontal_ROM_symmetry_.png')
    plt.close(fig)


def plot_saggital_hip_ROM_symmetry():
    fig = plt.figure()
    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB/rom_' + str(gc_count) + '.pickle', 'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_saggital[1], ea_hip_ROM_symmetry_saggital[0], 'b*')
    expert_ROM_sym_sag = ea_hip_ROM_symmetry_saggital[0]
    plt.axhline(y=ea_hip_ROM_symmetry_saggital[0], linewidth=0.3, color='black')
    plt.axvline(x=ea_hip_ROM_symmetry_saggital[0], linewidth=0.3, color='black')
    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_perfect_fit/rom_' + str(gc_count) + '.pickle',
                  'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_saggital[1], expert_ROM_sym_sag, 'rs')
    # plt.text(ea_hip_ROM_symmetry_saggital[0]-1,ea_hip_ROM_symmetry_saggital[0]+0.01, 'expert hip ROM symmetry',rotation=90)
    plt.legend(handles=[blue_star, red_square],loc='best')
    plt.ylabel('Expert Hip saggital ROM symmetry(degrees)')
    plt.xlabel('Agent Hip saggital ROM symmetry(degrees)')
    plt.title(' Hip saggital ROM symmetry(degrees) ')
    plt.savefig('/home/novikova/thesis/SeptemberResults/control_group_saggital_ROM_symmetry.png')
    plt.close(fig)

def plot_hip_symmetry():
    plot_saggital_hip_ROM_symmetry()
    plot_frontal_hip_ROM_symmetry()
    plot_transversal_hip_ROM_symmetry()


plot_hip_symmetry()
plot_pelvis_ROM()