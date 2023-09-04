class Vehicle:
    def __init__(self):
        self.owner_name = ""
        self.vin = ""
        self.manufacturer = ""

    def input_data(self):
        self.owner_name = input("Enter the owner's name: ")
        self.vin = input("Enter the vehicle identification number (VIN): ")
        self.manufacturer = input("Enter the name of the manufacturer: ")

    def display_data(self):
        print("Owner's Name:", self.owner_name)
        print("Vehicle Identification Number (VIN):", self.vin)
        print("Manufacturer:", self.manufacturer)


class Passenger(Vehicle):
    def __init__(self):
        super().__init__()
        self.num_passengers = 0

    def input_data(self):
        super().input_data()
        self.num_passengers = int(input("Enter the number of passengers: "))

    def display_data(self):
        super().display_data()
        print("Number of Passengers:", self.num_passengers)


# Example usage:
if __name__ == "__main__":
    passenger_vehicle = Passenger()
    print("Enter details for the passenger vehicle:")
    passenger_vehicle.input_data()
    print("\nVehicle Details:")
    passenger_vehicle.display_data()
