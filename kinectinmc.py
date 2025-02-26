import freenect,time,colors
from mine import *
mc = Minecraft()
size = 8
while True:
    depth = freenect.sync_get_depth()
    img = freenect.sync_get_video()
    time.sleep(1)
    for y in range (int(round(len(depth[0]))/size)):
        for x in range(int(round(len(depth[0][0]))/size)):
            mc.setBlocks(x,58-y,(2048/size/4)+10,x,58-y,0,0)
            mc.setBlock(x,58-y,int(round(depth[0][y*size][x*size]/size/2)),colors.rgbToBlock(img[0][y*size][x*size]))  
