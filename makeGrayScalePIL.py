from PIL import Image
from matplotlib import pyplot as plt

img = Image.open('3.JPG').convert('LA')
plt.imshow(img)
plt.show()
img.save('3_1.png')