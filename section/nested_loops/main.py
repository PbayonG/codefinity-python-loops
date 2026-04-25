# List of travel costs (each sublist represents a trip)
travel_costs = [
    [5, 15, 10, 8, 25, 30, 55, 68, 75, 5],
    [60, 20, 60, 70, 80, 80, 80, 90, 90, 90],
    [100, 100, 100, 100, 50, 110, 110, 120, 120, 120, 130],
    [130, 140, 39, 140, 150, 150, 150, 150, 160, 160],
    [170, 180, 180, 190, 40, 190, 200],
    [200, 200, 200, 210, 11, 220, 220, 220, 250, 250, 250],
    [280, 300, 300, 110, 300, 320, 350, 400, 400, 450],
    [480, 500, 500, 90, 500, 550, 600, 700]
]

# List to store maximum costs per trip
max_costs = []

trip = 0
while trip < len(travel_costs):
    maxim_cost = 0
    cost = 0
    while cost < len(travel_costs[trip]):
        if maxim_cost < travel_costs[trip][cost]:
            maxim_cost = travel_costs[trip][cost]
        cost += 1
    max_costs.append(maxim_cost)
    trip +=1
        





# Testing
print('Maximum Travel Costs:', max_costs)