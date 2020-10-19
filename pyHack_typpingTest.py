import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import pyscreenshot as ImageGrab
from webbot import Browser
import time

pytesseract.pytesseract.tesseract_cmd = 'D:/Programmes/Tesseract/tesseract.exe'
web = Browser()
web.go_to('https://10fastfingers.com/typing-test/english')
time.sleep(6)
# part of the screen
for i in range(60):
    im=ImageGrab.grab(bbox=(433,352,1403,396))
    im.save('test.jpg')

    im = Image.open("test.jpg") # Ouverture du fichier image
     
    # Filtrage (augmentation du contraste)
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
     
    # Lancement de la procédure de reconnaissance
    text = pytesseract.image_to_string(im)
    print(text)
    web.type(text)
    web.type(' ')
    time.sleep(5)


