"""
Class Hierarchy Implementation
----------------------------
Implement the following class hierarchy according to the specified requirements.
This exercise focuses on inheritance, polymorphism, and method overriding.
"""

class Vehicle:
    """
    Base class for all vehicles.
    
    Attributes:
        make (str): The manufacturer of the vehicle
        model (str): The model of the vehicle
        year (int): The production year
        fuel_level (float): Current fuel level as a percentage (0-100)
        
    Methods:
        refuel(amount): Add fuel to the vehicle
        drive(distance): Simulate driving the vehicle a certain distance
        get_info(): Return a string with the vehicle information
        get_fuel_level(): Return the current fuel level
    """
    
    def __init__(self, make, model, year, fuel_level=100):
        """
        Initialize a new Vehicle instance.
        
        Args:
            make (str): The manufacturer of the vehicle
            model (str): The model of the vehicle
            year (int): The production year
            fuel_level (float, optional): Starting fuel level. Defaults to 100.
        """
        # YOUR CODE HERE
        pass
    
    def refuel(self, amount):
        """
        Add fuel to the vehicle.
        
        Args:
            amount (float): Amount of fuel to add (percentage points)
            
        Returns:
            float: The new fuel level
            
        Raises:
            ValueError: If amount is negative
            ValueError: If adding would exceed 100%
        """
        # YOUR CODE HERE
        pass
    
    def drive(self, distance):
        """
        Simulate driving the vehicle a certain distance.
        Base method to be overridden by subclasses.
        
        Args:
            distance (float): Distance to drive
            
        Returns:
            bool: True if the drive was completed, False if not enough fuel
        """
        # YOUR CODE HERE
        pass
    
    def get_info(self):
        """
        Get information about the vehicle.
        
        Returns:
            str: A string containing the vehicle details
        """
        # YOUR CODE HERE
        pass
    
    def get_fuel_level(self):
        """
        Get the current fuel level.
        
        Returns:
            float: The current fuel level (0-100)
        """
        # YOUR CODE HERE
        pass


class Car(Vehicle):
    """
    A class representing a car, inheriting from Vehicle.
    
    Additional Attributes:
        num_doors (int): Number of doors
        is_electric (bool): Whether the car is electric
        
    Methods:
        All methods from Vehicle
        plus:
        honk(): Make the car honk
    """
    
    def __init__(self, make, model, year, num_doors, is_electric=False, fuel_level=100):
        """
        Initialize a new Car instance.
        
        Args:
            make (str): The manufacturer of the car
            model (str): The model of the car
            year (int): The production year
            num_doors (int): Number of doors
            is_electric (bool, optional): Whether the car is electric. Defaults to False.
            fuel_level (float, optional): Starting fuel level. Defaults to 100.
        """
        # YOUR CODE HERE
        pass
    
    def drive(self, distance):
        """
        Simulate driving the car a certain distance.
        Each unit of distance consumes 1% of fuel for regular cars,
        and 0.5% for electric cars.
        
        Args:
            distance (float): Distance to drive
            
        Returns:
            bool: True if the drive was completed, False if not enough fuel
        """
        # YOUR CODE HERE
        pass
    
    def honk(self):
        """
        Make the car honk.
        
        Returns:
            str: A honking sound
        """
        # YOUR CODE HERE
        pass
    
    def get_info(self):
        """
        Get information about the car.
        
        Returns:
            str: A string containing the car details
        """
        # YOUR CODE HERE
        pass


class Motorcycle(Vehicle):
    """
    A class representing a motorcycle, inheriting from Vehicle.
    
    Additional Attributes:
        has_sidecar (bool): Whether the motorcycle has a sidecar
        
    Methods:
        All methods from Vehicle
        plus:
        wheelie(): Attempt to do a wheelie
    """
    
    def __init__(self, make, model, year, has_sidecar=False, fuel_level=100):
        """
        Initialize a new Motorcycle instance.
        
        Args:
            make (str): The manufacturer of the motorcycle
            model (str): The model of the motorcycle
            year (int): The production year
            has_sidecar (bool, optional): Whether the motorcycle has a sidecar. Defaults to False.
            fuel_level (float, optional): Starting fuel level. Defaults to 100.
        """
        # YOUR CODE HERE
        pass
    
    def drive(self, distance):
        """
        Simulate driving the motorcycle a certain distance.
        Each unit of distance consumes 2% of fuel.
        If the motorcycle has a sidecar, it consumes 2.5% per unit.
        
        Args:
            distance (float): Distance to drive
            
        Returns:
            bool: True if the drive was completed, False if not enough fuel
        """
        # YOUR CODE HERE
        pass
    
    def wheelie(self):
        """
        Attempt to do a wheelie. 
        Only possible if the motorcycle doesn't have a sidecar.
        
        Returns:
            str: The result of the wheelie attempt
        """
        # YOUR CODE HERE
        pass
    
    def get_info(self):
        """
        Get information about the motorcycle.
        
        Returns:
            str: A string containing the motorcycle details
        """
        # YOUR CODE HERE
        pass


class Truck(Vehicle):
    """
    A class representing a truck, inheriting from Vehicle.
    
    Additional Attributes:
        cargo_capacity (float): The cargo capacity in tons
        current_cargo (float): The current cargo load in tons
        
    Methods:
        All methods from Vehicle
        plus:
        load_cargo(amount): Load cargo onto the truck
        unload_cargo(amount): Unload cargo from the truck
    """
    
    def __init__(self, make, model, year, cargo_capacity, fuel_level=100):
        """
        Initialize a new Truck instance.
        
        Args:
            make (str): The manufacturer of the truck
            model (str): The model of the truck
            year (int): The production year
            cargo_capacity (float): The cargo capacity in tons
            fuel_level (float, optional): Starting fuel level. Defaults to 100.
        """
        # YOUR CODE HERE
        pass
    
    def drive(self, distance):
        """
        Simulate driving the truck a certain distance.
        Each unit of distance consumes 3% of fuel.
        Additional fuel consumption based on cargo load:
        For each ton of cargo, add 0.25% fuel consumption per unit of distance.
        
        Args:
            distance (float): Distance to drive
            
        Returns:
            bool: True if the drive was completed, False if not enough fuel
        """
        # YOUR CODE HERE
        pass
    
    def load_cargo(self, amount):
        """
        Load cargo onto the truck.
        
        Args:
            amount (float): Amount of cargo to load in tons
            
        Returns:
            float: The new cargo load
            
        Raises:
            ValueError: If amount is negative
            ValueError: If loading would exceed capacity
        """
        # YOUR CODE HERE
        pass
    
    def unload_cargo(self, amount):
        """
        Unload cargo from the truck.
        
        Args:
            amount (float): Amount of cargo to unload in tons
            
        Returns:
            float: The new cargo load
            
        Raises:
            ValueError: If amount is negative
            ValueError: If unloading more than current load
        """
        # YOUR CODE HERE
        pass
    
    def get_info(self):
        """
        Get information about the truck.
        
        Returns:
            str: A string containing the truck details
        """
        # YOUR CODE HERE
        pass


def main():
    """Test the classes with some examples."""
    # Create a car
    print("Creating a Car...")
    car = Car("Toyota", "Corolla", 2022, 4)
    print(car.get_info())
    print(f"Fuel level: {car.get_fuel_level()}%")
    car.drive(30)
    print(f"After driving, fuel level: {car.get_fuel_level()}%")
    print(car.honk())
    
    # Create an electric car
    print("\nCreating an Electric Car...")
    electric_car = Car("Tesla", "Model 3", 2023, 4, True)
    print(electric_car.get_info())
    electric_car.drive(40)
    print(f"After driving, fuel level: {electric_car.get_fuel_level()}%")
    
    # Create a motorcycle
    print("\nCreating a Motorcycle...")
    motorcycle = Motorcycle("Harley-Davidson", "Sportster", 2021)
    print(motorcycle.get_info())
    print(motorcycle.wheelie())
    motorcycle.drive(15)
    print(f"After driving, fuel level: {motorcycle.get_fuel_level()}%")
    
    # Create a motorcycle with sidecar
    print("\nCreating a Motorcycle with Sidecar...")
    sidecar_motorcycle = Motorcycle("BMW", "R1250GS", 2023, True)
    print(sidecar_motorcycle.get_info())
    print(sidecar_motorcycle.wheelie())
    
    # Create a truck
    print("\nCreating a Truck...")
    truck = Truck("Ford", "F-150", 2020, 2.5)
    print(truck.get_info())
    truck.load_cargo(1.5)
    print(f"Loaded 1.5 tons of cargo")
    truck.drive(10)
    print(f"After driving, fuel level: {truck.get_fuel_level()}%")
    truck.unload_cargo(0.5)
    print(f"Unloaded 0.5 tons of cargo")

if __name__ == "__main__":
    main()