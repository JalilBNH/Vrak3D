from pycocotools.coco import COCO

def load_coco_dataset(annotation_path):
    
    coco = COCO(annotation_path)
    return coco.imgs
    
def load_anns(images):
    pass