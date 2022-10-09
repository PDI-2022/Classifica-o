import cortar_malha as cm
import os
import numpy as np
import cv2

'''Receber dois lotes
juntar em uma imagem as faces da 
imagem correspondente'''

def join_image(path, name, lote1, lote2):
    try:
        '''cria a pasta
        para o lote especificado'''
        os.mkdir(path + name)

        '''Chama a função cortar_malha'''
        sementes1 = cm.cortar_malha(lote1)
        '''Chama a função cortar_malha'''
        sementes2 = cm.cortar_malha(lote2)

        '''Unir as imagens correspondentes'''
        for i in range(1, 51):
            '''Abrir a pasta'''
            os.chdir(path + name+'/')
            '''Unir as imagens'''
            cv2.imwrite(name + '_semente_' + str(i) + '.jpg', np.hstack(
                [sementes1[i],
                 sementes2[i]]
                    ))
            os.chdir(path)
    except:
        return


