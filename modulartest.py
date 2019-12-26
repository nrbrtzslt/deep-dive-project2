import unittest
from modulararithmetic import Mod


class TestMod(unittest.TestCase):
    def setUp(self):
        self.value = 2
        self.modulus = 3

    def tearDown(self):
        del self.value
        del self.modulus

    def create_mod(self):
        return Mod(self.value, self.modulus)

    def test_create_mod_ok(self):
        m = self.create_mod()
        self.assertEqual(self.value, m.value)
        self.assertEqual(self.modulus, m.modulus)

    def test_create_mod_residue_overdrawn(self):
        residue = 2
        self.value = 8
        m = self.create_mod()
        self.assertEqual(residue, m.value)

    def test_create_mod_with_float_value(self):
        self.value = 2.3
        with self.assertRaises(TypeError):
            self.create_mod()

    def test_create_mod_with_float_modulus(self):
        self.modulus = 2.3
        with self.assertRaises(TypeError):
            self.create_mod()

    def test_create_mod_with_negative_modulus(self):
        self.modulus = -5
        with self.assertRaises(ValueError):
            self.create_mod()

    def test_equal_with_integer_ok(self):
        compare_value = 2
        self.assertTrue(self.create_mod() == compare_value)

    def test_equal_with_integer_not_ok(self):
        compare_value = 3
        self.assertFalse(self.create_mod() == compare_value)

    def test_equal_with_not_integer(self):
        compare_value = 2.3
        self.assertEqual(False, self.create_mod() == compare_value)

    def test_equal_with_mod_ok(self):
        self.assertTrue(self.create_mod() == self.create_mod())

    def test_equal_with_mod_not_ok(self):
        self.assertFalse(self.create_mod() == Mod(7, 8))

    def test_int_with_mod(self):
        compare_value = 2
        self.assertEqual(int(self.create_mod()), compare_value)

    def test_repr(self):
        compare_value = 'Mod(value={}, modulus={})'.format(self.value, self.modulus)
        self.assertEqual(str(self.create_mod()), compare_value)

    def test_add_mod(self):
        add_value = Mod(5, 3)
        self.assertEqual(self.create_mod() + add_value, Mod(1, 3))

    def test_add_mod_with_different_modulus(self):
        add_value = Mod(5, 4)
        with self.assertRaises(TypeError):
            self.create_mod() + add_value

    def test_add_integer(self):
        add_value = 12
        compare_value = Mod(2, 3)
        self.assertEqual(self.create_mod() + add_value, compare_value)

    def test_add_float(self):
        add_value = 5.3
        with self.assertRaises(TypeError):
            self.create_mod() + add_value

    def test_neg_mod(self):
        compare_value = Mod(-2, 3)
        self.assertEqual(-self.create_mod(), compare_value)


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


run_tests(TestMod)
