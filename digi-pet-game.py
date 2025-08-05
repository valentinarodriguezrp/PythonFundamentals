#lab10.py

import random
import time

class DigiPet:
    def __init__(self, name):
        self.name = name
        self.happiness = 100
        self.food_level = 100
        self.health = 100
        self.age = 0
        
    def age_pet(self):
        self.age += 1
        self.happiness -= random.randint(2, 5)
        self.food_level -= random.randint(1, 3)
        self.health -= random.randint(1, 2)
        
        self.happiness = max(0, self.happiness)
        self.food_level = max(0, self.food_level)
        self.health = max(0, self.health)
        
        if self.happiness == 0 or self.food_level == 0 or self.health == 0:
            print(f"{self.name} has passed away... :(")
            return True
        return False
    
    def read(self):
        if self.food_level > 10:
            self.happiness += random.randint(3, 7)
            self.food_level -= random.randint(1, 5)
            self.health -= random.randint(1, 2)
        else:
            print(f"{self.name} is too hungry to read. You should feed it!")
        
    def pizza(self):
        self.food_level += random.randint(5, 10)
        self.food_level = min(100, self.food_level)  
        self.health += random.randint(1, 3)
        
    def pilates(self):
        if self.food_level > 10:
            self.happiness += random.randint(2, 6)
            self.food_level -= random.randint(3, 7)
            self.health -= random.randint(1, 2)
        else:
            print(f"{self.name} is too hungry to work out. You should feed it!")
    
    def display_status(self):
        print(f"{self.name}'s Status:")
        print(f"Happiness: {self.happiness}   Food level: {self.food_level}   Health: {self.health}   Age: {self.age}")
        print()

def main():
    pet_name = input("What would you like to name your DigiPet? ")
    pet = DigiPet(pet_name)
    
    while True:
        pet.display_status()
        
        if pet.age_pet():
            break

        print("1. Read Books")
        print("2. Eat Pizza with LOTS of cheese")
        print("3. Do Pilates")
        print("4. Quit")
        
        try:
            choice = int(input("What would you like to do today? "))
        except ValueError:
            print("Invalid input, please enter a number.")
            continue
        
        if choice == 1:
            pet.read()
        elif choice == 2:
            pet.pizza()
        elif choice == 3:
            pet.pilates()
        elif choice == 4:
            print("You chose to quit. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid action.")
        
        time.sleep(1) 

if __name__ == "__main__":
    main()