'''
開啟並顯示圖片
這篇教學會介紹 OpenCV 裡 imread()、imshow()、waitKey() 方法，透過這些方法，在電腦中使用不同的色彩模式開啟圖片並顯示圖片。
'''
import cv2                    # 匯入 OpenCV 函式庫
# img = cv2.imread(r'02//meme.jpg')  # 讀取圖片
img = cv2.imread(r'02//meme.jpg', cv2.IMREAD_COLOR)  # 使用 別的 模式




cv2.imshow('cute cat :)))))', img)  
cv2.waitKey(0)                 # 按下任意鍵停止
cv2.destroyAllWindows()        # 結束所有圖片視窗