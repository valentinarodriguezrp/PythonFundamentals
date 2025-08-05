#codeAlong10.py
class EngineType:
    #valid engine types
    VALID_ENGINE_TYPES = {'gasoline', 'diesel', 'electric', 'hybrid'}
    
    def __init__(self, engine_type, fuel_efficiency, horsepower = None, battery_capacity=None):
        if engine_type.lower() not in self.VALID_ENGINE_TYPES:
            raise ValueError (f"Engine type must be one of {self.VALID_ENGINE_TYPES}, you entered {engine_type}")
        
        #valid fuel efficiency
        if not isinstance(fuel_efficiency, (int, float)) or fuel_efficiency <= 0:
            raise ValueError("Fuel efficiency must be a positive number")
        self.engine_type = engine_type.lower()
        self.fuel_efficiency = fuel_efficiency
        self.horsepower = horsepower
        self.battery_capacity = battery_capacity #kW/h applicable to electric engines
        
    def describe_engine(self):
        #determine the unit base done engine type
        efficiency_unit = 'kWh/100 miles' if self.engine_type == 'electric' else 'miles/gallon'
        base_info = f"Engine type: {self.engine_type.capitalize()}, Fule Efficiency: {self.fuel_efficiency} {efficiency_unit}"
        if self.horsepower:
            base_info += f", Horsepower: {self.horsepower} HP"
        if self.battery_capacity and self.engine_type == 'electric':
            base_info += f", Battery Capacity: {self.battery_capacity} kWh"
        return base_info
    
    def charge(self):
        if self.engine_type != 'electric':
            raise ValueError ("only electric engines can be charged")
        return "Charging electric engine...."
    

class Vehicle:
    
    def __init__ (self, make, model, year, color, engine_type, fuel_efficiency, horsepower=None, battery_capacity=None):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.started = False
        self.speed = 0
        self.max_speed = 200
        self.engine = EngineType(engine_type, fuel_efficiency, horsepower, battery_capacity)
        
    def accelerate(self, value):
        if not self.started:
            print("The car is not started.")
            return
        if self.speed + value <= self.max_speed:
            self.speed += value
        else:
            self.speed = self.max_speed
        print(f"Accelerating to {self.speed} km/h ....")
        
    def brake(self, value):
        if self.speed - value >= 0:
            self.speed -= value
        else:
            self.speed = 0
        print(f"Braking to {self.speed} km/h ....")
    
    def start(self):
        if self.started:
            print("Engine is running")
        else:
            print(f"Starting {self.engine.engine_type} engine")
            self.started = True
            
    def stop(self):
        if not self.started:
            print("Engine is already stopped")
        else:
            print(f"Stopping {self.engine.engine_type} engine")
            self.started = False
            
    def get_status(self):
        return "running" if self.started else "stopped"   
    
    def charge_engine(self):
        return self.engine.charge()
        
    def __str__(self):
        return f"{self.make} {self.model} {self.year} {self.color} {self.engine.engine_type}"
    
    def __repr__(self):
        return (
            
            f"{type(self).__name__}"
            f'(make="{self.make}",'
            f'model = "{self.model}",'
            f'year = "{self.year}",'
            f'color = "{self.color}",'
        )
        
def main():
    try:
        #create a bunch of vehicles with different models, colors, years, and makes.
        car1 = Vehicle("Toyota", "Camry", 2024, "White", "gasoline", 30, horsepower = 203)
        car2 = Vehicle("GMC", "Yukon", 2015, "Black", "diesel", 13, horsepower = 250)
        car3 = Vehicle("Kia", "Sorento", 2019, "Blue", "hybrid", 45, horsepower = 175)
        car4 = Vehicle("Honda", "CRV", 2025, "Orange", "gasoline", 14, horsepower = 203)
        car5 = Vehicle("Tesla", "Model y", 2025, "Grey", "electric", 104, battery_capacity = 200)
        
        vehicles = [car1, car2, car3, car4, car5]
        for vehicle in vehicles:
            print(vehicle)
            vehicle.start()
            print(vehicle)
            if vehicle.engine.engine_type == 'electric':
                print(vehicle.charge_engine())
            vehicle.stop()
            print(vehicle)
            print("-"*50)
                 
    except ValueError as e:
        print(f"Error: {e}")
        
if __name__ =="__main__":
    main()