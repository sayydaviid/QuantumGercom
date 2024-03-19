import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import numpy as np
from auxiliar import *
from request import *



def find_shortest_route(graph, source, target, max_distance):
    try:
        # Use Dijkstra's algorithm to find the shortest path
        shortest_path = nx.shortest_path(graph, source=source, target=target, weight='distance')

        # Check if all links in the route are within the max distance constraint
        for i in range(len(shortest_path) - 1):
            current_node = shortest_path[i]
            next_node = shortest_path[i + 1]
            distance = graph[current_node][next_node]['distance']
            if distance > max_distance:
                raise nx.NetworkXNoPath

        # Extract information about each hop in the path
        hops = []
        total_distance = 0.0
        for i in range(len(shortest_path) - 1):
            current_node = shortest_path[i]
            next_node = shortest_path[i + 1]
            distance = graph[current_node][next_node]['distance']
            hops.append({'source': current_node, 'target': next_node, 'distance': distance})
            total_distance += distance

        return hops, total_distance

    except nx.NetworkXNoPath:
        return None, None
    

def allocate_drones(route, max_distance=1000, drone_range=100,max_drones=10):
    if route is None:
        print("No direct route found.")
        return None

    new_route = []
    total_drones = 0

    for hop in route:
        source = hop['source']
        target = hop['target']
        distance = hop['distance']

        if distance <= max_distance:
            new_route.append({'source': source, 'target': target, 'distance': distance})
        else:
            print(f"\nLink from {source} to {target} exceeds max distance.")
            print("Need to allocate auxiliary drone nodes.")

            # Calculate the number of drones needed
            num_drones = math.ceil((distance - max_distance) / drone_range)
            print(f"Difference: {distance - max_distance} km")
            print(f"Number of drones needed: {num_drones}")
            if num_drones <=max_drones:
                # Allocate drones in the new route
                drone_distance = drone_range
                for i in range(num_drones):
                    drone_source = f'Drone_{total_drones}'
                    drone_target = f'Drone_{total_drones + 1}'
                    new_route.append({'source': drone_source, 'target': drone_target, 'distance': drone_distance})
                    total_drones += 1
                    drone_distance = drone_range if i < num_drones - 1 else (distance - max_distance) % drone_range
            else:
                print("Not Enough Drones. Needed",num_drones)
                new_route=None
                total_drones=0
                return new_route,total_drones

    return new_route,total_drones


