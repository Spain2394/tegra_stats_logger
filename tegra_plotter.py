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

# plt.style.use('fivethirtyeight') # also a good theme
plt.style.use('seaborn')

pwr = []
time = []
ram = []
index = count()

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

# tegra stats format information found below
# https://docs.nvidia.com/jetson/archives/l4t-archived/l4t-3231/index.html#page/Tegra%2520Linux%2520Driver%2520Package%2520Development%2520Guide%2FAppendixTegraStats.html%23
# https://forums.developer.nvidia.com/t/source-for-tegrastats-and-or-info-about-querying-overall-gpu-utilization/43000/2
def parse_line(line):
    """
    input: str line from tegrastats log file
    output: int power in MB, and memory usage in MB
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
        
    except IndexError as e:
        print("You've reached the end of the file")
        plt.savefig('./figures/power_ram_plot_1_seaborn.png')
        sys.exit(0)

if __name__ == "__main__":
    # note interval needs to be equal to --interval 
    f = open("./logs/tegra_stats.log", "r")
    datalines = f.readlines()
    ani = FuncAnimation(fig, animate, interval = 1000)
    plt.tight_layout()
    plt.show()
    f.close()
    