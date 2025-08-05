""" 
Valentina Rodriguez
 Final Project
 CS 1400
 4/21/2025
"""

# Class and object for Runner
class Runner:
    def __init__(self, name, category, races):
        self.name = name
        self.category = category
        self.races = races

    def bonus(self):
        return len(self.races) == 3

# Main Program Class
class RunProgram:
    def __init__(self):
        self.race_files = {
            1: "LeprechaunDash.txt",
            2: "PioneerDash.txt",
            3: "TurkeyTriathlon.txt"
        }
        self.race_costs = {
            1: 40,
            2: 48,
            3: 55
        }

    # create the file by the user
    def createRaceFile(self):
        fileName = input("What would you like to name the file? ")
        f = open(fileName, 'w')
        f.close()
        print("Your file was created.")

    # Register the runner or runners
    def registerRunner(self):
        count = int(input("How many runners will you be registering: "))
        for _ in range(count):
            name = input("What is the name of the runner? ")
            print("What is the category of the runner? ")
            print("1. Student\n2. Faculty\n3. Community member")
            category = int(input("Choice selected: "))

            print("The runner can register for the following races: ")
            print("1. Leprechaun Dash\n2. Pioneer Days 5k\n3. Turkey Triathlon")
            race = input("Which races will the runner register for? \nRaces Selected (type like: 1,2,3): ")
            race_ids = list(map(int, race.replace(" ", "").split(',')))

            runner = Runner(name, category, race_ids)

            total_cost = sum(self.race_costs[r] for r in race_ids)
            if runner.bonus():
                print("The runner qualifies for a 20% discount!")
                total_cost *= 0.8

            for race_id in race_ids:
                with open(self.race_files[race_id], 'a') as file:
                    file.write(runner.name + "\n")

            print(f"{runner.name} has been registered to the races.")
            print(f"The cost is ${total_cost:.2f}")

    # print those who qualify for bonus metals
    def printQualifiers(self):
        try:
            with open(self.race_files[1], 'r') as f1, \
                 open(self.race_files[2], 'r') as f2, \
                 open(self.race_files[3], 'r') as f3:

                r1 = set(f1.read().splitlines())
                r2 = set(f2.read().splitlines())
                r3 = set(f3.read().splitlines())
                qualifiers = r1 & r2 & r3

                print("Bonus Medal Qualifiers")
                for name in qualifiers:
                    print(name)
        except FileNotFoundError:
            print("One or more race files do not exist yet.")

    # print all participants
    def viewList(self):
        print("Which race participants would you like to print?")
        print("1. Leprechaun Dash\n2. Pioneer Days 5k\n3. Turkey Triathlon")
        choice = int(input("Choice Selected: "))
        filename = self.race_files.get(choice)

        try:
            print(f"\n{filename.replace('.txt', '')} Participants")
            with open(filename, 'r') as f:
                for line in f:
                    print(line.strip())
        except FileNotFoundError:
            print("That file doesn't exist yet.")

# Main Menu
def menu():
    print("\nMain Menu")
    print("1. Create a Fun Run File")
    print("2. Register Participant")
    print("3. Print Qualifiers for Bonus Medals")
    print("4. Print race day participants")
    print("5. Quit")

# Start program
program = RunProgram()

menu()
option = int(input("Choice Select: "))

while option != 5:
    if option == 1:
        program.createRaceFile()
    elif option == 2:
        program.registerRunner()
    elif option == 3:
        program.printQualifiers()
    elif option == 4:
        program.viewList()
    else:
        print("Invalid entry")

    menu()
    option = int(input("Choice Select: "))

print("Thank you for registering!")

""" Resources that helped me with this assignment include: 
https://www.w3schools.com/python/python_lists.asp
https://stackoverflow.com/questions/70053821/how-to-create-a-txt-file-with-a-user-inputted-name-in-python
https://youtu.be/daefaLgNkw0?si=2DVThp6p5ab6tpB9
https://youtu.be/MZZSMaEAC2g?si=8WSsW2Xj3kJVhZvN
"""