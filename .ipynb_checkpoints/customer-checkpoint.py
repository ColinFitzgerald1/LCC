# creates the Person class
class Person:
    # create the __init__ function with three parameters
    def __init__(self, name, adress, number):
        # name attribute
        self.__name = name
        # address attribute
        self.__adress = adress
        # number attribute
        self.__number = number
    # name setter method
    def set_name(self, name):
        # defining the name variable
        self.__name = name
    # address setter method
    def set_adress(self, adress):
        # defining the address variable
        self.__adress = adress
    # number setter method
    def set_number(self, number):
        # defining the number variable
        self.__number = number
    # name getter method
    def get_name(self):
        # returns the name
        return self.__name
    # address getter method
    def get_adress(self):
        # returns the address
        return self.__adress
    # number getter method
    def get_number(self):
        # returns the number
        return self.__number
# creates the Customer subclass
class Customer(Person):
    # creates __init__ function with many attributes as parametes
    def __init__(self, name, adress, number, customer_number, mailing_list):
        # __init__ from the superclass
        super().__init__(name, adress, number)
        # customer's number attribute
        self.__customer_number = customer_number
        # customer's mailing list attribute
        self.__mailing_list = mailing_list
    # customer number setter method
    def set_customer_number(self, customer_number):
        # defining the customer_number variable
        self.__customer_number = customer_number
    # mailing list setter method
    def set_mailing_list(self, mailing_list):
        # defining the mailing_list variable
        self.__mailing_list = mailing_list
    # customer number getter method
    def get_customer_number(self):
        # returns the customer's number
        return self.__customer_number
    # mailing list getter method
    def get_mailing_list(self):
        # returns the mailing_list variable
        return self.__mailing_list