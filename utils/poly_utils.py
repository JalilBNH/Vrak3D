
from math import sqrt, atan, cos, sin
import numpy as np
from copy import deepcopy
from matplotlib import pyplot as plt
from matplotlib.patches import Polygon
import shapely
# Every polygon must have the same size 

def visualize_polygons(polygons):
    """Given a list of polygons, plot all of them.

    Args:
        polygons (list[list]): list of polygons
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

    

def visualize_points(polygons):
    """Given a list of polygons, plot the points

    Args:
        polygons (list[list]): list of list of tuple size 2
    """
    colors = plt.cm.rainbow(np.linspace(0, 1, len(polygons)))
    
    for poly, color in zip(polygons, colors):
        for coords in poly:
            plt.scatter(coords[0], coords[1], color=color, s=2)   
            
    plt.show() 


def compute_slope(v1, v2):
    """Given two points, return the slope. 

    Args:
        v1 (tuple): coordinates of the first point
        v2 (tuple): coordinates of the second point

    Returns:
        float: slope between the two points
    """
    
    x1, y1 = v1
    x2, y2 = v2
    
    return (y2 - y1)/(x2 - x1)

def compute_mean_slope(polygons):
    """Given a list of polygons of the same size, return the mean slope for each segment.

    Args:
        polygons (list[tuple]): list of polygons

    Returns:
        np.array: array of means slope
    """
    
    num_polygons = len(polygons)
    num_verticies = len(polygons[0])
    
    slopes = np.zeros(num_verticies - 1)
    
    for i in range(num_polygons):
        for j in range(num_verticies - 1):
            slopes[j] += compute_slope(polygons[i][j], polygons[i][j+1])
    
    return slopes/num_polygons


def euclidean_distance(v1, v2):
    """Given two points, return the euclidean distance between them.

    Args:
        v1 (tuple): coordinates of the first point
        v2 (tuple): coordinates of the second point

    Returns:
        float: euclidean distance between the two points.
    """
    x1, y1 = v1
    x2, y2 = v2
    
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)


def compute_mean_distance(polygons):
    """Given a list of polygons of the same size, return the mean euclidean distance for each segment.

    Args:
        polygons (list[list]): list of polygons

    Returns:
        np.array: array of means slope
    """
    num_polygons = len(polygons)
    num_verticies = len(polygons[0])
    
    means = np.zeros(num_verticies - 1)
    
    for i in range(num_polygons):
        for j in range(num_verticies - 1):
            means[j] += euclidean_distance(polygons[i][j], polygons[i][j+1])
            
    return means/num_polygons 


def new_point_position(start_point, slope, dist):
    x1, y1 = start_point
    theta = atan(slope)
    
    d_x = dist * cos(theta)
    d_y = dist * sin(theta)
    
    x2 = x1 + d_x
    y2 = y1 + d_y
    
    return (x2, y2)


def find_start_point_pos(polygons):
    """Given a list of polygons return the mean position of the starting point

    Args:
        polygons (list[list]): list of polygons 
    """
    num_polygons = len(polygons)
    mean_x = 0
    mean_y = 0 
    
    for poly in polygons:
        mean_x += poly[0][0]
        mean_y += poly[0][1]
    
    return (mean_x/num_polygons, mean_y/num_polygons)

def mean_polygons(polygons):
    """Given a list of polygons return a new polygon that is the mean of all the polygons given.

    Args:
        polygons (list[list]): list of polygons

    Returns:
        list: coordinates of the new polygon 
    """
    new_polygon = [find_start_point_pos(polygons)]
    means_slope = compute_mean_slope(polygons)
    means_distances = compute_mean_distance(polygons)
    
    num_segments = len(means_distances)
    
    for i in range(num_segments):
        new_polygon.append(new_point_position(new_polygon[i], means_slope[i], means_distances[i]))
    
    return [new_polygon]

def fill_polygons(polygons, thresold=1):
    """Given a list of polygons and a thresold, return the polygons filled with points on the outline

    Args:
        polygons (list[list]): list of polygons
        thresold (int, optional): thresold for the minimal distance between 2 points. Defaults to 1.

    Returns:
        : polygons filled with points
    """
    new_polys = []
    for poly in polygons:
        new_poly = []
        for i in range(len(poly)):
            #print(f'i : {i}, i + 1 : {(i+1)%len(poly)}')
            dist = euclidean_distance(poly[i], poly[(i+1)%len(poly)])
            
            if dist > thresold:
                num_points = int(dist // thresold)
                x_vals = np.linspace(poly[i][0], poly[(i+1)%len(poly)][0], num_points + 2)
                y_vals = np.linspace(poly[i][1], poly[(i+1)%len(poly)][1], num_points + 2)
                #print('c laaaa ', list(zip(x_vals, y_vals)))
                for j in range(len(x_vals)):
                    new_poly.append((x_vals[j], y_vals[j]))
                #new_poly.append(zip(x_vals, y_vals)) 
        new_polys.append(new_poly)
        
    return new_polys


def find_corner(polygons):
    """Given a list of polygons, return the for points that frames the polygon

    Args:
        polygons (list[list]): list of polygons

    Returns:
        list: list of the coordinates that frames the polygons
    """
    
    corners = deepcopy(polygons)
    for poly in polygons:
        #print(f"poly : {poly}")
        x_array = np.zeros(len(poly), dtype='float')
        y_array = np.zeros(len(poly))
        for i, coord in enumerate(poly):
            x_array[i] = coord[0]
            y_array[i] = coord[1]
        x_max = np.max(x_array)
        x_min = np.min(x_array)
        y_max = np.max(y_array)
        y_min = np.min(y_array)
        corners.append([(x_max, y_max), (x_max, y_min), (x_min, y_max), (x_min, y_min)]) 
    
    return corners


def compute_iou(polygon1, polygon2):
    """Given two polygons, return the intersection over union area.

    Args:
        polygon1 (list[tuples]): list of polygon coordinates
        polygon2 (list[tuples]): list of polygon coordinates

    Returns:
        float: intersection over union area
    """
    poly1 = shapely.geometry.Polygon(polygon1)
    poly2 = shapely.geometry.Polygon(polygon2)
    
    intersection = poly1.intersection(poly2).area
    union = poly1.union(poly2).area
    
    return intersection / union