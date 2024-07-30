# creates Employee class
class Employee:
    # creates __init__ function
    def __init__(self, name, number):
        # creates the name attribute
        self.__name = name
        # creates the number attribute
        self.__number = number
    # name setter method
    def set_name(self, name):
        # assigning the name variable
        self.__name = name
    # number setter method
    def set_number(self, number):
        # assigning the number variable
        self.__number = number
    # name getter method
    def get_name(self):
        # returning the name
        return self.__name
    # number getter method
    def get_number(self):
        # returning the number
        return self.__number
# creates the ProductionWorker subclass
class ProductionWorker(Employee):
    # creates the __init__ function
    def __init__(self, name, number, shift_number, hourly):
        # __init__ from the superclass
        super().__init__(name, number)
        # creates the shift_number attribute
        self.__shift_number = shift_number
        # creates the hourly attribute
        self.__hourly = hourly
    # shift number setter method
    def set_shift_number(self, shift_number):
        # assigning the shift_number variable
        self.__shift_number = shift_number
    # hourly wage setter method
    def set_hourly(self, hourly):
        # assigning the hourly variable
        self.__hourly = hourly
    # shift number getter method
    def get_shift_number(self):
        # returns the shift number
        return self.__shift_number
    # hourly wage getter method
    def get_hourly(self):
        # returns the hourly wage
        return self.__hourly