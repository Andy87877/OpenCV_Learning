'''
寫入並儲存圖片
這篇教學會介紹 OpenCV 裡的 imwrite() 方法，實現將圖片另存新檔 ( 也可轉檔 ) 的功能。

後面是我亂玩得XD
'''

import cv2
import numpy as np #儲存陣列產生的圖片 
import random #隨機生成顏色


# imwrite() 寫入並儲存圖片
img = cv2.imread(r'03//cute.jpg', cv2.IMREAD_GRAYSCALE)   # 以灰階模式開啟圖片
cv2.imwrite(r'03//cute_2.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 80])  # 存成 jpg
cv2.imwrite(r'03//cute_3.png', img)  # 存成 png



# 儲存陣列產生的圖片 
img = np.zeros((500,500,3), dtype='uint8')   # 快速產生 500x500，每個項目為 [0,0,0] 的三維陣列
# img[150:350, 150:350] = [0,0,255]  # 將中間 200x200 的每個項目內容，改為 [0,0,255]


path = r'03//mid_color.jpg'

for i in range(2500):
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    a, b = random.randint(0+int(i*0.1), 250),random.randint(250, int(500-i*0.1))
    c, d =random.randint(0+int(i*0.1), 250),random.randint(250, int(500-i*0.1))
    img[a:b , c:d] = [R,G,B]
    cv2.imwrite(path, img)       # 存成 jpg
    cv2.imshow(path, img)        # 顯示圖片
    # cv2.waitKey(0)               # 按下任意鍵停止
    cv2.waitKey(1)             # 等待 毫秒 後

cv2.destroyAllWindows()
