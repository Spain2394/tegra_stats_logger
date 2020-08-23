#!/usr/local/bin/python3
import numpy as np
import math 
import os
import re
import time
import random
import sys

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count


plt.style.use('seaborn')
duration = 10           # seconds 
line_color = (0,255,0)
block_color = (255,0,0)
window_size = (500,500) # may not be needed

pwr = []
time = []
ram = []
index = count()

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

# parsing info can be found at the link below
# https://forums.developer.nvidia.com/t/source-for-tegrastats-and-or-info-about-querying-overall-gpu-utilization/43000/2
def parse_line(line):
    """
    input: single
    output: power, and gpu utilization
    """
    # RAM X/Y (lfb NxZ), X is memory in MB, Y is total app memory
    ram_str = re.search("RAM\s\d\d\d\d/\d\d\d\d",line)
    # print("memory %s MB" % ram_str.group(0))
    ram_mb_str = re.search("\d\d\d\d",ram_str.group(0))
    ram_mb = int(ram_mb_str.group(0))
    # print(int(ram_mb_str.group(0)))

    # POM_5V_IN represents the total power into the boards
    power_str = re.search("POM_5V_IN\s\d\d\d\d/\d\d\d\d",line)
    power_mw_str = re.search("\d\d\d\d",power_str.group(0))
    pwr_mw = int(power_mw_str.group(0))
    return pwr_mw, ram_mb
    

def get_pwr():
    return pwr
    
# def compute_power_W():
#     """
#     input: single line
#     output: list of 
#     """

#     return power

# def RAM():
#     #    RAM X/Y (lfb NxZ) 
#     """
#     input: single line
#     output: Ram used in MB as a string
    
#     """
#     return true_gpu_util

# def animage(i):
#     pwr.append(next(index))
#     time.append(next(index))

def animate(i):
    try:
        print(datalines[i])
        power, memory = parse_line(datalines[i])
        print("time = %s sec "% i)
        print("power = %s mW "%(power/1000))
        print("memory = %s MB "% memory)
        time.append(i)
        pwr.append(power/1000) # mW to W
        ram.append(memory)
    
        ax1.clear()
        ax2.clear()
        
        ax1.plot(time, pwr, label='Power (W)') # plot x and y values every time called
        ax2.plot(time, ram, label='Ram (MB)',color='green') # plot x and y values every time called

        
        # ax1.set_title('Power plot')
        # ax1.set_xlabel('Time (s)')
        # ax1.legend(loc='upper left')
        # ax2.legend(loc='upper left')
        # ax2.set_title('Memory plot')
        ax2.set_xlabel('Time (s)')
        ax1.set_ylabel('Power (W)')
        ax2.set_ylabel('Memory (MB)')

        ax1.figure.canvas.draw()
        ax2.figure.canvas.draw()

        plt.tight_layout()
        # plt.show()
        
    except IndexError as e:
        print("You've reached the end of the file")
        plt.savefig('./figures/power_ram_plot_1_seaborn.png')
        sys.exit(0)


# gcf get current figure
# interval 1000 which is one second
# the animate is going to run every seconds

    
    #### plot line chart with power as a function of time


    #### plot a bar chart showing GPU utilization out of 100


if __name__ == "__main__":
    # usage tegrastats --interval <int> --logfile <out_file>
    # note interval needs to be equal to --interval 
    ## set your plot style
    f = open("./logs/tegra_stats.log", "r")
    datalines = f.readlines()
    # time.sleep(0.9)
    ani = FuncAnimation(fig, animate, interval = 1000)
    plt.tight_layout()
    plt.show()
    print('---------------------')
    f.close()
    