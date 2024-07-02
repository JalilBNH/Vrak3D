from utils import *
from matplotlib import pyplot as plt 
import numpy as np

def main():
    polygons = [[(0,0), (2,3), (4,0)], [(6,0), (8,3), (10,0)]]

    thresold = 1
    print('==============================')
    
    new_poly = []
    for poly in polygons:
        for i in range(len(poly)):
            #print(f'i : {i}, i + 1 : {(i+1)%len(poly)}')
            dist = euclidDistance(poly[i], poly[(i+1)%len(poly)])
            
            if dist > thresold:
                num_points = int(dist // thresold)
                x_vals = np.linspace(poly[i][0], poly[(i+1)%len(poly)][0], num_points + 2)
                y_vals = np.linspace(poly[i][1], poly[(i+1)%len(poly)][1], num_points + 2)
                #print('c laaaa ', list(zip(x_vals, y_vals)))
                new_poly.append(list(zip(x_vals, y_vals))) 
        break
    #visualizePoints(polygons)
    print(polygons)
    print(new_poly) # Because in this case, i consider 1 polygon as 3
        
if __name__ == '__main__':
    main()
    