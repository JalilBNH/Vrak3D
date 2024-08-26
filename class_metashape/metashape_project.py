import Metashape
import math
from matplotlib import pyplot as plt
import numpy as np

class Project:
    def __init__(self, project_path) -> None:
        """Load the metashape project.

        Args:
            project_path (string): Path/to/project.psx 
        """
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
        """Print all the cameras labels of the project.
        """
        for i, camera in enumerate(self.chunk.cameras):
            print(f"Camera {i}: {camera.label}")
            
    def get_xyz_distance_cameras_ind(self, ind1, ind2):
        """Given 2 indices of cameras, return the relative on the axis (x, y, z) between them.

        Args:
            ind1 (int): Camera indice 1
            ind2 (int): Camera indice 2

        Returns:
            tuple: (delta_x, delta_y, delta_z)
        """
        camera1 = self.chunk.cameras[ind1]
        camera2 = self.chunk.cameras[ind2]
        
        pos1 = camera1.center
        pos2 = camera2.center
        
        delta_x = pos2.x - pos1.x
        delta_y = pos2.y - pos1.y
        delta_z = pos2.z - pos1.z 
        
        print(f"The x-offset between {ind1} camera and {ind2} camera is {delta_x}")
        print(f"The y-offset between {ind1} camera and {ind2} camera is {delta_y}")
        print(f"The z-offset between {ind1} camera and {ind2} camera is {delta_z}")
        return (delta_x, delta_y, delta_z)
        

    def get_distance_cameras(self, ind1, ind2):
        """Given 2 indices of cameras, return the distance between them.

        Args:
            ind1 (int): Camera indice 1
            ind2 (int): Camera indice 2

        Returns:
            float: Distance between the 2 cameras
        """
        camera1 = self.chunk.cameras[ind1]
        camera2 = self.chunk.cameras[ind2]
        
        pos1 = camera1.center
        pos2 = camera2.center
        
        distance = (pos1 - pos2).norm()
        print(f"The distance between the camera {ind1} and the camera {ind2} is {distance}")
        return distance

    def get_angle_cameras(self, ind1, ind2):
        """Given 2 cameras indices, return the angle between them.

        Args:
            ind1 (int): Camera indice 1
            ind2 (int): Camera indice 2
        """
        camera1 = self.chunk.cameras[ind1]
        camera2 = self.chunk.cameras[ind2]
        
        direction1 = camera1.transform.mulv(Metashape.Vector([0, 0, -1]))
        direction2 = camera2.transform.mulv(Metashape.Vector([0, 0, -1]))

        cos_angle = direction1 * direction2 / (direction1.norm() * direction2.norm())
        
        angle_rad = math.acos(cos_angle)
        
        angle_deg = math.degrees(angle_rad)
        
        print(f"The angle between {ind1} camera and {ind2} camera is {angle_deg} degrees.")

    def visualize_cameras_3D(self):
        """Plot all the cameras of the project in 3d.
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
        
        plt.show()