from utils import computeMeanSlope, computeMeanDistance, visualizePolygons

def main():
    polygons = [[(1,1), (2,3), (3,1)], [(1,1), (2,10), (3,1)], [(1,1), (2,2), (3,-1)]]
    
    visualizePolygons(polygons)
    
    print(computeMeanSlope(polygons))
    print(computeMeanDistance(polygons))

if __name__ == '__main__':
    main()
    