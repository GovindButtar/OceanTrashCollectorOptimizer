import os
import webbrowser
import matplotlib.pyplot as plt
from lib.remus100 import remus100
from lib.plotTimeSeries import *
from lib.mainloop import simulate, simulatePos
# Simulation parameters: 
sampleTime = 0.02                   # sample time [seconds]
N = 10000                           # number of samples
currentPos = [90, 90, 0.0, 0.0]
# 3D plot and animation parameters where browser = {firefox,chrome,safari,etc.}
numDataPoints = 50                  # number of 3D data points
FPS = 10                            # frames per second (animated GIF)
filename = '3D_animation.gif'       # data file for animated GIF
browser = 'safari'          
vehicle = remus100('depthHeadingAutopilot',90,90,1525,0.0, 0.0) #30, 50, 1525, 0.5, 170
def main():    
    
    [simTime, simData] = simulate(N, sampleTime, vehicle)
    
    plotVehicleStates(simTime, simData, 1)                    
    plotControls(simTime, simData, vehicle, 2)
    plot3D(simData, numDataPoints, FPS, filename, 3)   
    
    """ Ucomment the line below for 3D animation in the web browswer. 
    Alternatively, open the animated GIF file manually in your preferred browser. """
    # webbrowser.get(browser).open_new_tab('file://' + os.path.abspath(filename))
    
   
    vehicle.setTargetDepthAndHeading(70,70)
    [simTime, simData] = simulatePos(N, sampleTime, vehicle, currentPos[0], currentPos[1], currentPos[2], currentPos[3])
    plotVehicleStates(simTime, simData, 1)                    
    plotControls(simTime, simData, vehicle, 2)
    plot3D(simData, numDataPoints, FPS, filename, 3)  
    plt.show()
    plt.close()
    
main()