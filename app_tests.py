import unittest
import app

class AppTests(unittest.TestCase):

    def test_findDay(self):
        self.assertEqual(app.findDay('12 12 2022'), 'Monday')

if __name__ == '__main__':
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()