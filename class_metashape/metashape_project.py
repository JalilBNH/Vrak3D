import Metashape
import math
from matplotlib import pyplot as plt
import numpy as np

class Project:
    def __init__(self, project_path) -> None:
        self.doc = Metashape.Document()
        self.doc.open(project_path)
        self.chunk = self.doc.chunk
        self.cameras_labels = []
        self.positions = []
        self.rotations = []
        for i, camera in enumerate(self.chunk.cameras):
            self.cameras_labels.append(camera.label)
            self.positions.append((int(camera.center[0]*100), int(camera.center[1]*100), int(camera.center[2]*100)))
            if camera.transform:
                self.rotations.append(camera.transform.rotation())
        self.rotations = np.array(self.rotations) 
        
    def print_camera_labels(self):
        for i, camera in enumerate(self.chunk.cameras):
            print(f"Camera {i}: {camera.label}")
            
    def get_xyz_distance_cameras_ind(self, ind1, ind2):
        camera1 = self.chunk.cameras[ind1]
        camera2 = self.chunk.cameras[ind2]
        
        pos1 = camera1.center
        pos2 = camera2.center
        
        delta_x = pos2.x - pos1.x
        delta_y = pos2.y - pos1.y
        delta_z = pos2.z - pos1.z 
        
        print(f"Le décalage en x entre la caméra {ind1} et la caméra {ind2} est de {delta_x}")
        print(f"Le décalage en y entre la caméra {ind1} et la caméra {ind2} est de {delta_y}")
        print(f"Le décalage en z entre la caméra {ind1} et la caméra {ind2} est de {delta_z}")
        return (delta_x, delta_y, delta_z)
        

    def get_distance_cameras(self, ind1, ind2):
        camera1 = self.chunk.cameras[ind1]
        camera2 = self.chunk.cameras[ind2]
        
        pos1 = camera1.center
        pos2 = camera2.center
        
        distance = (pos1 - pos2).norm()
        print(f"La distance entre la caméra {ind1} et la caméra {ind2} est de {distance}")
        return distance

    def get_angle_cameras(self, ind1, ind2):
        camera1 = self.chunk.cameras[ind1]
        camera2 = self.chunk.cameras[ind2]
        
        direction1 = camera1.transform.mulv(Metashape.Vector([0, 0, -1]))
        direction2 = camera2.transform.mulv(Metashape.Vector([0, 0, -1]))

        cos_angle = direction1 * direction2 / (direction1.norm() * direction2.norm())
        
        angle_rad = math.acos(cos_angle)
        
        angle_deg = math.degrees(angle_rad)
        
        print(f"L'angle entre la caméra {ind1} et la caméra {ind2} est de {angle_deg} degrés.")

    def visualize_cameras_3D(self):
        """Given a list of polygons, plot all the points

        Args:
            polygons (list[list]): list of list of tuple size 3
        """
        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')
        
        x_coords = [] 
        y_coords = [] 
        z_coords = []
        for cord in self.positions:
            x_coords.append(cord[0]) 
            y_coords.append(cord[1])
            z_coords.append(cord[2])
        
        ax.scatter(x_coords, y_coords, z_coords)
        
    

        
# Ajuster l'échelle et les labels
        
        plt.show()