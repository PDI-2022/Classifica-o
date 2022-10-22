import cortar_malha as cm
import os
import numpy as np
import cv2

'''Receber dois lotes
juntar em uma imagem as faces da 
imagem correspondente'''

def join_image(path, name, lote1):
    try:
        '''cria a pasta
        para o lote especificado'''
        os.mkdir(path + name)

        '''Chama a função cortar_malha'''
        sementes1 = cm.cortar_malha(lote1)
        '''Unir as imagens correspondentes'''
        aux = 0
        aux_2 = 0
        for i in range(50):
            '''Abrir a pasta'''
            os.chdir(path + name+'/')
            '''Unir as imagens'''
            if(i%5 == 0):
                if i > 0:
                    aux += 4    
                
                cv2.imwrite(name + '_semente_' + str(i - aux+1) + '.jpg', np.hstack(
                    [sementes1[i]]
                        ))
                aux2 = 0

            if(i%5 != 0):
                aux2 += 9
                cv2.imwrite(name + '_semente_' + str(i - aux + aux2+1) + '.jpg', np.hstack(
                    [sementes1[i]]
                        ))

            os.chdir(path)
    except:
        return


