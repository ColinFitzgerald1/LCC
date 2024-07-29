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