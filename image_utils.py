from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    pass # Replace the `pass` with your code

def edge_detection(image):import numpy as np
from PIL import Image
from scipy.signal import convolve2d

def load_image(path):
    # 1. Open image using PIL or matplotlib
    img = Image.open(path)
    # 2. Convert to numpy array and return
    return np.array(img)

def edge_detection(image):
    # 1. Convert to grayscale (average of RGB channels)
    # לפי ההוראות: מיצוע שלושת ערכי הצבע [cite: 7]
    gray_image = np.mean(image, axis=2)

    # 2. Define Kernels 
    kernelX = np.array([[1, 0, -1], [2, 0, -2], [1, 0, -1]])
    kernelY = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])

    # 3. Convolve (Apply filters)
    # לפי ההוראות: padding=0 ושמירה על גודל מקורי [cite: 13]
    edgeX = convolve2d(gray_image, kernelX, mode='same', boundary='fill', fillvalue=0)
    edgeY = convolve2d(gray_image, kernelY, mode='same', boundary='fill', fillvalue=0)

    # 4. Calculate Magnitude 
    edgeMAG = np.sqrt(edgeX**2 + edgeY**2)

    return edgeMAG
