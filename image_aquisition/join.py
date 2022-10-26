import cortar_malha as cm
import os
import numpy as np
import cv2

'''Receber dois lotes
juntar em uma imagem as faces da 
imagem correspondente'''

def crop_function(image):
        lower = np.array([94, 20, 2])
        upper = np.array([145, 255, 255])

        img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, lower, upper)

        img = cv2.bitwise_and(img ,img, mask = mask)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.GaussianBlur(img, (3, 3), 0)
        return img
        
    
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
            sementes1[i] = crop_function(sementes1[i])
            if(i%5 == 0):
                if i > 0:
                    aux += 4
                aux2 = 0    
                
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


