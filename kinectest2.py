from mine import *
import math,time
mc = Minecraft()

rotX=-130
rotY=0
distance=15

def line(x1,y1,z1,x2,y2,z2,blck):
    m1 = (y2-y1)/(x2-x1-.00001)
    m2 = (y2-y1)/(z2-z1-.00001)
    
    for e in range(int(math.floor(math.sqrt(((x2-x1-.00001)**2)+((y2-y1)**2))))):
        mc.setBlock(round(x1),round(y1)+100,0*round(z1),blck)
        x1=x1-(1/(math.sqrt((m1**2)+1)))
        y1=y1-(m1/(math.sqrt((m1**2)+1)))
        z1=z1-(m2/(math.sqrt((m2**2)+1)))
    mc.setBlock(x2,y2+100,0*z2,blck)
    

def plotX(x,y,z,a1,a2,d):
    return (y*math.sin(a1)*math.sin(a2))-(z*math.sin(a2)*math.cos(a1))+(x*math.cos(a2))

def plotY(x,y,z,a1,a2,d):
    return (y*math.cos(a1))+(z*math.sin(a1))

def plotZ(x,y,z,a1,a2,d):
    return (z*math.cos(a1)*math.cos(a2))-(y*math.sin(a1)*math.cos(a2))+(x*math.sin(a2))

def polygon(points,rotX=rotX,rotY=rotY,distance=distance):
    pointNum=int(len(points)/3)
    for x in range(pointNum):
        x*=3
        line(plotX(points[x-3],points[x-2],points[x-1],rotX,rotY,distance),plotY(points[x-3],points[x-2],points[x-1],rotX,rotY,distance),plotZ(points[x-3],points[x-2],points[x-1],rotX,rotY,distance),plotX(points[x],points[x+1],points[x+2],rotX,rotY,distance),plotY(points[x],points[x+1],points[x+2],rotX,rotY,distance),plotZ(points[x],points[x+1],points[x+2],rotX,rotY,distance),block.GOLD_BLOCK)

while True:
    for rotX1 in range(-3600,3600):
        size=5
        rotX1/=30
        rotY1=rotX1
        rotX2=-rotX1+360
        rotY2=-rotY1+180
        polygon([size,size,size,size,size,-size,size,-size,-size,size,-size,size],rotX1,rotY1)
        polygon([-size,size,size,-size,size,-size,-size,-size,-size,-size,-size,size],rotX1,rotY1)
        polygon([size,size,size,-size,size,size],rotX1,rotY1)
        polygon([size,size,-size,-size,size,-size],rotX1,rotY1)
        polygon([size,-size,-size,-size,-size,-size],rotX1,rotY1)
        polygon([size,-size,size,-size,-size,size],rotX1,rotY1)
        time.sleep(.25)
        mc.setBlocks(-10,90,-10,10,110,10,0)
