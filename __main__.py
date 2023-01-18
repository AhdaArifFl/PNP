import cv2 as ocv
from matplotlib import pyplot as plt

img = ocv.imread('tnkb/baru.jpg')
cop = ocv.cvtColor(img, ocv.COLOR_BGR2GRAY)
cop = ocv.GaussianBlur()

plt.subplot(2,1,1)
plt.imshow(ocv.cvtColor(img, ocv.COLOR_BGR2RGB))
plt.subplot(2,1,2)
plt.imshow(ocv.cvtColor(cop, ocv.COLOR_BGR2RGB))

plt.show()