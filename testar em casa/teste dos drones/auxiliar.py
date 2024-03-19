import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import numpy as np
from request import *
from rotas import *


def calculate_circular_trajectory(radius, angle_degrees):
    angle_radians = math.radians(angle_degrees)
    x = radius * math.cos(angle_radians)
    y = radius * math.sin(angle_radians)
    return x, y


def create_satellite_network(num_satellites, num_base_stations):
    G = nx.Graph()

    for i in range(num_satellites):
        G.add_node(f'Satellite_{i}', type='Satellite', angle=0)

    for i in range(num_base_stations):
        G.add_node(f'BaseStation_{i}', type='BaseStation', pos=(i * 2, 0))

    for base_station in G.nodes(data=True):
        if base_station[1]['type'] == 'BaseStation':
            for satellite in G.nodes(data=True):
                if satellite[1]['type'] == 'Satellite':
                    angle_degrees = (360 / num_satellites) * int(satellite[0].split('_')[1])
                    distance = math.sqrt((calculate_circular_trajectory(1, angle_degrees)[0] - base_station[1]['pos'][0])**2
                                         + (calculate_circular_trajectory(1, angle_degrees)[1] - base_station[1]['pos'][1])**2) * 300.0
                    G.add_edge(base_station[0], satellite[0], distance=distance)
    
    return G