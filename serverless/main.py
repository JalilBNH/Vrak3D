import json
import torch
from detectron2.engine import DefaultPredictor
from detectron2.config import get_cfg
from detectron2 import model_zoo
from detectron2.data import MetadataCatalog
from detectron2.utils.visualizer import Visualizer
import cv2
import numpy as np
from PIL import Image
import io
import base64

# Configure model
cfg = get_cfg()
cfg.merge_from_file(model_zoo.get_config_file("COCO-InstanceSegmentation/mask_rcnn_R_50_FPN_3x.yaml"))
cfg.MODEL.ROI_HEADS.SCORE_THRESH_TEST = 0.5  # set threshold for this model
cfg.MODEL.WEIGHTS = "/opt/nuclio/model_final.pth"  # path to the copied model
predictor = DefaultPredictor(cfg)

def handler(context, event):
    try:
        # Decode image
        img = Image.open(io.BytesIO(event.body))
        img = np.array(img)

        # Make prediction
        outputs = predictor(img)

        # Create masks
        v = Visualizer(img[:, :, ::-1], MetadataCatalog.get(cfg.DATASETS.TRAIN[0]), scale=1.2)
        out = v.draw_instance_predictions(outputs["instances"].to("cpu"))

        # Encode result
        result_img = Image.fromarray(out.get_image()[:, :, ::-1])
        buffered = io.BytesIO()
        result_img.save(buffered, format="JPEG")
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return context.Response(body=json.dumps({"segmentation": img_str}), headers={},
                                content_type='application/json', status_code=200)
    except Exception as e:
        return context.Response(body=json.dumps({"error": str(e)}), headers={},
                                content_type='application/json', status_code=500)
