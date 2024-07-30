from matplotlib import pyplot as plt
from detectron2.config import get_cfg
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.utils.visualizer import Visualizer
from detectron2.utils.visualizer import ColorMode



def visualize_predictions(image_path, model_weights, threshold=None):
    """Given a path to an image, a path to model weights plot the segmentation prediction on the image.

    Args:
        image_path (str): PATH/TO/IMAGE
        model_weights (str): PATH/TO/WEIGHTS
        threshold (float, optional): Value of thresold between 0 and 1. Defaults to None.
    """
    DATA_SET_NAME = "bloc_segmentation"
    ARCHITECTURE = "mask_rcnn_R_101_FPN_3x"
    CONFIG_FILE_PATH = f"COCO-InstanceSegmentation/{ARCHITECTURE}.yaml"
    
    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file(CONFIG_FILE_PATH))
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1
    cfg.MODEL.WEIGHTS = model_weights
    if threshold:
        cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = threshold
    predictor = DefaultPredictor(cfg)
    
    image = plt.imread(image_path)
    
    outputs = predictor(image)
    
    v = Visualizer(
        image,
        metadata={},
        scale=0.8,
        instance_mode=ColorMode.IMAGE_BW
    )
    
    out = v.draw_instance_predictions(outputs['instances'].to('cpu'))
    return out.get_image()
