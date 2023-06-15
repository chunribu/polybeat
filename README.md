# Polybeat



https://github.com/chunribu/polybeat/assets/57521167/1bad0cd3-3feb-4222-8fea-8398ac4c3689



## Installation
```shell
# first, install manim from conda-forge channel
conda install -c conda-forge manim

# then install polybeat from pypi
pip install polybeat
```

## Usage
```python
# step 1: import module
from polybeat import play

# step 2:
# primary usage
play([3,4,12])

# advanced usage
play(
    rhythms=[3,4,6,12],
    custom_order=None,
    colors=[RED,YELLOW,BLUE,GREEN],
    sounds=['kick_drum','open_conga','side_stick','low_bongo'],
    volumes=[0,-2,-6,-4],
    cycle_time=1.8,
    dot_radius=0.16,
    width_range=[2.5,3.5],
    preview=True,
)
```

`custom_order` is None by default, which equals [0,1,2,3] in this case.

`colors` should be a list of variables supported by manim or hex number strings, e.g. ['#3ec1d3', '#f6f7d7', '#ff9a00', '#ff165d'].

`sounds` can be paths to custom audio files, or just leave it default.

`cycle_time` has an effect on speed.

`preview` means you want the video to auto play or not after rendering.

>It's safe to use default parameters when the number of beats is 4 or less
