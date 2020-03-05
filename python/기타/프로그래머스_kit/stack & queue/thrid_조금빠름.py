# bridge_length = 2
# weight = 10
# truck_weights = [7, 4, 5, 6]

def solution(bridge_length, weight, truck_weights):
    time = 1
    passing_truck= []
    passed_truck= []
    current_mass = 0
    time_dic = {}

    while True:
        while truck_weights:
            if weight >= current_mass + truck_weights[0]:
                passing_truck.append(truck_weights.pop(0))
                time_dic[time] = bridge_length + time
                current_mass = sum(passing_truck)
                break
            else :
                break

        time += 1

        for out_time in time_dic:
            if time_dic[out_time] == time:
                passed_truck.append(passing_truck.pop(0))

        current_mass = sum(passing_truck)

        if passing_truck == [] and truck_weights== []:
            break
    return time