from imutils import contours
import imutils
import numpy as np
import cv2

def getLines(img):
	#Coloca linhas mais acentuadas
	cv2.rectangle(img, (0,0), (img.shape[1],img.shape[0]), (0,0,0), 1)
	th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 2)	
	edges = cv2.Canny(th, 50,150, apertureSize=3)
	lines = cv2.HoughLinesP(edges, 1, np.pi/180, threshold = 100, minLineLength= 75, maxLineGap=4)

	for line in lines:
		x1,y1,x2,y2 = line[0]
		if(abs(y1-y2) < 10):
			cv2.line(th, (0,y1), (500,y2),(0), 1)

	#Usa o métode erode no sentido horizontal
	kernel = np.ones((1,3), np.uint8)
	th = cv2.erode(th, kernel, iterations=2)
	
	linesY = []
	h, w = img.shape
	print(img.shape)
	i=0
	while(i<h):
		cont = 0
		for j in range(w):
			if(th[i][j]==0):
				cont+=1
		if(w//(1.1)<=cont):
			linesY.append(i)
			i+=h//12	
		i+=1

	linesImg = []
	
	for i in range(1, len(linesY)):
		linesImg.append(img[linesY[i-1]:linesY[i],:])
	return linesImg

def getNumbers(v):
	sudoku = []
	for i in range(9):
		
		th = cv2.adaptiveThreshold(v[i], 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 2)	
		line = []
		h,w = th.shape

		cv2.line(th, (w-1,0), (w-1,500), 0, 3)
		for j in range(0,11):
			cv2.line(th, ((w//9)*(j)+j,0),((w//9)*j+j,500), (0), w//50)
			cv2.imshow('Line ' + str(i), th)

		columnsFront = []
		k = 1
		while(k<w):
			cont=0	
			for j in range(h):	
				cont+=th[j][k]
			if(cont==0):
				columnsFront.append(k)
				k+=w//11
			k+=1

		columnsBack = []
		k=w-2
		while(k>=0):
			cont=0	
			for j in range(h):
				cont+=th[j][k]
			if(cont==0):
				columnsBack.append(k)
				k-=w//11
			k-=1
		columnsBack.reverse()
		print(columnsFront)
		print(columnsBack)
		print(' ')
		for k in range(9):
		 	line.append(th[:,columnsBack[k]:columnsFront[k+1]])
		 	cv2.rectangle(line[k], (0,0), (line[k].shape[1]-2, line[k].shape[0]), (255,255,255),6)
		 	cv2.imshow('Janela '+ str(i) + ' ' + str(k), line[k])

		sudoku.append(line)
	
	return sudoku

def cleanSquare(img):
	h, w = img.shape	
	cv2.rectangle(img, (0,0), (w,h), (255,255,255), 5)
	se = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
	img = cv2.morphologyEx(img, cv2.MORPH_CLOSE, se)
	return img