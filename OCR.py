import  pytesseract
import  cv2
from PIL import Image

img_path= "D:/OCRresim/"

pytesseract.pytesseract.tesseract_cmd = "C:/Program Files (x86)/Tesseract-OCR/tesseract"
def donustur(path):
    img = Image.open(path)
    result = pytesseract.pytesseract.image_to_string(img,lang='tur')
    print(result)

def goruntule(path):
    image = cv2.imread(path)
    cv2.namedWindow("pencere", cv2.WINDOW_AUTOSIZE)
    cv2.imshow("pencere",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

donustur(img_path+"download.png")
goruntule(img_path+"download.png")