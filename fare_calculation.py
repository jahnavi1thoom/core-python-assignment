trips = [5, 10, 3]
def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10 * distance
    total = base_fare + distance_fare
    return total
total_fare = 0
for i, distance in enumerate(trips, 1):
    fare = calculate_fare(distance)
    print(f"Trip {i}: ${fare}")
    total_fare += fare

print("Total Fare: $", total_fare)
