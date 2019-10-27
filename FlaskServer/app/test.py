import unittest

class MyTest(unittest.TestCase):
    def test(self):
        self.assertEqual(3, 3)

if __name__ == '__main__':
    import xmlrunner
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output='.'))

