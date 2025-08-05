# Employee need to enter work hoirs
#Work hours must be in integers
#Work Hours nust be between 0 and 80 hours for two week period
#employee must enter their name
#Print out the name of the employee and hours worked

Employee = ''
HoursWorked = ''
Employee = input("Enter the Employee Name: ")
HoursWorked = input("Enter the number of hours worked(Should be between 0 and 80): ")

def checkPositiveNumberValue(hours):
    while True:
        try:
            hours = int(hours)
            if hours < 0 or hours > 80:
                raise IndexError("Invalid number of hours worked, should be between 0 and 80. ")
            
            return hours
        except ValueError:
            hours = input("Value must be a integer: ")
        except:
            print("Invalid number of hours worked entered. Hours must be between 0 and 80.")
            
            hours = input("Enter the number of hours worked: ")
            
HoursWorked = checkPositiveNumberValue(HoursWorked)
print("Employee: ", Employee, " worked", str(HoursWorked), "hours during the time period.")