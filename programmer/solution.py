from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    total_weight = 0
    passing_truck = deque([])
    passing_count = deque([])
    while len(truck_weights) != 0 or len(passing_truck) != 0:
        time += 1
        if passing_count and passing_count[0] >= bridge_length:
            passing_count.popleft()
            total_weight -= passing_truck.popleft()

        if truck_weights and total_weight+truck_weights[0] <= weight:
            truck = truck_weights.pop(0)
            total_weight += truck
            passing_count.append(0)
            passing_truck.append(truck)

        for i in range(len(passing_count)):
            passing_count[i] += 1
    return time