# shopping list
# view items in the list, remove items, add items
#read write open close files
list = []
file = "Groceries.txt"

#load the file into the list
def LoadList():
    print(f"Loading {file}")
    
    try:
        f = open(f"{file}", 'r')      #this opens the file in read mode
        for line in f:
            line = line.strip()
            list.append(line)
        f.close()           #close the file
    except FileNotFoundError as err:
        print(err)
        print(f"Creating {file}")
        f = open(f"{file}", 'w')        #create the groceries file
        f.close()
        
def AddItem():
    item = input("What item do you want to add to the list? ")
    list.append(item) #append to the kist
    
    try:
        print(f"Adding {item} to the {file}")
        f = open(f"{file}", 'a')      #open file to append item to the list
        f.write(item + "\n")        #write item and move to the next line
        f.close()       #close the file
        
    except FileNotFoundError as err:
        print(err)
        
def ViewList():
    print(f"Here are the items in the {file}")
    for i in list:      #iterate through each item in the list
        print(i)        # print out each item found
    SaveList()
    
def SaveList():
    try:
        f = open(file, 'w')
        for i in list:      #for each item in the list write to file
            f.write(i + "\n")
        f.close()
    except FileNotFoundError as err:
        print(err)
        
def RemoveItem():
    try:
        item = input(f"What item would you like to remove from the  {file}")
        list.remove(item)       #remove from the array
        ViewList()
        SaveList()
    except ValueError as err:
        print(f"{item} is not in the list. remember that items in the list are case sensitive")
        ViewList()
        
def Menu():
    print(f"1: Add an item to the {file}")
    
    print(f"2: Remove an item to the {file}")
    
    print(f"3: Show the items in the {file}")
    
    print(f"4: Quit")
    
choice = 0

while choice !=4:
    ViewList()
    Menu()
    try:
        choice = int(input("Make a choice from the above options: "))
        if choice == 1:
            AddItem()
        if choice == 2:
            RemoveItem()
        if choice == 3:
            ViewList()
        if choice == 4:
            print("Thanks for using the ListGenerator")
        else:
            raise Exception ("Not a valid number")
    except ValueError as err:
        print("Enter a number integer between 1 and 4")
    except: 
        print("Enter an integer between 1 and 4")

Loadlist()
AddItem()
ViewList()
SaveList()
RemoveItem()