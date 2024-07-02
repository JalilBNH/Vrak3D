from utils import *
from matplotlib import pyplot as plt 
import numpy as np

def main():
    polygons = [[(0,0), (2,3), (4,0)], [(6,0), (8,3), (10,0)]]

    print(polygons)
    thresold = 1
    
    
    for poly in polygons:
        for i in range(len(poly)):
            #print(f'i : {i}, i + 1 : {(i+1)%len(poly)}')
            dist = euclidDistance(poly[i], poly[(i+1)%len(poly)])
            if dist > thresold:
                num_points = int(dist // thresold)
                x_vals = np.linspace(poly[i][0], poly[(i+1)%len(poly)][0], num_points + 2)
                y_vals = np.linspace(poly[i][1], poly[(i+1)%len(poly)][1], num_points + 2)
                for j, coord in enumerate(zip(x_vals, y_vals)):
                    poly.insert((i+1)%len(poly) + j, coord)
    
    print('===================================')
    print(polygons)
    visualizePoints(polygons)
                    

        
if __name__ == '__main__':
    main()
    