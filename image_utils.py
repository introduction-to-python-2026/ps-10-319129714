from PIL import Image
import numpy as np
from scipy.signal import convolve2d

def load_image(path):
    pass # Replace the `pass` with your code

def edge_detection(image):
roi = plt.imread('roi.jpeg')
plt.imshow(roi)
plt.axis('off')
plt.show()
print(roi.shape)
print(roi.dtype)
gray_roi = np.mean(roi, axis=2)

plt.imshow(gray_roi, cmap='gray')
plt.axis('off')
plt.show()

print("Grayscale image shape:", gray_roi.shape)
print("Grayscale image dtype:", gray_roi.dtype)

from scipy.signal import convolve2d
filter = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
filter = filter / np.sum(filter)
filtered_image = convolve2d(gray_roi, filter, mode='same')
fig, axs = plt.subplots(1,2)
axs[0].imshow(gray_roi, cmap='gray')
axs[0].axis('off')
axs[0].set_title('Original Image')
axs[1].imshow(filtered_image, cmap='gray')
axs[1].axis('off')
axs[1].set_title('Filtered Image')
plt.show()
