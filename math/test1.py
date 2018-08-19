# coding=gbk
from PIL import Image
import numpy as np
# import scipy
import matplotlib.pyplot as plt


def ImageToMatrix(filename):
    # ��ȡͼƬ
    im = Image.open(filename)
    # ��ʾͼƬ
    #     im.show()
    width, height = im.size
    im = im.convert("L")
    data = im.getdata()
    data = np.matrix(data, dtype='float') / 255.0
    new_data = np.reshape(data, (width, height))
    return new_data


#     new_im = Image.fromarray(new_data)
#     # ��ʾͼƬ
#     new_im.show()
def MatrixToImage(data):
    data = data * 255
    new_im = Image.fromarray(data.astype(np.uint8))
    return new_im


filename = '11.jpg'
data = ImageToMatrix(filename)
print
data
print(len(data))
new_im = MatrixToImage(data)
plt.imshow(data, cmap=plt.cm.gray, interpolation='nearest')
# new_im.show()
# new_im.save('22.jpg')