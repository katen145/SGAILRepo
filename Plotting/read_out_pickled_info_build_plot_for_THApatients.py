import pickle

from DeepMimic_plotter_util import *
import matplotlib.lines as mlines
import matplotlib.pyplot as plt

blue_star = mlines.Line2D([], [], color='blue', marker='*', linestyle='None',
                          markersize=10, label='DM_LB_policy_THA_GT_THA')
red_square = mlines.Line2D([], [], color='red', marker='s', linestyle='None',
                           markersize=10, label='DM_LB_policy_H_GT_THA')
purple_triangle = mlines.Line2D([], [], color='green', marker='+', linestyle='None',
                                markersize=10, label='DM_LB_policy_perfect_fit_H_GT_THA')




def plot_transversal_ROM_pelvis():
    fig = plt.figure()

    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_THA/rom_pelvis_' + str(gc_count) + '.pickle', 'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_transversal[1], ea_hip_ROM_symmetry_transversal[0], 'b*')

    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_THA_policyH5/rom_pelvis_' + str(gc_count) + '.pickle',
                  'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_transversal[1], ea_hip_ROM_symmetry_transversal[0], 'rs')

    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_perfect_fit_THA/rom_pelvis_' + str(gc_count) + '.pickle',
                  'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_transversal[1], ea_hip_ROM_symmetry_transversal[0], 'g+')

    plt.axhline(y=ea_hip_ROM_symmetry_transversal[0], linewidth=0.3, color='black')
    plt.axvline(x=ea_hip_ROM_symmetry_transversal[0], linewidth=0.3, color='black')


    plt.legend(handles=[blue_star, red_square, purple_triangle],loc='best')

    plt.ylabel('Expert Pelvis transversal ROM (degrees)')
    plt.xlabel('Agent Pelvis transversal ROM (degrees)')
    plt.title(' Pelvis transversal ROM (degrees) ')
    plt.savefig('/home/novikova/thesis/SeptemberResults/THA_transversal_ROM_pelvis.png')
    plt.close(fig)


def plot_frontal_ROM_pelvis():
    fig = plt.figure()

    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_THA/rom_pelvis_' + str(gc_count) + '.pickle', 'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_frontal[1], ea_hip_ROM_symmetry_frontal[0], 'b*')

    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_THA_policyH5/rom_pelvis_' + str(gc_count) + '.pickle',
                  'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_frontal[1], ea_hip_ROM_symmetry_frontal[0], 'rs')

    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_perfect_fit_THA/rom_pelvis_' + str(gc_count) + '.pickle',
                  'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_frontal[1], ea_hip_ROM_symmetry_frontal[0], 'g+')

    plt.axhline(y=ea_hip_ROM_symmetry_frontal[0], linewidth=0.3, color='black')
    plt.axvline(x=ea_hip_ROM_symmetry_frontal[0], linewidth=0.3, color='black')

    plt.legend(handles=[blue_star, red_square, purple_triangle],loc='best')
    plt.ylabel('Expert Pelvis frontal ROM (degrees)')
    plt.xlabel('Agent Pelvis frontal ROM (degrees)')
    plt.title(' Pelvis frontal ROM (degrees) ')
    plt.savefig('/home/novikova/thesis/SeptemberResults/THA_frontal_ROM_pelvis.png')
    plt.close(fig)


def plot_saggital_ROM_pelvis():
    fig = plt.figure()
    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_THA/rom_pelvis_' + str(gc_count) + '.pickle', 'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_saggital[1], ea_hip_ROM_symmetry_saggital[0], 'b*')

    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_THA_policyH5/rom_pelvis_' + str(gc_count) + '.pickle',
                  'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_saggital[1], ea_hip_ROM_symmetry_saggital[0], 'rs')

    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_perfect_fit_THA/rom_pelvis_' + str(gc_count) + '.pickle',
                  'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_saggital[1], ea_hip_ROM_symmetry_saggital[0], 'g+')

    plt.plot()
    plt.axhline(y=ea_hip_ROM_symmetry_saggital[0], linewidth=0.3, color='black')

    plt.axvline(x=ea_hip_ROM_symmetry_saggital[0], linewidth=0.3, color='black')
    plt.legend(handles=[blue_star, red_square, purple_triangle],loc='best')

    plt.ylabel('Expert Pelvis saggital ROM (degrees)')
    plt.xlabel('Agent Pelvis saggital ROM (degrees)')
    plt.title(' Pelvis saggital ROM (degrees) ')
    plt.savefig('/home/novikova/thesis/SeptemberResults/THA_saggital_ROM_pelvis.png')
    plt.close(fig)


def plot_pelvis_ROM():
    plot_saggital_ROM_pelvis()
    plot_frontal_ROM_pelvis()
    plot_transversal_ROM_pelvis()



def plot_transversal_hip_ROM_symmetry():
    fig = plt.figure()
    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_THA/rom_' + str(gc_count) + '.pickle', 'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_transversal[1], ea_hip_ROM_symmetry_transversal[0], 'b*')

    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_THA_policyH5/rom_' + str(gc_count) + '.pickle',
                  'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_transversal[1], ea_hip_ROM_symmetry_transversal[0], 'rs')

    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_perfect_fit_THA/rom_' + str(gc_count) + '.pickle',
                  'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_transversal[1], ea_hip_ROM_symmetry_transversal[0], 'g+')

    plt.axhline(y=ea_hip_ROM_symmetry_transversal[0], linewidth=0.3, color='black')
    plt.axvline(x=ea_hip_ROM_symmetry_transversal[0], linewidth=0.3, color='black')


    plt.legend(handles=[blue_star, red_square, purple_triangle],loc='best')
    plt.ylabel('Expert Hip transversal ROM symmetry(degrees)')
    plt.xlabel('Agent Hip transversal ROM symmetry(degrees)')
    plt.title(' Hip transversal ROM symmetry(degrees) ')
    plt.savefig('/home/novikova/thesis/SeptemberResults/THA_transversal_ROM_symmetry.png')
    plt.close(fig)


def plot_frontal_hip_ROM_symmetry():
    fig = plt.figure()
    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_THA/rom_' + str(gc_count) + '.pickle', 'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_frontal[1], ea_hip_ROM_symmetry_frontal[0], 'b*')

    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_THA_policyH5/rom_' + str(gc_count) + '.pickle',
                  'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_frontal[1], ea_hip_ROM_symmetry_frontal[0], 'rs')

    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_perfect_fit_THA/rom_' + str(gc_count) + '.pickle',
                  'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_frontal[1], ea_hip_ROM_symmetry_frontal[0], 'g+')

    plt.axhline(y=ea_hip_ROM_symmetry_frontal[0], linewidth=0.3, color='black')
    plt.axvline(x=ea_hip_ROM_symmetry_frontal[0], linewidth=0.3, color='black')

    plt.legend(handles=[blue_star, red_square, purple_triangle],loc='best')
    plt.ylabel('Expert Hip frontal ROM symmetry(degrees)')
    plt.xlabel('Agent Hip frontal ROM symmetry(degrees)')
    plt.title(' Hip frontal ROM symmetry(degrees) ')
    plt.savefig('/home/novikova/thesis/SeptemberResults/THA_frontal_ROM_symmetry.png')
    plt.close(fig)


def plot_saggital_hip_ROM_symmetry():
    fig = plt.figure()
    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_THA/rom_' + str(gc_count) + '.pickle', 'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_saggital[1], ea_hip_ROM_symmetry_saggital[0], 'b*')

    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_THA_policyH5/rom_' + str(gc_count) + '.pickle',
                  'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_saggital[1], ea_hip_ROM_symmetry_saggital[0], 'rs')

    for gc_count in range(5):
        with open('/home/novikova/thesis/SeptemberResults/DM_LB_perfect_fit_THA/rom_' + str(gc_count) + '.pickle',
                  'rb') as f:
            ea_hip_ROM_symmetry_frontal, ea_hip_ROM_symmetry_transversal, ea_hip_ROM_symmetry_saggital = pickle.load(f)
            plt.plot(ea_hip_ROM_symmetry_saggital[1], ea_hip_ROM_symmetry_saggital[0], 'g+')

    plt.plot()
    plt.axhline(y=ea_hip_ROM_symmetry_saggital[0], linewidth=0.3, color='black')

    plt.axvline(x=ea_hip_ROM_symmetry_saggital[0], linewidth=0.3, color='black')
    plt.legend(handles=[blue_star, red_square, purple_triangle],loc='best')

    plt.ylabel('Expert Hip saggital ROM symmetry(degrees)')
    plt.xlabel('Agent Hip saggital ROM symmetry(degrees)')
    plt.title(' Hip saggital ROM symmetry(degrees) ')
    plt.savefig('/home/novikova/thesis/SeptemberResults/THA_saggital_ROM_symmetry.png')
    plt.close(fig)

def plot_hip_symmetry():
    plot_saggital_hip_ROM_symmetry()
    plot_frontal_hip_ROM_symmetry()
    plot_transversal_hip_ROM_symmetry()


plot_hip_symmetry()
plot_pelvis_ROM()




