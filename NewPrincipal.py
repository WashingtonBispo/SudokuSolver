from imutils.perspective import four_point_transform
from imutils import contours
import imutils
import numpy as np
import cv2
import Func
import Detector
import Solver
kernal = np.ones((2,2), np.uint8)

#Charge the photo them resize
img = cv2.imread('Modelo10.jpg')
img = imutils.resize(img, height=500)
cv2.imshow('Sudoku', img)

#Get the Edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 0)
edges = cv2.Canny(blur, 50, 150, 255)

cnts = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)

displayCnt = None

for c in cnts:
	#Aproximate the contour
	peri = cv2.arcLength(c, True)
	approx = cv2.approxPolyDP(c, 0.02*peri, True)

	if(len(approx) == 4):
		displayCnt = approx
		break

#Sudoku Extraído

warped = four_point_transform(gray, displayCnt.reshape(4,2))
blur = cv2.GaussianBlur(warped, (5,5), 0)

#Vai receber um vetor com as coordenadas Y das linhas
lines = Func.getLines(blur)
	
if(len(lines) == 9):
	sudoku = Func.getNumbers(lines)

sudokuList = Detector.defineNumbers(sudoku)
Solver.solve(sudokuList)

cv2.waitKey(0)
cv2.destroyAllWindows()
