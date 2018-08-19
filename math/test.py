from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def getMatrix(index):
    np.set_printoptions(threshold=np.inf)
    im = Image.open('./image/'+index+'.bmp')
    width, height = im.size
    im = im.convert('1')
    data = im.getdata()
    new_data = np.reshape(data, (height, width))
    return new_data
def getIndex(index):
    str1 = ''
    if index<10:
        str1= '00'+str(index)
    else :
        str1 =  '0'+str(index)
    return str1
templist = []
for index in range(0,19):
    templist.append(getIndex(index))

for k in templist:
    getMatrix(k)

def MatrixToImage(data):
    data = data
    new_im = Image.fromarray(data.astype(np.uint8))
    return new_im
#=======================================
ii = 0;
shuzhi = '008'
templist.remove(shuzhi)
testshuzhi=[shuzhi]
while (len(templist) >0):
    count = 0
    ii=ii+1
    data10 = getMatrix(shuzhi)
    data11 = ((data10[:, (len(data10[0]) - 1)]).tolist())
    for k in templist:
        data13 = getMatrix(k)[:,0].tolist()
        bb =0
        for i ,v in enumerate(data13):
            if(v == data11[i] ==0):
                bb=bb+1
        if(bb > count):
            count=bb
            shuzhi = k

    if(len(templist)>0):
        if shuzhi in templist:
            templist.remove(shuzhi)
            testshuzhi.append(shuzhi)
testdata=[]
for v in testshuzhi:
    testdata = testdata+ np.transpose(getMatrix(v)).tolist()

arr = np.array(testdata).transpose()
print(len(arr))
new_im = MatrixToImage(arr)
plt.imshow(arr, cmap=plt.cm.gray, interpolation='nearest')
new_im.show()
new_im.save('221.jpg')






