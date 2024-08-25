import cv2
from matplotlib import pyplot as plt
from detectron2.utils.visualizer import Visualizer
import random

def visualizeMask(dataset, metadata, ind=0, rand=False):
    """Visualize segmentations mask with detectron2

    Args:
        dataset 
        metadata : Optionnal
        ind (int, optional): Image indice. Defaults to 0.
        rand (bool, optional): Random image from the dataset. Defaults to True.
    """
    if rand==True:
        ind = random.randint(0,len(dataset)-1)
    
    dataset_in = dataset[ind]
    img = cv2.imread(dataset_in['file_name'])
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    v = Visualizer(
        img,
        metadata=metadata,
        scale=0.8
    )
    
    out = v.draw_dataset_dict(dataset_in)
    plt.imshow(out.get_image()), plt.axis('off'), plt.title(f"Image : {ind}")