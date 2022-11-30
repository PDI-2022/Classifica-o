import cv2
from modelo import *
import os, glob

embriao_classes = []
path1 ='LOTE_1_R1'
i = 0

with open("embriao.names", "r") as f:
	embriao_classes = [cname.strip() for cname in f.readlines()]


def deteccao(img,index):      
    
    embriao_res = embriao_detect(img)

    for ret, _, _ in embriao_res:
    
        embriao_cortado = img[ret[1]:ret[3], ret[0]:ret[2]]
        if len(embriao_cortado) > 0:
            cv2.imwrite(f'./embrioes/semente-'+ str(index+1) + '.jpg',embriao_cortado)
        return embriao_cortado


for dic in glob.glob(f"{path1}*"):
    for img_path in glob.glob(os.path.join(dic, "*.jpg")):
        label = img_path.split("_")
        img = cv2.imread(img_path)
        img = deteccao(img,i)
        i+=1
