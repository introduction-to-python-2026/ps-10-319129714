import matplotlib.pyplot as plt
import numpy as np
from skimage.filters import median
from skimage.morphology import ball
# ייבוא הפונקציות מהקובץ השני [cite: 32]
from image_utils import load_image, edge_detection 

# 1. Load Image [cite: 21]
image_path = 'your_image.jpg' # תחליף לנתיב שלך
original_img = load_image(image_path)

# 2. Remove Noise (Median Filter) [cite: 24, 25]
# הפונקציה הזו מצפה לתמונה באפור או לכל ערוץ בנפרד, וודא התאמה
# הקוד מהמסמך:
clean_img = median(original_img, ball(3)) # שים לב: זה עשוי לדרוש התאמה אם התמונה צבעונית

# 3. Detect Edges 
edges = edge_detection(clean_img)

# 4. Convert to Binary (Thresholding) 
# עליך לבחור ערך סף לפי ההיסטוגרמה. נניח שבחרנו 50
threshold = 50 
binary_edges = edges > threshold

# 5. Show and Save [cite: 30]
plt.imshow(binary_edges, cmap='gray')
plt.show()
plt.imsave('edges_result.png', binary_edges, cmap='gray')
