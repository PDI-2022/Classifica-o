from os.path import realpath

import cv2
import os

import join as join

os.mkdir(("C:/Users/neand/PycharmProjects/projetoPDI/" + 'imagens_cortadas'))

path1 = "C:/Users/neand/PycharmProjects/projetoPDI/imagens_cortadas/"
path2 = "C:/Users/neand/PycharmProjects/projetoPDI/lote_de_imagens_PDI/"
path3 = "C:/Users/neand/PycharmProjects/projetoPDI/"

# img1 = cv2.imread("C:/Users/neand/PycharmProjects/projetoPDI/lote_de_imagens_PDI/LOTE 1 R1 INTERNA.jpeg")
# img2 = cv2.imread("C:/Users/neand/PycharmProjects/projetoPDI/lote_de_imagens_PDI/LOTE 1 R1 EXTERNA.jpeg")


# files = [f for f in os.listdir(path2)]
# print(files)

for i in range(1, 11):
    for j in range(1, 3):

            os.chdir(path2)
            img1 = cv2.imread("LOTE " + str(i) + ' R' + str(j) + " INTERNA.jpeg")
            img2 = cv2.imread("LOTE " + str(i) + ' R' + str(j) + " EXTERNA.jpeg")
            if img1 is not None and img2 is not None:
                join.join_image(path1, 'LOTE_' + str(i) + "_R_" + str(j), img1, img2)

            os.chdir(path2)
            img3 = cv2.imread("LOTE " + str(i) + ' R' + str(j) + " T" + " INTERNA.jpeg")
            img4 = cv2.imread("LOTE " + str(i) + ' R' + str(j) + " T" + " EXTERNA.jpeg")
            if img3 is not None and img4 is not None:
                join.join_image(path1, 'LOTE_' + str(i) + "_R_" + str(j) + "_T", img3, img4)



            os.chdir(path2)
            img5 = cv2.imread("LOTE " + str(i) + ' R' + str(j) + " INTERNA.jpg")
            img6 = cv2.imread("LOTE " + str(i) + ' R' + str(j) + " EXTERNA.jpg")
            if img5 is not None and img6 is not None:
                join.join_image(path1, 'LOTE_' + str(i) + "_R_" + str(j), img5, img6)

            os.chdir(path2)
            img7 = cv2.imread("LOTE " + str(i) + ' R' + str(j) + " T" + " INTERNA.jpg")
            img8 = cv2.imread("LOTE " + str(i) + ' R' + str(j) + " T" + " EXTERNA.jpg")
            if img7 is not None and img8 is not None:
                join.join_image(path1, 'LOTE_' + str(i) + "_R_" + str(j) + "_T", img7, img8)


            os.chdir(path2)
            img9 = cv2.imread("LOTE " + str(i) + ' R' + str(j) + " INTERNA.jpeg")
            img10 = cv2.imread("LOTE " + str(i) + ' R' + str(j) + " T" + " C.jpeg")
            if img9 is not None and img10 is not None:
                join.join_image(path1, 'LOTE_' + str(i) + ' R' + str(j) + "INTERNA_T_C", img9, img10)

            os.chdir(path2)
            img11 = cv2.imread("LOTE " + str(i) + ' R' + str(j) + " INTERNA.jpg")
            img12 = cv2.imread("LOTE " + str(i) + ' R' + str(j) + " T" + " C.jpg")
            if img11 is not None and img12 is not None:
                join.join_image(path1, 'LOTE_' + str(i) + ' R' + str(j) + "INTERNA_T_C", img11, img12)



            os.chdir(path2)
            img13 = cv2.imread("LOTE " + str(i) + ' R' + str(j) + " INTERNA.jpeg")
            img14 = cv2.imread("LOTE " + str(i) + ' R' + str(j) + " C.jpeg")
            if img13 is not None and img14 is not None:
                join.join_image(path1, 'LOTE_' + str(i) + ' R' + str(j) + "INTERNA_T_C" + ".jpeg", img13, img14)

            os.chdir(path2)
            img15 = cv2.imread("LOTE " + str(i) + ' R' + str(j) + " INTERNA.jpg")
            img16 = cv2.imread("LOTE " + str(i) + ' R' + str(j) + " C.jpg")
            if img15 is not None and img16 is not None:
                join.join_image(path1, 'LOTE_' + str(i) + ' R' + str(j) + "INTERNA_T_C" + ".jpg", img15, img16)

            os.chdir(path3)

# for i in range(1, 11):
#
#         try:
#             os.chdir("C:/Users/neand/PycharmProjects/projetoPDI/lote_de_imagens_PDI")
#             img1 = cv2.imread("LOTE " + str(i) + ' R' + str(1) + " INTERNA.jpeg")
#             img2 = cv2.imread("LOTE " + str(i) + ' R' + str(1) + " EXTERNA.jpeg")
#             join.join_image(path, 'LOTE_'+str(i) + "R_" + str(i), img1, img2)
#             os.chdir(path)
#             os.chdir("C:/Users/neand/PycharmProjects/projetoPDI/lote_de_imagens_PDI")
#             img3 = cv2.imread("LOTE " + str(i) + ' R' + str(1) + " T" + " INTERNA.jpeg")
#             img4 = cv2.imread("LOTE " + str(i) + ' R' + str(1) + " T" + " EXTERNA.jpeg")
#             join.join_image(path, 'LOTE_'+str(i) + "R_" + str(1) + "_T", img3, img4)
#             os.chdir(path)
#             os.chdir("C:/Users/neand/PycharmProjects/projetoPDI/lote_de_imagens_PDI")
#             img5 = cv2.imread("LOTE " + str(i) + ' R' + str(2) + " INTERNA.jpeg")
#             img6 = cv2.imread("LOTE " + str(i) + ' R' + str(2) + " EXTERNA.jpeg")
#             join.join_image(path, 'LOTE_' + str(i) + "R_" + str(2), img5, img6)
#             os.chdir(path)
#             os.chdir("C:/Users/neand/PycharmProjects/projetoPDI/lote_de_imagens_PDI")
#             img7 = cv2.imread("LOTE " + str(i) + ' R' + str(2) + " T" + " INTERNA.jpeg")
#             img8 = cv2.imread("LOTE " + str(i) + ' R' + str(2) + " T" + " EXTERNA.jpeg")
#             join.join_image(path, 'LOTE_' + str(i) + "R_" + str(2) + "_T", img7, img8)
#             os.chdir(path)
#             os.chdir("C:/Users/neand/PycharmProjects/projetoPDI/lote_de_imagens_PDI")
#             img9 = cv2.imread("LOTE " + str(i) + ' R' + str(1) + " INTERNA.jpeg")
#             img10 = cv2.imread("LOTE " + str(i) + ' R' + str(1) + " T" + " C.jpeg")
#             join.join_image(path, 'LOTE_' + str(i) + "INTERNA_T_C", img9, img10)
#             os.chdir(path)
#             os.chdir("C:/Users/neand/PycharmProjects/projetoPDI/lote_de_imagens_PDI")
#             img11 = cv2.imread("LOTE " + str(i) + ' R' + str(2) + " INTERNA.jpg")
#             img12 = cv2.imread("LOTE " + str(i) + ' R' + str(2) + " T" + " C.jpg")
#             join.join_image(path, 'LOTE_' + str(i) + "INTERNA_T_C", img11, img12)
#             os.chdir(path)
#
#             os.chdir("C:/Users/neand/PycharmProjects/projetoPDI/lote_de_imagens_PDI")
#             img13 = cv2.imread("LOTE " + str(i) + ' R' + str(1) + " INTERNA.jpeg")
#             img14 = cv2.imread("LOTE " + str(i) + ' R' + str(1) + " C.jpeg")
#             join.join_image(path, 'LOTE_' + str(i) + "INTERNA_T_C", img13, img14)
#             os.chdir(path)
#
#             os.chdir("C:/Users/neand/PycharmProjects/projetoPDI/lote_de_imagens_PDI")
#             img15 = cv2.imread("LOTE " + str(i) + ' R' + str(2) + " INTERNA.jpg")
#             img16 = cv2.imread("LOTE " + str(i) + ' R' + str(2) + " C.jpg")
#             join.join_image(path, 'LOTE_' + str(i) +  "INTERNA_T_C", img15, img16)
#             os.chdir(path)
#         except:
#             pass
