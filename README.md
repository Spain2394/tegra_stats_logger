# tegra_stats_plotter

#### Usage
Run tegrastats and store results to file:
```tegrastats --interval 1 --logfile ./logs/tegra_stats.log```

Next run python script: 
```python3 tegra_plotter.py```

#### Output example
<img src="./figures/
power_ram_plot_1_seaborn.png" width=600>

#### System tests
-Setup Jetson Nano, no monitor running tegra stats and piping to a remote machine

### JETSON NANO
#### test videos form test set: UGA 2015, UGA 2018
[UGA 2015](/Volumes/HSKY-BCKUP/YOLO/data/UGA2015/test_videos/UGA_2015_V14.mp4)

[UGA 2018](/Volumes/HSKY-BCKUP/YOLO/data/UGA2018/test_videos/UGA_2018_V9.mp4)

Terminal 1 : ```$ tegrastats```
Terminal 2 : ```$ plotter```

--------------------------
#### yolov3-tiny-big
<img src="/Volumes/HSKY-BCKUP/YOLO/plotting_tools/figures/yolov3_benchmark_big.png" width=600>
```AVG_FPS = 0.7```

#### yolov4-tiny-big
<img src="/Volumes/HSKY-BCKUP/YOLO/plotting_tools/figures/yolov4_benchmark_big.png" width=600>
```AVG_FPS = 0.8```

----------------------------------------------------
#### yolov3-tiny-med
<img src="/Volumes/HSKY-BCKUP/YOLO/plotting_tools/figures/yolov3_benchmark_med.png" width=600>
```AVG_FPS = 2.7```

#### yolov4-tiny-med
<img src="/Volumes/HSKY-BCKUP/YOLO/plotting_tools/figures/yolov4_benchmark_med.png" width=600>
```AVG_FPS = 3.0```

----------------------------------------------------
#### yolov3-tiny-small
<img src="/Volumes/HSKY-BCKUP/YOLO/plotting_tools/figures/yolov3_benchmark_small.png" width=600>
```AVG_FPS = 5.6```

#### yolov4-tiny-small
<img src="/Volumes/HSKY-BCKUP/YOLO/plotting_tools/figures/yolov4_benchmark_small.png" width=600>
```AVG_FPS = 6.2```

### JETSON TX2
#### test videos form test set: UGA 2015, UGA 2018
[UGA 2015](/Volumes/HSKY-BCKUP/YOLO/data/UGA2015/test_videos/UGA_2015_V14.mp4)

[UGA 2018](/Volumes/HSKY-BCKUP/YOLO/data/UGA2018/test_videos/UGA_2018_V9.mp4)

Terminal 1 : ```$ tegrastats```
Terminal 2 : ```$ plotter```

--------------------------
#### yolov3-tiny-big
<img src="/Volumes/HSKY-BCKUP/YOLO/plotting_tools/figures/tx2/yolov3_benchmark_big.png" width=600>
```AVG_FPS = 9.7```

#### yolov4-tiny-big
<img src="/Volumes/HSKY-BCKUP/YOLO/plotting_tools/figures/tx2/yolov4_benchmark_big.png" width=600>
```AVG_FPS = 5.5```

----------------------------------------------------
#### yolov3-tiny-med
<img src="/Volumes/HSKY-BCKUP/YOLO/plotting_tools/figures/tx2/yolov3_benchmark_med.png" width=600>
```AVG_FPS = 35.8```

#### yolov4-tiny-med
<img src="/Volumes/HSKY-BCKUP/YOLO/plotting_tools/figures/tx2/yolov4_benchmark_med.png" width=600>
```AVG_FPS = 19.8```

----------------------------------------------------
#### yolov3-tiny-small
<img src="/Volumes/HSKY-BCKUP/YOLO/plotting_tools/figures/tx2/yolov3_benchmark_small.png" width=600>
```AVG_FPS = 75.1```

#### yolov4-tiny-small
<img src="/Volumes/HSKY-BCKUP/YOLO/plotting_tools/figures/tx2/yolov4_benchmark_small.png" width=600>
```AVG_FPS = 39.5```
