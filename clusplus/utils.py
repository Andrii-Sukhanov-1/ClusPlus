'''
Helper functions that operate on datasets, 
most importantly for plotting
'''
import matplotlib.pyplot as plt
from typing import Tuple, List, Dict, Any
from matplotlib.axes import Axes

Point = Tuple[int | float, int | float]

def get_x_y(points : List[Point]) -> Tuple[List[int | float]]:
    '''Unziping list of points into lists for x and y coordinates'''
    #Preparing coordinates for a plot 
    x, y = [], []
    for point in points:
        x.append(point[0])
        y.append(point[1])
    return x, y



def int_label_to_color(label: int) -> str:
    '''
    Module specific colors for clusters.
    Main feature - outliers are RED.
    Supports labels from -1 to 5
    '''

    colors = {-1 : 'r',
               0 : 'b',
               1 : 'g', 
               2 : 'c',
               3 : 'y',
               4 : 'k',
               5 : 'm' }
    try:
        return colors[label]
    except (KeyError):
        raise KeyError(f'For plotting using this package all labels should be in range {colors.keys()}')


def plot_real_clusters(points : List[Point], labels : List[int], ax : Axes) -> None:
    '''
    Module specific colors for clusters,
    RED points are considered as outliers
    '''
    my_labels = list(map(int_label_to_color, labels)) #myclusters specific colors for clusters
    x, y = get_x_y(points)
    ax.scatter(x, y, c=my_labels)
         