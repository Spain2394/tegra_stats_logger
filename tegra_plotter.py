#!/usr/local/bin/python3

import numpy as np
import math 
import os
import re
import time as clock
import random
import sys

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import argparse

# plt.style.use('fivethirtyeight') # also a good theme
plt.style.use('seaborn')

pwr = []
time = []
ram = []
index = count()
duration = 10
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)

JETSON_NANO = False
JETSON_TX2 = True

def parse_args():
    """Parse input arguments."""
    parser = argparse.ArgumentParser(description='tegra_stats_plotter')
    parser.add_argument("--log_path", help="path to tegra log", type=str, default='/Volumes/HSKY-BCKUP/YOLO/plotting_tools/logs/tegra_stats_now.log')
    parser.add_argument("--duration", help="Amount of time to plot data", type=int, default=None)
    args = parser.parse_args()
    return args

# tegra stats format datasheets found below
# https://docs.nvidia.com/jetson/archives/l4t-archived/l4t-3231/index.html#page/Tegra%2520Linux%2520Driver%2520Package%2520Development%2520Guide%2FAppendixTegraStats.html%23
# https://forums.developer.nvidia.com/t/source-for-tegrastats-and-or-info-about-querying-overall-gpu-utilization/43000/2
def parse_line(line):
    """
    input: str line from tegrastats log file
    output: int power in MB, and memory usage in MB
    """
    # RAM X/Y (lfb NxZ), X is memory in MB, Y is total app memory
    ram_str = re.search("RAM\s\d\d\d\d/\d\d\d\d",line)
    ram_mb_str = re.search("\d\d\d\d",ram_str.group(0))
    ram_mb = int(ram_mb_str.group(0))

    # POM_5V_IN represents the total power into the boards
    # TODO there should be a better way to do this
    if JETSON_NANO: # Max Power 10,000 mW
        power_str = re.search("POM_5V_IN\s\d\d\d\d/\d\d\d\d",line)
        power_mw_str = re.search("\d\d\d\d",power_str.group(0))
        pwr_mw = int(power_mw_str.group(0))
    elif JETSON_TX2: ### MAX Power can be 12000 mW 
        power_str = re.search("VDD_IN\s\d\d\d\d/\d\d\d\d",line)
        if power_str is None:
            power_str = re.search("VDD_IN\s\d\d\d\d\d/\d\d\d\d",line)
            power_mw_str = re.search("\d\d\d\d\d",power_str.group(0))
        else:
            power_mw_str = re.search("\d\d\d\d",power_str.group(0))
        pwr_mw = int(power_mw_str.group(0))
    else: 
        print("JETSON ")
        pwr_mw = 0

    return pwr_mw, ram_mb

def animate(i):
    try:
        if duration is None or i <= duration:
            print(datalines[i])
            power, memory = parse_line(datalines[i])
            print("time = %s sec "% i)
            print("power = %s W "%(power/1000))
            print("memory = %s MB "% memory)
            time.append(i)
            pwr.append(power/1000) # mW to W
            ram.append(memory)
        
            ax1.clear()
            ax2.clear()
            
            ax1.plot(time, pwr, label='Power (W)') # plot x and y values every time called
            ax2.plot(time, ram, label='Ram (MB)',color='green') # plot x and y values every time called

            ax2.set_xlabel('Time (s)')
            ax1.set_ylabel('Power (W)')
            ax2.set_ylabel('Memory (MB)')

            ax1.figure.canvas.draw()
            ax2.figure.canvas.draw()
            plt.tight_layout()
        else:
            plt.savefig('/Volumes/HSKY-BCKUP/YOLO/plotting_tools/figures/tx2/yolov4_benchmark_small.png')
            sys.exit(0)
    except (IndexError, KeyboardInterrupt) as e:
        print("You've reached the end of the file")
        plt.savefig('/Volumes/HSKY-BCKUP/YOLO/plotting_tools/figures/tx2/yolov4_benchmark_small.png')
        clock.sleep(1)
        sys.exit(0)

if __name__ == "__main__":
    
    args = parse_args()
    duration = args.duration
    f = open(args.log_path, "r")
    datalines = f.readlines()

    # make interval larger if you are reading the file too fast
    # tegra stats default update rate = 1000 ms
    ani = FuncAnimation(fig, animate, interval = 1000)
    plt.tight_layout()
    plt.show()
    f.close()
    
