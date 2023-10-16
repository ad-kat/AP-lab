class Owner:
    def __init__(self, name, address, profession, license_number):
        self.name = name
        self.address = address
        self.profession = profession
        self.license_number = license_number

    def displayOwner(self):
        print("Owner Details:")
        print("Name:", self.name)
        print("Address:", self.address)
        print("Profession:", self.profession)
        print("Driving License Number:", self.license_number)
        print()

class Car:
    def __init__(self, engine_number, reg_number, reg_date, color, owner, model):
        self.engine_number = engine_number
        self.reg_number = reg_number
        self.reg_date = reg_date
        self.color = color
        self.owner = owner
        self.model = model

    def displayCarDetails(self):
        print("Car Details:")
        print("Engine Number:", self.engine_number)
        print("Registration Number:", self.reg_number)
        print("Registration Date:", self.reg_date)
        print("Color:", self.color)
        print("Model:", self.model)
        self.owner.displayOwner()  # Utilize the Owner class's displayOwner method
        print()

# Create an array of five Owner objects
owners = [
    Owner("adri", "123 Main St", "student", "DL12345"),
    Owner("angira", "456 Elm St", "Engineer", "DL67890"),
    Owner("amita", "789 Oak St", "Doctor", "DL54321"),
    Owner("anupam", "101 Pine St", "Doctor", "DL98765"),
    Owner("aadhyashri", "202 Cedar St", "Doctor", "DL23456")
]

# Create an array of five Car objects, associating each car with an owner
cars = [
    Car("123ABC", "XYZ123", "2022-01-01", "none", owners[0], "carless"),
    Car("456DEF", "PQR456", "2022-02-15", "grey", owners[1], "mercedes"),
    Car("789GHI", "LMN789", "2022-03-20", "silver", owners[2], "creta"),
    Car("101JKL", "OPQ101", "2022-04-10", "black", owners[3], "vitara"),
    Car("202MNO", "RST202", "2022-05-05", "White", owners[4], "BMW")
]

# Display details of all cars
for car in cars:
    car.displayCarDetails()
