import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
count=0
image=Image.open('Googleimage.png')
#image.show()
text=pytesseract.image_to_string(image)
print(text)
for x in text:
	count=count+1
print(count)

