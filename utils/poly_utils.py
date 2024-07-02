
from math import sqrt, atan, cos, sin
import numpy as np

from matplotlib import pyplot as plt
from matplotlib.patches import Polygon

# Every polygon must have the same size 

def visualizePolygons(polygons):
    """Given a list of polygons, plot all of them.

    Args:
        polygons (list): list of polygons
    """
    
    fig, ax = plt.subplots()
    
    n = len(polygons)
    color = plt.cm.rainbow(np.linspace(0, 1, n))
    
    for i, poly in enumerate(polygons):
        p = Polygon(poly, closed=True, fill=False, edgecolor=color[i])
        ax.add_patch(p)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    plt.show()


def visualizePoints(polygons):
    """Given a list of polygons, plot the points

    Args:
        polygons (list): list of polygons 
    """
    colors = plt.cm.rainbow(np.linspace(0, 1, len(polygons)))
    
    for poly, color in zip(polygons, colors):
        for coords in poly:
            plt.scatter(coords[0], coords[1], color=color)   
            
    plt.show() 


def computeSlope(v1, v2):
    """Given two points, return the slope. 

    Args:
        v1 (int): coordinates of the first point
        v2 (int): coordinates of the second point

    Returns:
        float: slope between the two points
    """
    
    x1, y1 = v1
    x2, y2 = v2
    
    return (y2 - y1)/(x2 - x1)

def computeMeanSlope(polygons):
    """Given a list of polygons of the same size, return the mean slope for each segment.

    Args:
        polygons (list): list of polygons

    Returns:
        np.array: array of means slope
    """
    
    num_polygons = len(polygons)
    num_verticies = len(polygons[0])
    
    slopes = np.zeros(num_verticies - 1)
    
    for i in range(num_polygons):
        for j in range(num_verticies - 1):
            slopes[j] += computeSlope(polygons[i][j], polygons[i][j+1])
    
    return slopes/num_polygons


def euclidDistance(v1, v2):
    """Given two points, return the euclidean distance between them.

    Args:
        v1 (_type_): _description_
        v2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    x1, y1 = v1
    x2, y2 = v2
    
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)


def computeMeanDistance(polygons):
    """Given a list of polygons of the same size, return the mean euclidean distance for each segment.

    Args:
        polygons (list): list of polygons

    Returns:
        np.array: array of means slope
    """
    num_polygons = len(polygons)
    num_verticies = len(polygons[0])
    
    means = np.zeros(num_verticies - 1)
    
    for i in range(num_polygons):
        for j in range(num_verticies - 1):
            means[j] += euclidDistance(polygons[i][j], polygons[i][j+1])
            
    return means/num_polygons 


def newPointPosition(start_point, slope, dist):
    x1, y1 = start_point
    theta = atan(slope)
    
    d_x = dist * cos(theta)
    d_y = dist * sin(theta)
    
    x2 = x1 + d_x
    y2 = y1 + d_y
    
    return (x2, y2)


def startPointPosition(polygons):
    """Given a list of polygons return the mean position of the starting point

    Args:
        polygons (list): list of polygons 
    """
    num_polygons = len(polygons)
    mean_x = 0
    mean_y = 0 
    
    for poly in polygons:
        mean_x += poly[0][0]
        mean_y += poly[0][1]
    
    return (mean_x/num_polygons, mean_y/num_polygons)

def meanPolygon(polygons):
    """Given a list of polygons return a new polygon that is the mean of all the polygons given.

    Args:
        polygons (list): list of polygons

    Returns:
        list: coordinates of the new polygon 
    """
    new_polygon = [startPointPosition(polygons)]
    means_slope = computeMeanSlope(polygons)
    means_distances = computeMeanDistance(polygons)
    
    num_segments = len(means_distances)
    
    for i in range(num_segments):
        new_polygon.append(newPointPosition(new_polygon[i], means_slope[i], means_distances[i]))
    
    return [new_polygon]