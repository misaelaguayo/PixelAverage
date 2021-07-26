import numpy as np
from PIL import Image
import glob
import time
import ctypes
import os

numpy_vars = []
for np_name in glob.glob('*.np[yz]'):
    numpy_vars.append(np.load(np_name))
    os.remove(np_name)

numpyCount = len(numpy_vars)
print("number of files found: " + str(len(numpy_vars)))

tmp = sum(numpy_vars)
timestr = time.strftime("%Y%m%d-%H%M%S")

errorCode = ctypes.windll.shcore.SetProcessDpiAwareness(2)
w, h = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)
print(w,h)

start_time = time.time()
dataZero = np.zeros((w, h, 3), dtype=np.uint8)

for i in range(w):
    for j in range(h):
        r,g,b = [a // numpyCount for a in tmp[i,j]]
        dataZero[i,j] = [r,g,b]
            

img = Image.fromarray(dataZero, 'RGB')
img.save('pixelAverage.png')
np.save("PixelAverage" + timestr, dataZero)
print("Time elapsed: " + str(time.time() - start_time))
