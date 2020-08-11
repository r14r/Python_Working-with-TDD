import unittest

class DefaultBaseTests(unittest.TestCase):
    teststate = ""
    debuglevel=0

    def setUp(self):
        if self.debuglevel > 0:
            print("TST/DefaultBaseTests: setup")
        pass

    def tearDown(self):
        if self.debuglevel > 0:
            print("TST/DefaultBaseTests: tearDown")
        
        pass
        
class BaseTests(DefaultBaseTests):
    teststate = ""
    debuglevel=0

    @classmethod
    def setUpClass(self):
        if self.debuglevel > 0:
            print("TST/BaseTests: setUpClass")

    @classmethod
    def tearDownClass(self):
        if self.debuglevel > 0:
            print("TST/BaseTests: tearDownClass")

    def setUp(self):
        if self.debuglevel > 0:
            print("TST/BaseTests: setup")

    def tearDown(self):
        if self.debuglevel > 0:
            print("TST/BaseTests: tearDown")

    def test_should_pass(self):
        pass

    def test_check_if_true_is_true(self):
        assert True == True

    def inc(self, x):
        return x + 1

    def test_check_if_inc_works(self):
        self.assertEqual(self.inc(3), 4)


    #
    def test_assertEqual(self):
        self.assertEqual(1, 1, "assertEqual(1, 1)")


    def test_assertNotEqual(self):
        self.assertNotEqual(1, 2, "assertNotEqual(1, 2)")	 

    def test_assertTrue(self):
        self.assertTrue(True, "assertTrue(True)")

    def test_assertFalse(self):
        self.assertFalse(False, "test_assertFalse(True)")

    def test_assertIs(self):
        a=12
        b=12

        self.assertIs(a, b, "test_assertIs({}, {})".format(a,b))

    def test_assertIsNot(self):
        a=12
        b=13

        self.assertIsNot(a, b, "test_assertIsNot({}, {})".format(a,b))

    def test_assertIsNone(self):
        a=None

        self.assertIsNone(a, "assertIsNone(({})".format(a))

    def test_assertIsNotNone(self):
        a=10

        self.assertIsNotNone(a, "assertIsNotNone(({})".format(a))

    """
    def test_assertIn(self):
        self.assertTrue(True, "assertTrue(True)")
        self.(a, b)	a in b	2.7
    def test_assertNotIn((self):
        self.assertTrue(True, "assertTrue(True)")
        self.a, b)	a not in b	2.7
    def test_assertIsInstance(self):
        self.assertTrue(True, "assertTrue(True)")
        self.(a, b)	isinstance(a, b)	2.7
    def test_assertNotIsInstance(self):
        self.assertTrue(True, "assertTrue(True)")
        self.(a, b)
    """

if __name__ == '__main__':
    #unittest.main()

    suite = unittest.TestLoader().loadTestsFromTestCase(BaseTests)
    unittest.TextTestRunner(verbosity=4).run(suite)