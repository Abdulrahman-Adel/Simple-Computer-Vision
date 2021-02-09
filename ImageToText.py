import cv2
import pytesseract
import re



def prep_img(frame):
    
    img_cvt = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #img_cvt = cv2.blur(img_cvt,(1,2))
    #img_cvt = cv2.GaussianBlur(img_cvt,(3,3),1)
    img_cvt = cv2.medianBlur(img_cvt,5)
    #img_cvt = cv2.bilateralFilter(img_cvt,9,75,75)
    #img_cvt = cv2.adaptiveThreshold(img_cvt, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 5, 4)
    
    return img_cvt
    
def Extract_text(frame):
    
    boxes = pytesseract.image_to_data(frame,lang="ara") 
    for x,b in enumerate(boxes.splitlines()):
        if x != 0:
            b = b.split("\t")
            if re.match(r"[A-Za-z0-9]+",b[-1]):
                x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9])
                cv2.rectangle(img, (x,y), (w+x,h+y), (0, 255, 255), 2)
            
    string = pytesseract.image_to_string(frame,lang="ara")            

    return string.strip()       

if __name__ == "__main__":
        
        img_path = "IMG_5957.jpg"
        img = cv2.imread(img_path)
        img = cv2.resize(img, (600,400), interpolation = cv2.INTER_AREA)  
        #hImg,wImg,_ = img.shape
        
        img_cvt = prep_img(img)
        print(Extract_text(img_cvt))
        
        
        cv2.imshow("result",img)
        
        
cv2.waitKey(0)
cv2.destroyAllWindows()

