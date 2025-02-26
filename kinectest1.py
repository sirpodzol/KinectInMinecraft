from mine import *
import math,time
mc = Minecraft()
mc.postToChat("Hellorld")
playerPos = mc.player.getPos()
mc.setBlock(0,120,0,block.DIAMOND_BLOCK)

rotX=-130
rotY=0
distance=15

def line(x1,y1,x2,y2,blck):
    try:
        m=(y2-y1)/(x2-x1)
    except:
        mc.setBlock(x1,y1,0,blck)
        mc.setBlock(x1,y2,0,blck)
        if y1>y2:
            for y in range(y2,y1):
                mc.setBlock(x1,y,0,blck)
        else:
            for y in range(y1,y2):
                mc.setBlock(x1,y,0,blck)
    else:
        if x2>x1:
            temp=x1
            x1=x2
            x2=temp
            temp=y1
            y1=y2
            y2=temp
        for e in range(int(math.floor(math.sqrt(((x2-x1)**2)+((y2-y1)**2))))):
            mc.setBlock(round(x1),round(y1),0,blck)
            x1=x1-(1/(math.sqrt((m**2)+1)))
            y1=y1-(m/(math.sqrt((m**2)+1)))
        mc.setBlock(x2,y2,0,blck)

def functionZ(x,y,z,a1,a2):
    return math.cos(a2)*y*math.sin(a1+x)-math.sin(a2)*z

def plotCylinX(x,y,z,a1=-130,a2=-20,d=5):
    return (d/(d-functionZ(x,y,z,a1,a2)))*y*math.cos(a1+x)

def plotCylinY(x,y,z,a1=-130,a2=-20,d=5):
    return d/(d-functionZ(x,y,z,a1,a2))*(y*math.sin(a2)*math.sin(a1+x)+z*math.cos(a2))

def plotCartX(x,y,z,a1=-130,a2=-20,d=5):
    return round(15+(2*plotCylinX(math.atan2(y,x),math.sqrt(x**2+y**2),z,a1,a2,d)))
           
def plotCartY(x,y,z,a1=-130,a2=-20,d=5):
    return round(15+(2*plotCylinY(math.atan2(y,x),math.sqrt(x**2+y**2),z,a1,a2,d)))

def polygon(points,rotX=rotX,rotY=rotY,distance=distance):
    pointNum=int(len(points)/3)
    for x in range(pointNum):
        x*=3
        line(plotCartX(points[x-3],points[x-2],points[x-1],rotX,rotY,distance),plotCartY(points[x-3],points[x-2],points[x-1],rotX,rotY,distance)+100,plotCartX(points[x],points[x+1],points[x+2],rotX,rotY,distance),plotCartY(points[x],points[x+1],points[x+2],rotX,rotY,distance)+100,block.GOLD_BLOCK)

while True:
    for rotX1 in range(-3600,3600):
        size=4
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
        time.sleep(.1)
        mc.setBlocks(-10,90,0,50,150,0,block.AIR)
