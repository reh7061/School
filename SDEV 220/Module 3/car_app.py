# Author: Pa Reh
# File Name: car_app.py
# Description: This app accepts user's input to create an Automobile object.
#              It gathers details like year, make, model, number of doors, and roof type,
#              and then displays the information in a formatted way.

class Vehicle:
    def __init__(self, vehicle_type: str):
        self.vehicle_type = vehicle_type


class Automobile(Vehicle):
    """A car, with year, make, model, number of doors, and roof type."""
    def __init__(self, year: int, make: str, model: str, doors: int, roof: str):
        super().__init__("car")           # always set vehicle_type to "car"
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof


def main():
    print("Enter the details of your automobile:\n")

    # Gather inputs
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")

    # Validate door input; is 2 or 4
    while True:
        doors = input("Number of doors (2 or 4): ")
        if doors in ("2", "4"):
            doors = int(doors)
            break
        print("Please enter 2 or 4.")

    # Validate roof input; is either "solid" or "sun roof"
    valid_roofs = {"solid", "sun roof"}
    while True:
        roof = input("Type of roof (solid or sun roof): ").strip().lower()
        if roof in valid_roofs:
            break
        print("Please enter 'solid' or 'sun roof'.")

    # Create the Automobile instance
    car = Automobile(int(year), make, model, doors, roof)

    # Output the vehicle information
    print("\nVehicle Information:")
    print(f"  Vehicle type: {car.vehicle_type}")
    print(f"  Year: {car.year}")
    print(f"  Make: {car.make}")
    print(f"  Model: {car.model}")
    print(f"  Number of doors: {car.doors}")
    print(f"  Type of roof: {car.roof}")


if __name__ == "__main__":
    main()
