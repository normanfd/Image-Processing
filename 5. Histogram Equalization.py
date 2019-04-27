import matplotlib.pyplot as plt
import cv2
import numpy as np

img = cv2.imread("car.png",0)
row, col = img.shape

# print(np.array(frek))
max= np.max(img)
min= np.min(img)

def ContrastStreching(img,max,min):
    row, col = img.shape  # mengambil nilai dimensi dari "gambar"
    canvas = np.zeros((row, col, 1), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            hasil = ((img[i,j]-min)/(max-min))*255
            canvas.itemset((i,j,0), hasil)
    return canvas

def HistogramChannel(img):
    plt.hist(img.ravel(), 256, [0, 256])
    return plt.show()

def equalization(img):
    row, col = img.shape
    nilaiPixel = [0]*256
    BIN = 256
    canvas = np.zeros((row,col,1), np.uint8)
    #Standard Histogram = hitung banyaknya kemunculan tiap intensitas keabuan
    for i in range(0, row):
        for j in range(0, col):
            index = int(img[i, j])
            nilaiPixel[index] += 1
    #Normalized Histogram = Peluang nilai kemunculan setiap nilai derajat keabuan
    for i in range(0, BIN):
        nilaiPixel[i] = float(nilaiPixel[i])/float(row*col)
    #Histogram Kumulatif
    for i in range(0, BIN):
        nilaiPixel[i] = nilaiPixel[i] + nilaiPixel[i - 1]
    #Histogram Equalization
    for i in range(0, BIN):
        nilaiPixel[i] = nilaiPixel[i] * (BIN - 1)
    #memasukan nilai-nilai pixel di atas ke kanvas
    for i in range(0, row):
        for j in range(0, col):
            index = int(img[i, j])
            pixel = nilaiPixel[index]
            canvas.itemset((i,j,0), pixel)

    return canvas
#Citra Original
cv2.imshow("citra original",img)
HistogramChannel(img)

#Contrastreching
contraststrech=ContrastStreching(img,max,min)
cv2.imshow("Hasil ContrastStreching",contraststrech)
HistogramChannel(contraststrech)

#Histogram Equalization
equalization = equalization(img)
cv2.imshow("Hasil Equalization", equalization)
HistogramChannel(equalization)


cv2.waitKey(0)
cv2.destroyAllWindows()
# bit.ly/prak5pcd