import unittest
from main import Calculator

def setUpModule():
    print('set up module')

def tearDownModule():
    print('tear down module')

class TestCalculator(unittest.TestCase):

    # Create an instance of the calculator that can be used in all tests
    @classmethod
    def setUpClass(self):
        print('Set up class')
        self.c = Calculator()

    @classmethod
    def tearDownClass(self):
        print('Tear down class')

    # Write test methods for subtract, multiply, and divide
    def test_add(self):
        self.c.add_to_expression("1")
        self.c.add_to_expression("2")
        self.c.append_operator("+")
        self.c.add_to_expression("2")
        self.c.evaluate()

        self.assertEqual(self.c.current_expression, "14", msg=None)

        self.c.clear()

    def test_multiply(self):
        self.c.add_to_expression("1")
        self.c.add_to_expression("0")
        self.c.append_operator("*")
        self.c.add_to_expression("5")
        self.c.evaluate()

        self.assertEqual(self.c.current_expression, "50", msg=None) 

        self.c.clear()

    def test_divide(self):
        self.c.add_to_expression("1")
        self.c.add_to_expression("0")
        self.c.append_operator("/")
        self.c.add_to_expression("5")
        self.c.evaluate()

        self.assertEqual(self.c.current_expression, "2", msg=None) 

        self.c.clear()

    def test_square(self):
        self.c.add_to_expression("2")
        self.c.square()

        self.assertEqual(self.c.current_expression, "4", msg=None)

        self.c.backspace()

    def test_squareroot(self):
        self.c.add_to_expression("4")
        self.c.sqrt()

        self.assertEqual(self.c.current_expression, "2.0", msg=None)

        self.c.backspace()
        self.c.backspace()
        self.c.backspace()

    def test_subtract(self):
        self.c.add_to_expression("5")
        self.c.add_to_expression("0")
        self.c.append_operator("-")
        self.c.add_to_expression("10")
        self.c.evaluate()

        self.assertEqual(self.c.current_expression, "40", msg=None)

        self.c.clear()

    def test_decimal(self):
        self.c.add_to_expression("1")
        self.c.add_to_expression(".")
        self.c.add_to_expression("5")
        self.c.append_operator("*")
        self.c.add_to_expression("2")
        self.c.evaluate()

        self.assertEqual(self.c.current_expression, "3", msg=None)

        self.c.clear()



if __name__ == '__main__':
    unittest.main()