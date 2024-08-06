from typing import List

from project.route import Route
from project.user import User
from project.vehicles.base_vehicle import BaseVehicle
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VALID_VEHICLE_TYPE = {
        'PassengerCar': PassengerCar,
        'CargoVan': CargoVan
    }

    def __init__(self):
        self.users: List[User] = []
        self.vehicles: List[BaseVehicle] = []
        self.routes: List[Route] = []

    def __define_next_rout(self):
        return len(self.routes) + 1

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = next((u for u in self.users if u.driving_license_number == driving_license_number), None)
        if user:
            return f"{driving_license_number} has already been registered to our platform."
        self.users.append(User(first_name, last_name, driving_license_number))
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if not self.VALID_VEHICLE_TYPE.get(vehicle_type):
            return f"Vehicle type {vehicle_type} is inaccessible."

        vehicle = next((v for v in self.vehicles if v.license_plate_number == license_plate_number), None)
        if vehicle:
            return f"{license_plate_number} belongs to another vehicle."

        self.vehicles.append(self.VALID_VEHICLE_TYPE[vehicle_type](brand, model, license_plate_number))
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        rout_with_greater_length = next((r for r in self.routes if
                                         r.start_point == start_point and
                                         r.end_point == end_point and
                                         r.length > length), None)
        if rout_with_greater_length:
            rout_with_greater_length.is_locked = True

        equivalent_rout = next((r for r in self.routes if
                                r.start_point == start_point and
                                r.end_point == end_point and
                                r.length == length), None)
        if equivalent_rout:
            return f"{start_point}/{end_point} - {length} km had already been added to our platform."

        rout_with_less_length = next((r for r in self.routes if
                                      r.start_point == start_point and
                                      r.end_point == end_point and
                                      r.length < length), None)
        if rout_with_less_length:
            return f"{start_point}/{end_point} shorter route had already been added to our platform."

        r_id = self.__define_next_rout()
        r = Route(start_point, end_point, length, r_id)
        self.routes.append(r)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self,
                  driving_license_number: str,
                  license_plate_number: str,
                  route_id: int,
                  is_accident_happened: bool):

        user_is_blocked = next((u for u in self.users if u.driving_license_number == driving_license_number and
                                u.is_blocked), None)
        damaged_vehicle = next((v for v in self.vehicles if v.license_plate_number == license_plate_number and
                                v.is_damaged), None)
        locked_road = next((r for r in self.routes if r.route_id == route_id and r.is_locked), None)

        if user_is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."
        if damaged_vehicle:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."
        if locked_road:
            return f"Route {route_id} is locked! This trip is not allowed."

        vehicle = next((v for v in self.vehicles if v.license_plate_number == license_plate_number), None)
        user = next((u for u in self.users if u.driving_license_number == driving_license_number), None)
        if is_accident_happened:
            if vehicle:
                vehicle.is_damaged = True
            if user:
                user.decrease_rating()

        else:
            if user:
                user.increase_rating()

        needed_rout = next((r.length for r in self.routes if r.route_id == route_id), None)
        vehicle.drive(needed_rout)
        return vehicle.__str__()

    def repair_vehicles(self, count: int):
        damaged_vehicles = []
        for vehicle in self.vehicles:
            if vehicle.is_damaged:
                damaged_vehicles.append(vehicle)
        sorted_vehicles = sorted(damaged_vehicles, key=lambda v: (v.brand, v.model))

        vehicles_to_repair = sorted_vehicles[:count] if count <= len(sorted_vehicles) else sorted_vehicles
        for vehicle in vehicles_to_repair:
            vehicle.is_damaged = False
            vehicle.recharge()

        count_of_repaired_vehicles = len(vehicles_to_repair)
        return f"{count_of_repaired_vehicles} vehicles were successfully repaired!"

    def users_report(self):
        output = ['*** E-Drive-Rent ***']
        sorted_users = sorted(self.users, key=lambda u: u.rating, reverse=True)
        for user in sorted_users:
            output.append(user.__str__())

        return '\n'.join(output)
