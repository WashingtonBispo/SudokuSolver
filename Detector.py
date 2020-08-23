import pytesseract
import cv2
import Func

def retireNoise(s):
	if(s == ''):
		return 0;
	for i in s:
		if (ord(i) > ord('0')  and ord(i) <= ord('9')):
			return(int(i)- int(0))

def defineNumbers(orig):
	pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
	custom_config = r'--oem 3 --psm 6 outputbase digits'
	
	v = []
	for i in range(len(orig)):
		aux = []
		for j in range(len(orig[i])):
			img = Func.cleanSquare(orig[i][j])
			cv2.imshow('Janela ' + str(i) + ' ' + str(j),img)
			s = pytesseract.image_to_string(img, config=custom_config)
			aux.append(retireNoise(s))
		v.append(aux)
		
	return(v)

