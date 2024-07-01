from utils import computeMeanSlope, computeMeanDistance, visualizePolygons, meanPolygon

def main():
    polygons = [[(1,1), (2,3), (3,1)], [(1,1), (2,10), (3,1)], [(1,1), (2,2), (3,-1)]]
    
    print(meanPolygon(polygons))

if __name__ == '__main__':
    main()
    