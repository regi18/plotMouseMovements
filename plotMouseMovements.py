"""
Plot raw mouse data using matplotlib
For example if you pass as input a copy of '/dev/input/mice' it will replay everything done on a plot.
Created by: regi18
Version: 3.0.0
Github: https://github.com/regi18/plotMouseMovements
"""
import struct
import matplotlib.pyplot as plt
import argparse


xList = [0]
yList = [0]
data = [[0,0,0]]


# Sets the arguments (launch the program with --help to see them better)
parser = argparse.ArgumentParser()
parser.add_argument("inputfile", help="the input file (raw mouse data, e.g. from /dev/input/mice). Default name = \"mouse.bin\"", nargs="?", type=str, default=["mouse.bin"])
parser.add_argument('--speed', "-s", help="set the pause between updates (in seconds)", nargs="?",type=float, default=0.1)
parser.add_argument('--color', "-c", help="set the color of the plot (b = blue, g = green, r = red, c = cyan, m = magenta, y = yellow, k = black, w = white)", nargs="?",type=str, default="c")
args = parser.parse_args()

f = open( args.inputfile[0], "rb" ); 

# Gets the mouse informations from the file (b = button, x = x coordinate, y = y coordinate)
def getMouseEvent():
  b, x, y = struct.unpack('3b',f.read(3))
  data.append([x + (data[len(data)-1][0]), y + (data[len(data)-1][1]), b & 0x1])


try:
  while True:
    getMouseEvent()
finally:
  # Enable interactive mode (matplotlib)
  plt.ion()
  
  # Iterate over the mouse data
  for a,i in enumerate(data):
    # if left button clicked, append the data to these new lists
    if i[2] == 1:
      xList.append(i[0])
      yList.append(i[1])
    # if the left button wasn't press, but in the cycle before it was, updates the canvas
    elif data[a-1][2] == 1:
      plt.plot(xList, yList, args.color+",")
      plt.pause(args.speed)
   
  # Disable interactive mode, and leave plot open
  plt.ioff() 
  plt.show()
  f.close()
  exit()

