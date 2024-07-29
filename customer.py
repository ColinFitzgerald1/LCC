class Person:
    def __init__(self, name, adress, number):
        self.__name = name
        self.__adress = adress
        self.__number = number

    def set_name(self, name):
        self.__name = name

    def set_adress(self, adress):
        self.__adress = adress

    def set_number(self, number):
        self.__number = number

    def get_name(self):
        return self.__name

    def get_adress(self):
        return self.__adress

    def get_number(self):
        return self.__number
        
class Customer(Person):
    def __init__(self, name, adress, number, customer_number, mailing_list):
        super().__init__(name, adress, number)
        self.__customer_number = customer_number
        self.__mailing_list = mailing_list

    def set_customer_number(self, customer_number):
        self.__customer_number = customer_number

    def set_mailing_list(self, mailing_list):
        self.__mailing_list = mailing_list

    def get_customer_number(self):
        return self.__customer_number

    def get_mailing_list(self):
        return self.__mailing_list