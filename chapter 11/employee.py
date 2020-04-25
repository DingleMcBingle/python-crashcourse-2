class Employee():

    def __init__(self, first_name, last_name, salary):
        self.first = first_name.title()
        self.last = last_name.title()
        self.salary = salary

    def give_raise(self, amount=5000):
        self.salary += amount