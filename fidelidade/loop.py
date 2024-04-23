import random

def simulate_allocation(total_requests, time_window, batch_size, requests_per_slot):
    allocated_requests = 0
    current_batch = 1

    while allocated_requests < total_requests:
        print(f"\nProcessing Batch {current_batch}:")
        remaining_requests = total_requests - allocated_requests

        for time_slot in range(1, time_window + 1):
            requests_in_time_slot = min(requests_per_slot, remaining_requests)
            allocated_requests += allocate_requests(requests_in_time_slot, time_slot, current_batch)

        current_batch += 1

    print(f"\nTotal Requests: {total_requests}")
    print(f"Allocated Requests: {allocated_requests}")

def allocate_requests(requests_in_time_slot, time_slot, current_batch):
    allocated = 0
    print(f"\nAllocating requests for Time Slot {time_slot} (Batch {current_batch}):")

    for _ in range(requests_in_time_slot):
        if random.choice([True, False]):
            allocated += 1
            print(f"Request {allocated} allocated.")

    return allocated

# Set your parameters
total_requests = 100
time_window = 5
batch_size = 20
requests_per_slot = 2

# Run the simulation
simulate_allocation(total_requests, time_window, batch_size, requests_per_slot)

