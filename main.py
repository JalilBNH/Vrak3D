from utils import visualize_points, fill_polygons, find_corner, compute_iou
import os
from PIL import Image
from pycocotools.coco import COCO
import numpy as np
from matplotlib import pyplot as plt

def main():

    """ annotation_path = 'training/datasets/0COMPLET/complet/annotations/instances_default.json'
    images_path = 'training/datasets/0COMPLET/complet/images'
    
    coco = COCO(annotation_path)
    images = coco.imgs
    
    ind = 6
    
    image_info = images[ind]
    
    
    anns_ids = coco.getAnnIds(imgIds=ind)
    anns = coco.loadAnns(anns_ids)
    
    keypoints = []
    for ann in anns:
        mask = []
        for seg in ann['segmentation']:
            for i in range(0, len(seg)-1, 2):
                mask.append((seg[i], seg[i+1]))
        keypoints.append(mask)
     """
    #keypoints = [[(5702.49, 740.5), (5774.35, 678.23), (5811.3, 646.74), (5847.57, 628.27), (5903.01, 641.95), (5974.18, 647.43), (5982.39, 680.96), (5996.76, 696.02), (6013.19, 769.93), (5963.23, 813.05), (5822.94, 819.2), (5743.55, 886.96), (5699.75, 878.06), (5685.38, 856.84), (5689.48, 777.46)], [(6735.02, 2369.85), (6897.57, 2371.06), (6918.19, 2389.26), (6920.62, 2417.16), (6971.56, 2503.28), (6964.28, 2517.84), (6795.67, 2528.75), (6725.32, 2508.13), (6703.49, 2402.6)]]
    
    """keypoints_with_corners = find_corner(keypoints)
    print(keypoints_with_corners)
    
    visualize_points(keypoints_with_corners) """
    
    """ visualize_points(polygon)
    filled_keypoints = fill_polygons(keypoints, thresold=30)
    visualize_points(filled_keypoints) """
    
    
    """ plt.imshow(plt.imread(os.path.join(images_path, image['file_name']))), plt.axis('off'), plt.title(f'ind : {ind}')
    plt.show() """
    
    json_path = 'training/datasets/0COMPLET/complet/annotations/instances_default.json'
    imgs_path = 'training/datasets/0COMPLET/complet/images'
    coco = COCO(json_path)
    print(coco)
    
        
if __name__ == '__main__':
    main()
    






    #polygons = [[(0,0), (2,3), (4,0)], [(6,0), (8,3), (10,0)], [(0,10), (52,4), (19,0), (4, 4)]]    
    #polygons_filled = fill_polygons(polygons) 