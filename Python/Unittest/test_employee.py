import unittest
from unittest.mock import patch
from employee import Employee


class TestEmployee(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')

    def setUp(self):
        print('setUp')
        self.emp_1 = Employee("Solomon", "Eniola", 50860)
        self.emp_2 = Employee("Dorcas", "Okunlola", 50800)

    def tearDown(self):
        print('tearDown\n')
        pass

    def test_email(self):
        print('test_email')
        self.assertEqual(self.emp_1.email, 'Solomon.Eniola@email.com')
        self.assertEqual(self.emp_2.email, 'Dorcas.Okunlola@email.com')


        self.emp_1.first = 'John'
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.email, "John.Eniola@email.com")
        self.assertEqual(self.emp_2.email, 'Jane.Okunlola@email.com')


    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp_1.fullname, 'Solomon Eniola')
        self.assertEqual(self.emp_2.fullname, 'Dorcas Okunlola')


        self.emp_1.first = 'John'
        self.emp_2.first = 'Jane'

        self.assertEqual(self.emp_1.fullname, 'John Eniola')
        self.assertEqual(self.emp_2.fullname, 'Jane Okunlola')

    def test_apply_raise(self):
        print('test_apply_raise')
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 50860)
        self.assertEqual(self.emp_2.pay, 50800)


    def test_monthly_schedule(self):
        with patch('employee.requests.get') as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = 'Success' 

            schedule = self.emp_1.monthly_schedule('May')
            mocked_get.assert_called_with('http://company.com/Eniola/May')
            self.assertEqual(schedule, 'Success')

            mocked_get.return_value.ok = False
            
            schedule = self.emp_2.monthly_schedule('January')
            mocked_get.assert_called_with('http://company.com/Okunlola/January')
            self.assertEqual(schedule, 'Bad Response!')
if __name__ == "__main__":
    unittest.main()
