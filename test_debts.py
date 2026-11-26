import unittest

from debts import DebtRegister


class DebtTests(unittest.TestCase):
    def setUp(self):
        self.register = DebtRegister()

    def test_add_is_idempotent(self):
        for _ in range(2):
            self.register.add("А", 1)
        self.assertEqual(self.register.count("А"), 1)

    def test_students_are_independent(self):
        for student in ["А", "Б"]:
            self.register.add(student, 2)
        self.register.close("А", 2)
        self.assertEqual(self.register.count("А"), 0)
        self.assertEqual(self.register.count("Б"), 1)

    def test_unknown_debt(self):
        with self.assertRaises(KeyError):
            self.register.close("А", 9)

    def test_invalid_input(self):
        for student, lab in [("", 1), ("А", 0)]:
            with self.assertRaises(ValueError):
                self.register.add(student, lab)
