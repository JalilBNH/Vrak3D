from detectron2.config import get_cfg
from detectron2.data.detection_utils import read_image
from detectron2.engine.defaults import DefaultPredictor
from detectron2.data.datasets.builtin_meta import COCO_CATEGORIES
from detectron2 import model_zoo

ARCHITECTURE = "mask_rcnn_R_101_FPN_3x"
CONFIG_FILE_PATH = f"COCO-InstanceSegmentation/{ARCHITECTURE}.yaml"
WEIGHTS = r'C:\Users\Jalil\Desktop\PROJECTS\Vrak3D\training\bloc_segmentation\mask_rcnn_R_101_FPN_3x\2024-07-19-13-02-30\model_final.pth'
THRESOLD = 0.5


def setup_cfg():
    cfg = get_cfg()
    cfg.merge_from_file(model_zoo.get_config_file(CONFIG_FILE_PATH))
    cfg.MODEL.ROI_HEADS.NUM_CLASSES = 1
    cfg.MODEL.WEIGHTS = WEIGHTS
    cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = THRESOLD
    cfg.freeze()
    return cfg

def main():
    cfg = setup_cfg()
    input = r'C:\Users\Jalil\Desktop\PROJECTS\Vrak3D\training\datasets\0COMPLET\complet\images\20220210_glanum_a_000108.JPG'
    img = read_image(input)
    predictor = DefaultPredictor(cfg)
    predictions = predictor(img)
    instances = predictions['instances']
    pred_boxes = instances.pred_boxes
    scores = instances.scores
    pred_classes = instances.pred_classes
    pred_masks = instances.pred_masks
    for box, score, label in zip(pred_boxes, scores, pred_classes):
        #print(box.tolist(), float(score), int(label))
        pass


if __name__ == "__main__":
    main()



def handler(context, event):
    print('hello world les brozer')