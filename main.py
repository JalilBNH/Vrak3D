from utils import *

def main():
    polygons = [[(0,0), (2,3), (4,0)], [(6,0), (8,3), (10,0)]]

    visualizePolygons(polygons)
    new_poly = meanPolygon(polygons)   
    print(new_poly)
   
    polygons.append(new_poly[0])
    visualizePolygons(polygons)
    
if __name__ == '__main__':
    main()
    