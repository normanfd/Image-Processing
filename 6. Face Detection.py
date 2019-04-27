import cv2
import numpy as np
#membaca gambar FACE DETECTION.png
img = cv2.imread("FACE DETECTION.png")
#fungsi mengubah gambar RGB ke HSV
def RGBtoHSV(img):
    # mengambil nilai dimensi dari "gambar"
    row, col, ch = img.shape
    # bikin kanvas kosong dengan 3 elemen
    canvas = np.zeros((row, col, 3), np.uint8)
    for i in range(0, row):
        for j in range(0,col):
            b,g,r = img[i,j]
            b = int(b)
            g = int(g)
            r = int(r)
            v = max(b,g,r)
            # assign s dan h = 0 jika maks dari v == 0
            if v == 0:
                s = 0
                h = 0
            else:
                #ngitung s
                s = (float(v-min(b,g,r))/v)
                # ngitung h
                if v == min(b,g,r):
                    h = 0
                else:
                    if v == r:
                        h = 60 * (g - b) / (v - min(b, g, r))
                    elif v == g:
                        h = 120 + 60 * (b - r) / (v - min(b, g, r))
                    else :
                        h = 240 + 60 * (r - g) / (v - min(b, g, r))
                    if h < 0:
                        h+=360
                # convert hasil hsv ke angka rgb untuk ditampilkan di layar, kecuali v, karena v=red atau green atau blue (sudah rgb)
                s = int(s * 255)
                h = int(h / 2)
            # assignment ke kanvas baru masing2 elemennya (0 for h, 1 for s, 2 for v)
            canvas.itemset((i, j, 0), h)
            canvas.itemset((i, j, 1), s)
            canvas.itemset((i, j, 2), v)
    return canvas
#memanggil fungsi convert RGB ke HSV
convertcsv = RGBtoHSV(img)
#menampilkan hasil convert dari RGB ke HSV
cv2.imshow("Hasil RGB to CSV",convertcsv)
#######################################################################################################################

def FacDetection(img):
    # mengambil nilai dimensi dari "gambar"
    row,col,ch = img.shape
    # bikin kanvas kosong dengan 3 elemen
    canvas = np.zeros((row,col,3),np.uint8)
    for i in range(0,row):
        for j in range (0,col):
            intensitas= img[i,j]
            # nilai 19<H<240 berdasarkan artikel yg terlampir di dalam folder, katanya: kalau lebih atau kurang dari angka2 itu -> bukan kulit manusia
            if (intensitas[0]>19 and intensitas[0]<240):
                intensitas[0]=0
                intensitas[1]=0
                intensitas[2]=0
            # assignment ke kanvas baru masing2 elemennya (0 for h, 1 for s, 2 for v)
            canvas.itemset((i,j,0), intensitas[0])
            canvas.itemset((i,j,1), intensitas[1])
            canvas.itemset((i,j,2), intensitas[2])
    return canvas

#fungsi untuk mengubah gambar HSV ke RGB
def HSVtoRGB(image):
    row, col, ch = image.shape
    #bikin kanvas kosong dengan 3 elemen
    kanvas = np.zeros((row, col, 3), np.uint8)
    for i in range(0, row):
        for j in range(0, col):
            h, s, v = image[i, j]
            h = h*2
            s = s/255
            v = v/255
            c = v * s
            x = c * (1 - abs(((h/60) % 2) -1))
            m = v - c
            r, g, b = 0, 0, 0
            #hitung rgb
            if(h>=0 and h<60):
                r, g, b = c, x, 0
            elif(h>=60 and h<120):
                r, g, b = x, c, 0
            elif(h>=120 and h<180):
                r, g, b = 0, c, x
            elif(h>=180 and h<240):
                r, g, b = 0, x, c
            elif(h>=240 and h<300):
                r, g, b = x, 0, c
            elif(h>=300 and h<360):
                r, g, b = c, 0, x
            #convert hasil di atas ke angka rgb untuk ditampilkan di layar
            r, g, b = (r+m)*255, (g+m)*255, (b+m)*255
            #assignment ke kanvas baru masing2 elemennya (0 for h, 1 for s, 2 for v)
            kanvas.itemset((i, j, 0), b)
            kanvas.itemset((i, j, 1), g)
            kanvas.itemset((i, j, 2), r)
    return kanvas
#memanggil fungsi face detection dari gambar yang telah diconvert ke HSV
FaceDetect = FacDetection(convertcsv)
#memanggil fungsi HSV to RGB untuk membuat output face detection menjadi gambar RGB
HasilFaceDetection = HSVtoRGB(FaceDetect)
cv2.imshow("Hasil Face Detection", HasilFaceDetection)

cv2.waitKey(0)
cv2.destroyAllWindows()
#bit.ly/prak6pcd