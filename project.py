from os.path import realpath

import cv2
import os

import join as join
path1 = "C:\\Users\cezar\OneDrive\Documentos\PDI - CLASSIFICACAO\Classificacao\imagens_cortadas\\"
path2 = "C:\\Users\cezar\OneDrive\Documentos\PDI - CLASSIFICACAO\Classificacao\lote_de_imagens_PDI"

for i in range(1, 11):
    for j in range(1, 3):

            os.chdir(path2)
            img1 = cv2.imread("LOTE " + str(i) + ' R2' + " INTERNA.jpg")
            if img1 is not None:
                join.join_image(path1, 'LOTE_INTERNO_' + str(i) + "_R2", img1)

            os.chdir(path2)

for i in range(1, 11):
            j = 1
            os.chdir(path2)

            img2 = cv2.imread("LOTE " + str(i) + ' R' + str(j) +" EXTERNA.jpg")
            if img2 is not None:
                join.join_image(path1, 'LOTE_EXTERNO_' + str(i) + "_R1", img2)
            os.chdir(path2)
