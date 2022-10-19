import numpy as np
import cv2
import mahotas
import os
from binarizacao import binarizar


def regiaoROI(path1, pasta1, pasta2, h, w, x, y):
	for i in range(1000):
		img = cv2.imread(path1 + str(i) + ".jpg")
		
		linhas, colunas = img.shape[:2]
		
		##primeiro ponto
		x1 = int(linhas - x)
		y1 = int(colunas - y)
		
		##segundo ponto
		y2 = int(y1 + w)
		x2 = int(x1 + h)
		
		## recorte da imagem
		roi = img[x1:x2, y1:y2]
		# cv2.imshow('roi', roi)
		# cv2.waitKey()
		
		fileName = "C:/Users/neand/PycharmProjects/avaliacaoFinalCienciaDeDados/" + str(pasta1)
		
		# print('image %d' % i)
		
		# cv2.rectangle(img, (x2, y2), (x2 + w, y2 + h), (0, 255, 0), 2)
		
		os.chdir("C:/Users/neand/PycharmProjects/avaliacaoFinalCienciaDeDados/" + str(pasta1))
		cv2.imwrite(fileName + '/frameRecortado_' + str(i) + ".jpg", roi)
		
		# os.chdir("C:/Users/neand/PycharmProjects/avaliacaoFinalCienciaDeDados/" + str(pasta))
		img1 = binarizar("C:/Users/neand/PycharmProjects/avaliacaoFinalCienciaDeDados/" + str(pasta1)
		                    + '/frameRecortado_' + str(i) + ".jpg")
		os.chdir("C:/Users/neand/PycharmProjects/avaliacaoFinalCienciaDeDados/"+str(pasta2))
		cv2.imwrite(("C:/Users/neand/PycharmProjects/avaliacaoFinalCienciaDeDados/"+ str(pasta2)
		                    + '/frameBin_' + str(i) + ".jpg"), img1)
		
		os.chdir("C:/Users/neand/PycharmProjects/avaliacaoFinalCienciaDeDados")
		cv2.destroyAllWindows()
