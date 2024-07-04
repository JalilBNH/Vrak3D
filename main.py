from utils import *
from matplotlib import pyplot as plt 
import numpy as np

def main():
    polygons = [[(0,0), (2,3), (4,0)], [(6,0), (8,3), (10,0)], [(0,10), (52,4), (19,0), (4, 4)]]    
    
    polygons_filled = fill_polygons(polygons)
    
    visualize_points(polygons)
    visualize_polygons(polygons_filled)    
    
    
        
if __name__ == '__main__':
    main()
    