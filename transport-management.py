#add fiel efficiency and emission
class Vehicle:
    def __init__(self, vehicle_id, capacity, fuel_efficiency, emission_standard):
        self.vehicle_id = vehicle_id
        self.capacity = capacity
        self.current_cargo = []
        self.fuel_efficiency = fuel_efficiency
        self.emission_standard = emission_standard  # Emission standard (e.g., Euro 6)

    def load_cargo(self, cargo):
        if len(self.current_cargo) + len(cargo) <= self.capacity:
            self.current_cargo.extend(cargo)
            print(f"Cargo loaded into {self.vehicle_id}: {cargo}")
        else:
            print(f"Error: Cargo capacity exceeded for {self.vehicle_id}")

    def calculate_fuel_consumption(self, distance):
        return distance / self.fuel_efficiency

    def calculate_emission(self, distance):
        emission_factor = 2.5 if self.emission_standard == "Euro 6" else 3.5
        return distance * emission_factor

    def display_status(self):
        print(f"{self.vehicle_id} - Capacity: {self.capacity}, Current Cargo: {self.current_cargo}")


class Route:
    def __init__(self, source, destination, distance):
        self.source = source
        self.destination = destination
        self.distance = distance

    def display_info(self):
        print(f"Route from {self.source} to {self.destination} - Distance: {self.distance} km")


class TransportManagementSystem:
    def __init__(self):
        self.vehicles = []
        self.routes = []

    def add_vehicle(self, vehicle_id, capacity):
        vehicle = Vehicle(vehicle_id, capacity)
        self.vehicles.append(vehicle)
        print(f"Vehicle {vehicle_id} added to the fleet with capacity {capacity}")

    def add_route(self, source, destination, distance):
        route = Route(source, destination, distance)
        self.routes.append(route)
        print(f"Route from {source} to {destination} added with distance {distance} km")

    def display_fleet_status(self):
        print("\nFleet Status:")
        for vehicle in self.vehicles:
            vehicle.display_status()

    def display_routes_info(self):
        print("\nRoute Information:")
        for route in self.routes:
            route.display_info()


