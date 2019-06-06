# plotMouseMovements

Plot raw mouse data.
For example if you pass as input a copy of '/dev/input/mice' it will replay everything done on a plot.


# Usage

usage: plotMouseMovements.py [-h] [--scale [SCALE]] [--speed [SPEED]]
                             [--click [0;1]]
                             inputfile [inputfile ...]

positional arguments:
  inputfile        the input file (raw mouse data, e.g. from /dev/input/mice)

optional arguments:
  -h, --help       show this help message and exit
  --scale [SCALE]  set the scale of the plot
  --speed [SPEED]  set the speed of the drawing
  --click [0;1]    update plot relative to mouse clicks; (1 = Update on mouse
                   clicks, 0 = Do NOT update on mouse clicks)
                   
                   
# Usage

Here's an example of a recent CTF (in this example, the image was updated every letter)

![alt text](https://github.com/regi18/plotMouseMovements/blob/master/example.jpg)
