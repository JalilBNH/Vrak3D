# Project Vrak3D

The goal of the project was to segment stone block on 3D model of archeological site. I split this project, the first was the training of the segmentation model and the second was the construction of the model with photogrammetry technics.

## Training of the model

During this project, I've trained mask r-cnn with detectron2 with a small amount of data. You can use the models that I have trained, or you can train your own with the jupyter notebook in the training folder.

After the model training, I had to deploy it on CVAT to annotate easy unlabelled images. You can check in the serverless folder all you need to deploy the functions I made.

## Photogrammetry

Photogrammetry uses photos to build 3d models. To segment bloc on the 3d models, we decided to pass through the 2d photos by segmenting them and then construct the segmentation mask in 3d. During this process, we had a problem, from a photo to another, the segmentation mask wasn't made perfectly so I had to find a way to mean all our segmentation mask. I thought about 2 methods. 

### Using the IOU
The first method was to use the IOU area. I wanted to get the 2d positions of all the mask, take the central one as reference and compute the mean of all of them by weighting them with the IOU relative to the central one.

### Using the dot product
Each camera is associated with a position in the 3d space, an image and an orientation. If we have the camera vector, we can take one as a reference and compute the dot product with each other. Once we have each dot product value, we can compute the mean and weighting each camera with the dot product value.

- If the dot product is close to 1 so the cameras have approximately the same orientation.
- If the dot product is close to 0 the cameras have a perpendicular point of view. The second camera should not influence the first one.
- If the dot product is negative so the cameras don't follow the same directions, so they don't point as the same object.