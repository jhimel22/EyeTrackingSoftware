from unicodedata import name
import numpy as np
import matplotlib.pyplot as p
import sys
import threading
import random as r


lfw = np.load("lfwcrop.npy")
# input(lfw)
face = lfw[r.randint(0,len(lfw))]
# print(len(face))x
p.imshow(face)
p.show()
