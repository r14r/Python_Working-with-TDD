import unittest

class BaseTests(unittest.TestCase):
    def inc(self, x):
        return x + 1

    def test_should_raise_error(self):
        raise ValueError

    def test_check_if_inc_works(self):
        self.assertEqual(self.inc(3), 5)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(BaseTests)
    unittest.TextTestRunner(verbosity=2).run(suite)
