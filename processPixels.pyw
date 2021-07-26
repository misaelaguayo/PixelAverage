import ctypes
from PIL import ImageGrab
from PIL import Image
import numpy as np
import time

errorCode = ctypes.windll.shcore.SetProcessDpiAwareness(2)

w, h = ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)

timestr = time.strftime("%Y%m%d-%H%M%S")
start_time = time.time()
img = ImageGrab.grab().load()

dataZero = np.zeros((w, h, 3))

start_time = time.time()
for i in range(w):
    for j in range(h):
        r, g, b = list(img[i,j])
        dataZero[i, j] = [r, g, b]
dataZero = dataZero[::-1]


np.save("PixelAverage" + timestr, dataZero)
