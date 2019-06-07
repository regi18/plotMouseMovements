# Plot Mouse Movements

Plot raw mouse data.
For example if you pass as input a copy of '/dev/input/mice' it will replay everything done on a plot.


# Usage

usage: plotMouseMovements.py [-h] [--speed [SPEED]] [--color [COLOR]]
                             [inputfile]
```
positional arguments:
  inputfile             the input file (raw mouse data, e.g. from
                        /dev/input/mice). Default name = "mouse.bin"

optional arguments:
  -h, --help            show this help message and exit
  --speed [SPEED], -s [SPEED]
                        set the pause between updates (in seconds)
  --color [COLOR], -c [COLOR]
                        set the color of the plot (b = blue, g = green, r =
                        red, c = cyan, m = magenta, y = yellow, k = black, w =
                        white)
```
# Built With
* [Matplotlib](https://matplotlib.org/) (pip3 install -U matplotlib)
   * Option 2: [Turtle](https://docs.python.org/3.3/library/turtle.html) (apt install python3-tk & pip3 install turtle)
* [Python](https://www.python.org/) (apt install python3)
                   
# Example

Here's an example of a recent CTF (in this example, the image was updated every letter)  
```Matplotlib```
![alt text](https://github.com/regi18/plotMouseMovements/blob/master/matplotlibexample.jpg)  
```Turtle```
![alt text](https://github.com/regi18/plotMouseMovements/blob/master/example.jpg)
```In this case the flag was:  FLAG_7RXDNT52K6P```

# May be useful
* [hexascii2bin](https://github.com/regi18/hexascii2bin)
