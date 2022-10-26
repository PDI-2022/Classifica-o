import cv2
import numpy as np
import base64
import csv
import cortar_malha as cut
from skimage import measure
from shapely.geometry import Polygon

def count_holes(image) -> int:
    contours = measure.find_contours(image, 200)

    holes = [Polygon(contour) for contour in contours if len(contour) > 3]
    
    seed_polygons = []
    
    #ordenando pela maior área (as duas maiores áreas são os próprio feijão)
    holes.sort(reverse=True, key=lambda element: element.area)

    within = [] 
    up = 0
    down = 0    
    

    # checando se tem buracos
    if len(holes) > 2:
        for i in range(2):
            seed_polygons.append(holes[i])
            down += holes[i].area
            

        holes.pop(0)
        holes.pop(0)

        for hole in holes:
            for seed_polygon in seed_polygons:
                if hole.within(seed_polygon):
                    within.append(hole)
                    up += hole.area

        return (len(within), (up/down))

    return (0, 0) 

def remove_background_and_get_mask(input_image):
    used_threshold, thresholded_bgr_image = cv2.threshold(input_image, 110, 255, cv2.THRESH_BINARY)
    thresholded_blue_component, thresholded_green_component, thresholded_red_component = cv2.split(thresholded_bgr_image)

    mask_filtered = cv2.medianBlur(thresholded_red_component, 5)

    return mask_filtered

def extract_white_percentage(input_image, id=0):
    hsv = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)

    lower = np.array([0,0,168])
    upper = np.array([172,111,255])   
    mask = cv2.inRange(hsv, lower, upper)

    white_extracted_image = cv2.bitwise_and(input_image, input_image, mask = mask)

    pixels_number_seed = np.count_nonzero(input_image)
    pixels_extracted_white = np.count_nonzero(white_extracted_image)


    return pixels_extracted_white/pixels_number_seed


def remove_background(input_image, id=0):
    used_threshold, thresholded_bgr_image = cv2.threshold(input_image, 110, 255, cv2.THRESH_BINARY)
    thresholded_blue_component, thresholded_green_component, thresholded_red_component = cv2.split(thresholded_bgr_image)

    mask_filtered = cv2.medianBlur(thresholded_red_component, 5)

    result_image = cv2.bitwise_and(input_image, input_image, mask = mask_filtered)

    return result_image


def extract_dark_red_percentage(input_image, id=0):
    hsv = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)

    first_lower = np.array([161, 168, 80])
    first_upper = np.array([180 , 255, 240])   
    first_mask = cv2.inRange(hsv, first_lower, first_upper)

    second_lower = np.array([0, 168, 80])
    second_upper = np.array([60 , 255, 240])   
    second_mask = cv2.inRange(hsv, second_lower, second_upper)

    mask = cv2.bitwise_or(first_mask, second_mask)

    dark_red_extracted_image = cv2.bitwise_and(input_image, input_image, mask = mask)

    pixels_number_seed = np.count_nonzero(input_image)
    pixels_extracted_white = np.count_nonzero(dark_red_extracted_image)


    return pixels_extracted_white/pixels_number_seed


def extract_light_red_percentage(input_image, id=0):
    hsv = cv2.cvtColor(input_image, cv2.COLOR_BGR2HSV)

    first_lower = np.array([161, 90, 80])
    first_upper = np.array([180 , 190, 240])   
    first_mask = cv2.inRange(hsv, first_lower, first_upper)

    second_lower = np.array([0, 90, 80])
    second_upper = np.array([60 , 190, 240])   
    second_mask = cv2.inRange(hsv, second_lower, second_upper)

    mask = cv2.bitwise_or(first_mask, second_mask)

    light_red_extracted_image = cv2.bitwise_and(input_image, input_image, mask = mask)

    pixels_number_seed = np.count_nonzero(input_image)
    pixels_extracted_white = np.count_nonzero(light_red_extracted_image)


    return pixels_extracted_white/pixels_number_seed


def process_data(semente, label):
    input_image = semente


    header = ['SEMENTE', 'REPETICAO', 'Porcentagem de Branco', 'Porcentagem de Vermelho Carmim Claro', 'Porcentagem de Vermelho Carmim Escuro', 'Quantidade de Buracos', 'Área Buraco/Área Semente']
    rows = []
    removed_background = remove_background(input_image, label[-1])
    white_percentage = extract_white_percentage(removed_background, label[-1])
    light_red_percentage = extract_light_red_percentage(removed_background, label[-1])
    dark_red_percentage = extract_dark_red_percentage(removed_background, label[-1])
            
    thresholded_red_component = remove_background_and_get_mask(removed_background)
    aux_img = cv2.erode(thresholded_red_component, (3,3), iterations=120)
    aux_img = cv2.dilate(aux_img, (3,3), iterations=120)
    (holes, holes_percentage) = count_holes(aux_img)
    if(label[5] == "EXTERNO"):
        rows.append(
            [
            label[6],
            label[-1], 
            1, 
            white_percentage, 
            light_red_percentage,
            dark_red_percentage,
            holes,
            holes_percentage
            ]
            )
    else:
        rows.append(
            [
            label[6],
            label[-1], 
            2, 
            white_percentage, 
            light_red_percentage,
            dark_red_percentage,
            holes,
            holes_percentage
            ]
            )

    #with open('relatorio.csv', 'w', encoding='UTF8') as f:
     #   writer = csv.writer(f)
      #  writer.writerow(header)
       # for row in rows:
        #    writer.writerow(row)
        
    return rows

def is_empty(block):
    #removed_background = remove_background(block)
    #percentage = np.count_nonzero(removed_background) / (block.shape[0]*block.shape[1])

    #return True if percentage < 0.05 else False
    return False