'''
Stores built-in datasets of 2D points
and functions related to their choice and loading
'''
import random
from typing import Tuple, Literal, Dict, List, Any, Optional

Point = Tuple[int | float, int | float]
Labels = List[int]
#Creating a database of possible point sets for kmeans
database = {}

overlapping_clusters = [

    # --- Cluster 1: dense compact cloud ---
    (120,130),(122,132),(124,128),(126,131),(128,129),
    (130,133),(132,130),(134,134),(136,132),(138,131),

    # --- Cluster 2: medium-density circular-ish cluster ---
    (170,160),(180,170),(190,165),(200,155),(210,160),
    (195,180),(175,175),(185,190),(215,170),(200,180),
    (190,150),(170,155),(205,190),(220,160),

    # --- Cluster 3: sparse, wide convex cluster ---
    (230,140),(245,155),(260,135),(275,150),(290,140),
    (305,165),(295,180),(270,170),(255,185),(235,170),
    (220,160),(250,120),(285,120),(315,150),

    # --- Cluster 4: diagonal, medium density ---
    (260,220),(275,235),(290,250),(305,265),
    (320,280),(335,295),(350,310),
    (280,210),(300,225),(320,245),
    (340,265),(360,285)

]
overlapping_clusters_labels = [0] * 10 + [1] * 14 + [2] * 14 + [3] * 12
database['overlapping clusters'] = overlapping_clusters, overlapping_clusters_labels

noisy_points = [
    # Cluster 1
    (200,210),(205,215),(210,205),(215,210),(220,200),(210,220),
    (225,215),(215,225),(205,200),(200,205),

    # Cluster 2
    (600,610),(605,615),(610,605),(615,610),(620,600),(610,620),
    (625,615),(615,625),(605,600),(600,605),

    # Cluster 3
    (850,200),(855,205),(860,195),(865,210),(870,190),(860,215),
    (875,205),(865,220),(855,190),(850,215),

    # Noise / outliers
    (50,900),(900,50),(400,800),(800,400),(100,700),(700,100),
    (300,300),(900,900),(50,50),(950,950),
    (500,100),(100,500),(750,750),(250,900),(900,250),
    (600,100),(100,600),(850,500),(500,850),(50,500),
    (500,50),(300,700),(700,300),(200,800),(800,200)
]
noisy_points_labels = [0] * 10 + [1] * 10 + [2] * 10 + [-1] * 25
database['very dense clusters + noisy points'] = noisy_points, noisy_points_labels

two_lines = [
    # line 1 (diagonal line)
    (100,100),(120,120),(140,140),(160,160),(180,180),
    (200,200),(220,220),(240,240),(260,260),(280,280),
    (300,300),(320,320),(340,340),(360,360),(380,380),
    (400,400),(420,420),(440,440),(460,460),(480,480),
    (110,105),(130,125),(150,145),(170,165),(190,185),

    # line 2 (another diagonal)
    (600,200),(620,220),(640,240),(660,260),(680,280),
    (700,300),(720,320),(740,340),(760,360),(780,380),
    (800,400),(820,420),(840,440),(860,460),(880,480),
    (900,500),(920,520),(940,540),(960,560),(980,580),
    (610,205),(630,225),(650,245),(670,265),(690,285), (710,305),(730,325)
]
two_lines_labels = [0]*25 + [1]*27
database['two lines'] = two_lines, two_lines_labels
                
classic_set = [
    # Cluster A
    (2,2),(2,4),(2,6),(4,2),(4,4),(4,6),(6,2),(6,4),(6,6),
    (3,3),(3,5),(5,3),(5,5),

    # Cluster B
    (18,2),(18,4),(18,6),(20,2),(20,4),(20,6),(22,2),(22,4),(22,6),
    (19,3),(19,5),(21,3),(21,5),

    # Cluster C
    (10,14),(10,16),(10,18),(12,14),(12,16),(12,18),(14,14),(14,16),(14,18),
    (11,15),(11,17),(13,15),(13,17),
    (9,15),(15,17),(8,16),(16,14)
]
classic_set_labels = [0] * 13 + [1] * 13 + [2] * 17
database['classic set'] = classic_set, classic_set_labels

random_noises = [

    (12, 450), (789, 123), (456, 987), (234, 678), (567, 345),
    (890, 234), (345, 876), (123, 567), (678, 789), (432, 210),
    (876, 543), (210, 432), (345, 123), (567, 678), (234, 345),
    (789, 890), (654, 321), (432, 876), (210, 123), (987, 456),
    (123, 789), (678, 432), (345, 567), (876, 210), (543, 345),
    (210, 654), (432, 876), (765, 234), (321, 543), (678, 987),
    (123, 210), (456, 678), (789, 345), (234, 567), (567, 890),
    (890, 123), (345, 432), (123, 654), (678, 210), (432, 543),
    (210, 765), (987, 678), (543, 210), (654, 987), (321, 876),
    (876, 543), (210, 432), (432, 210), (765, 123), (123, 876),
    (543, 678), (678, 432), (890, 567), (345, 789), (567, 234),
    (234, 890), (789, 345), (432, 654), (210, 543), (654, 321),
    (321, 654), (876, 210), (543, 432), (210, 765), (987, 123),
    (123, 432), (678, 543), (345, 210), (567, 876), (234, 345),
    (789, 678), (432, 123), (210, 567), (654, 890), (321, 210),
    (876, 345), (543, 678), (210, 432), (432, 210), (765, 345),
    (123, 654), (543, 210), (678, 987), (890, 432), (345, 123),
    (567, 210), (234, 543), (789, 876), (432, 345), (210, 678),
    (654, 123), (321, 432), (876, 210), (543, 765), (210, 123),
    
    
    (100, 100), (105, 102), (98, 97), (102, 105), (101, 99),
    (99, 104), (103, 101), (97, 102),


    (700, 200), (705, 198), (702, 205), (698, 203), (701, 199),
    (703, 204), (699, 201), (704, 200),

    
    (400, 800), (402, 805), (398, 798), (401, 803), (399, 801),
    (403, 804), (397, 799), (400, 802),

    
    (850, 850), (852, 848), (848, 853), (851, 849), (849, 852),
    (853, 851), (847, 850), (850, 849),

    
    (200, 700), (202, 698), (198, 703), (201, 699), (199, 702),
    (203, 701), (197, 700), (200, 699)
]
random_noises_labels = [-1] * 135
database['random noises'] = random_noises, random_noises_labels

overlapping_clusters_2 = [

    # --- Cluster 0 (dense, well-separated) ---
    (100,100),(110,105),(120,110),(130,115),(140,120),
    (115,95),(125,100),(135,105),(145,110),
    (110,120),(120,125),(130,130),(140,135),
    (130,120),(140,125),(135,110),

    # --- Cluster 1 (sparser) ---
    (174,145),(165,134),
    (167,156),(181,160),(189,165),(198,173),
    (180,147),(190,145),(195,154),
    (175,125),(185,130),(195,135),
    (168,157),

    # --- Cluster 2 (distinct) ---
    (240,110),(250,115),(260,120),(270,125),(280,130),
    (245,100),(255,105),(265,110),(275,115),
    (250,135),(260,140),(270,145),(280,150),
]
overlapping_clusters_2_labels = [0]*16 + [1]*13 + [2]*13 
database['overlapping clusters 2'] = overlapping_clusters_2, overlapping_clusters_2_labels


slightly_overlapping_clusters = [

    # --- Circle 1 (core-heavy) ---
    (190,200),(195,205),(200,200),(205,195),(200,210),
    (195,195),(205,205),(210,200),(190,210),(210,210),
    (195,210),(205,190),(200,195),(210,205),

    # --- Circle 2 (shifted, overlapping) ---
    (230,220),(235,225),(240,220),(245,215),(240,230),
    (235,215),(245,225),(250,220),(230,230),(250,230),
    (235,230),(245,210),(240,215),(250,225),

    # --- Circle 3 (partial overlap with both) ---
    (215,240),(220,245),(225,240),(230,235),(225,250),
    (220,235),(230,245),(235,240),(215,250),(235,250),
    (220,250),(230,230)
]
slightly_overlapping_clusters_labels = [0]*14 + [1]*14 + [2]*12
database['slightly overlapping clusters'] = slightly_overlapping_clusters, slightly_overlapping_clusters_labels

three_vertical_lines = [

    # Tight core cluster
    (100,100),(102,101),(98,99),(101,103),(99,102),
    (103,100),(97,98),(100,104),

    # Medium-distance ring
    (150,100),(152,102),(148,98),(150,105),(145,100),
    (155,100),(150,95),

    # Far sparse points
    (220,100),(225,105),(215,95),(230,100),(210,100)
]
three_vertical_lines_labels = [0]*8 + [1]*7 + [2]*5
database['three vertical lines'] = three_vertical_lines, three_vertical_lines_labels

grid = [

    (50,50),(50,100),(50,150),(50,200),
    (100,50),(100,100),(100,150),(100,200),
    (150,50),(150,100),(150,150),(150,200),
    (200,50),(200,100),(200,150),(200,200)
]
grid_labels = [-1] * 16
database['grid'] = grid, grid_labels

cluster_plus_line = [

    # Real cluster
    (100,400),(105,405),(95,395),(110,400),(100,410),
    (90,390),(108,395),(102,402),

    # Gradient (no real clusters)
    (200,100),(220,120),(240,140),(260,160),(280,180),
    (300,200),(320,220),(340,240),(360,260),(380,280),
    (400,300)
]
cluster_plus_line_labels = [0]*8 + [1]*11
database['one cluster and one line'] = cluster_plus_line, cluster_plus_line_labels

concentric_circles = [

    # Inner circle
    (300,300),(305,300),(300,305),(295,300),(300,295),
    (303,303),(297,297),(303,297),(297,303),

    # Outer circle
    (330,300),(315,330),(300,340),(285,330),(270,300),
    (285,270),(300,260),(315,270),
    (320,320),(280,320),(280,280),(320,280)
]
concentric_circles_labels = [0]*9 + [1]*12
database['concentric circles'] = concentric_circles, concentric_circles_labels


def filter_datasets(only_from_clustered : bool, max_set_len: int, dbase : Optional[Dict[Any, Any]] = None) -> List[str]:
    '''Returns a list of all datasets from a given database that satisfy given parameters
       
       If you want to use database other from myclustering.database.database (standard), you must specify it
       only_from_clustered  - excludes datasets which contain only unclustered points
       (all labels = -1)
       max_set_len - excludes datasets which have more points that given value'''
    if dbase is None:
        dbase = database

    for k, v in dbase.items():
        options = []
        points, labels = v
        set_len = len(points)
        if (set_len <= max_set_len):
            set_has_clusters = (labels != [-1] * set_len)
            if only_from_clustered:
                if set_has_clusters:
                    options.append(k)
            else:
                options.append(k)
    return options


def load_random_dataset(dbase : Optional[Dict[Any, Any]] = None, options: List[str] | Literal['All'] = 'All') -> Tuple[List[Point], Labels]:
    '''
    Loads dataset from a given database. Set name is selected randomly from options
    If you want to use database other from myclustering.database.database (standard), you must specify it
    '''
    if dbase is None:
        dbase = database
    if options == 'All':
        options = list(dbase.keys())

    sset_name = random.choice(options)
    sset = dbase[sset_name]
    return sset_name, sset

def load_dataset(set_name: str, dbase : Optional[Dict[Any, Any]] = None) -> Tuple[List[Point], Labels]:
    '''
    Loads dataset with given name from a given database.
    If you want to use database other from this package's standard, you must specify it
    '''
    if dbase is None:
        dbase = database

    try:
        sset = dbase[set_name]
    except KeyError:
        raise KeyError(f'No set named {set_name} was found.')
    return set_name, sset