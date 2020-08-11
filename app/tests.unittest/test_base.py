import unittest

class BaseTests(unittest.TestCase):
    def test_should_pass(self):
        pass

    def test_check_if_true_is_true(self):
        assert True == True

    def inc(self, x):
        return x + 1

    def test_check_if_inc_works(self):
        self.assertEqual(self.inc(3), 4)


if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(BaseTests)
    unittest.TextTestRunner(verbosity=2).run(suite)