import cv2
import os
import numpy
import mahotas

def binarizar(imagem):
	img = cv2.imread(imagem)
	# cv2.imshow("img", img)
	# cv2.waitKey()
	#
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# cv2.imshow("img", img_gray)
	# cv2.waitKey()
	#Passo 2: Blur/Suavização da imagem
	img_suave = cv2.blur(img_gray, (7, 7))
	# cv2.imshow("img", img_suave)
	# cv2.waitKey()

	T = mahotas.thresholding.otsu(img_suave)
	bin = img_suave.copy()
	bin[bin > T] = 255
	bin[bin < 255] = 0
	bin = cv2.bitwise_not(bin)
	# cv2.imshow("img", bin)
	# cv2.waitKey()
	#Passo 4: Detecção de bordas com Canny
	bordas = cv2.Canny(bin, 70, 150)
	# cv2.imshow("img", bordas)
	# cv2.waitKey()
	#
	return bordas