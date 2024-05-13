import unittest
from student import Student
from datetime import timedelta

class TestStudent(unittest.TestCase):

    @classmethod #will make it a class method instead of an instance
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')
        self.student = Student('John', 'Doe')

    def tearDown(self):
        print('tearDown')

    #function tests the full name of student
    def test_full_name(self):
        print('test_full_name')
        self.assertEqual(self.student.full_name, 'John Doe') #tests if the above full name matches


    def test_email(self):
        print('test_email')

        self.assertEqual(self.student.email, 'john.doe@email.com')


    def test_alert_santa(self):
        print('test_alert_santa')
        self.student.test_alert_santa()

        self.assertTrue(self.student.naughty_list)

    def test_apply_extension(self):
        old_end_date = self.student.end_date
        self.student.apply_extension(5)

        self.assertEqual(self.student.end_date, old_end_date + timedelta(days=5))

if __name__ == '__main__':
    unittest.main()