import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math
import random
import time
import numpy as np
from auxiliar import *
from request import *
from rotas import *

def gerador_requests(num_requests):
    requests = []
    for _ in range(num_requests):
        source_base_station = random.choice([node for node, data in G.nodes(data=True) if data['type'] == 'BaseStation'])
        target_base_station = random.choice([node for node, data in G.nodes(data=True) if data['type'] == 'BaseStation' and node != source_base_station])
        #tempo_maximo_da_requisao=15
        requests.append((source_base_station, target_base_station))
    return requests


num_satellites = 30
num_base_stations = 12
num_requests = 100 # Number of time slots
time_slot_duration = 5  # Duration of each time slot in seconds

G = create_satellite_network(num_satellites, num_base_stations)

requests = gerador_requests(num_requests)

successful_requests = 0
failed_requests = 0
final_total_drones = 0


# Simulation loop
for time_slot in range(num_requests):
    print(f"\nRequest Number: {time_slot + 1}")
    
    
    # Agendamento de envio das solicitações até o tempo X
    requests_atuais = [req for req in requests if int(req[0].split('_')[-1]) < (time_slot + 1)]
    
    
    # Update satellite positions for the current time slot
# Update satellite positions and distances for the current time slot
    for satellite in G.nodes(data=True):
            if satellite[1]['type'] == 'Satellite':
                angle_degrees = satellite[1]['angle'] + random.uniform(1, 10)
                x, y = calculate_circular_trajectory(1, angle_degrees)
                satellite[1]['angle'] = angle_degrees
                G.nodes[satellite[0]]['pos'] = (x, y)
                for base_station in G.nodes(data=True):
                    if base_station[1]['type'] == 'BaseStation':
                        base_pos = base_station[1]['pos']
                        distance = math.sqrt((x - base_pos[0]) ** 2 + (y - base_pos[1]) ** 2) * 100.0
                        G.edges[base_station[0], satellite[0]]['distance'] = distance
                        
     # Re-agendar as solicitações restantes após a atualização da rede
    requests_atuais = [req for req in requests if int(req[0].split('_')[-1]) <= time_slot]
    
    
    # Generate random base station pair for route request
    source_base_station = random.choice([node for node, data in G.nodes(data=True) if data['type'] == 'BaseStation'])
    #print(source_base_station)
    target_base_station = random.choice([node for node, data in G.nodes(data=True) if data['type'] == 'BaseStation' and node != source_base_station])
    #print(target_base_station)
    # Find and print the route, considering the max distance constraint
    # for request in requests_atuais:
    #     source_base_station, target_base_station = request
    print(f"Request to find route from {source_base_station} to {target_base_station}")
    hops, total_distance = find_shortest_route(G, source_base_station, target_base_station, max_distance=1000)
    if hops is not None:
        for hop in hops:
            print(f"From {hop['source']} to {hop['target']}, Distance: {hop['distance']} km")
        print(f"Total distance: {total_distance} km")
        successful_requests += 1 #sucesso sem drones
    else:
        print("No direct route found.")
        print("Need to allocate auxiliary drone nodes.")
        hops, total_distance = find_shortest_route(G, source_base_station, target_base_station, max_distance=100000)
        new_route,total_drones = allocate_drones(hops)
        if new_route:
            print(new_route)
            for hop in new_route:
                print(f"From {hop['source']} to {hop['target']}, Distance: {hop['distance']} km")
            print(f"Total distance: {sum(hop['distance'] for hop in new_route)} km")
            print("Total Drones",total_drones)
            successful_requests += 1
            final_total_drones +=total_drones
        else:
            print("Request FAIL")
            failed_requests += 1    

    # Pause for the duration of the time slot
    #time.sleep(time_slot_duration)

# Print summary
print(f"""\nSimulation Summary:
Number of successful requests: {successful_requests}
Number of failed requests: {failed_requests}
Total number of drones: {final_total_drones}""")
