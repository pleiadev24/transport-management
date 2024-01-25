class Vehicle:
    def __init__(self, vehicle_id, capacity):
        self.vehicle_id = vehicle_id
        self.capacity = capacity
        self.current_cargo = []

    def load_cargo(self, cargo):
        if len(self.current_cargo) + len(cargo) <= self.capacity:
            self.current_cargo.extend(cargo)
            print(f"Cargo loaded into {self.vehicle_id}: {cargo}")
        else:
            print(f"Error: Cargo capacity exceeded for {self.vehicle_id}")

    def display_status(self):
        print(f"{self.vehicle_id} - Current Cargo: {self.current_cargo}")


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


