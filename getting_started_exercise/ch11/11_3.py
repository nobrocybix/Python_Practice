import unittest

class Employee():

    def __init__(self, first_name, last_name, annual_salary):

        self.first_name = first_name
        self.last_name  = last_name
        self.annual_salary = annual_salary

    def give_raise(self, raise_salary = 5000):
        
        self.annual_salary += raise_salary

        return self.annual_salary
        
class Test_raise(unittest.TestCase):

    def setUp(self):
        
        self.first_name = "Jack"
        self.last_name = "Oneil"
        annual_salary = 10000
        self.my_salary = Employee(self.first_name, self.last_name, annual_salary)

    def test_give_default(self):
        
        self.assertEqual("Jack", self.my_salary.first_name)
        self.assertEqual("Oneil", self.my_salary.last_name)
        self.assertEqual(15000, self.my_salary.give_raise())

    def test_give_custom_raise(self):

        self.assertEqual(14000, self.my_salary.give_raise(4000))

unittest.main()