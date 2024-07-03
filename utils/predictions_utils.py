from matplotlib import pyplot as plt
from detectron2.config import get_cfg
from detectron2 import model_zoo
from detectron2.engine import DefaultPredictor
from detectron2.utils.visualizer import Visualizer
from detectron2.utils.visualizer import ColorMode



def visualize_predictions(image_path):
    DATA_SET_NAME = "bloc_segmentation"
    ARCHITECTURE = "mask_rcnn_R_101_FPN_3x"
    CONFIG_FILE_PATH = f"COCO-InstanceSegmentation/{ARCHITECTURE}.yaml"
    
    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file(CONFIG_FILE_PATH))
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1
    cfg.MODEL.WEIGHTS = "training/bloc_segmentation/mask_rcnn_R_101_FPN_3x/2024-07-03-11-36-15/model_0005999.pth"
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.3
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
    plt.imshow(out.get_image()), plt.axis('off'), plt.title(f'{image_path}')
    plt.show()
