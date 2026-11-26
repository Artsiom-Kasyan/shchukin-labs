import unittest

from booking import overlaps


class BookingTests(unittest.TestCase):
    def test_touching_boundaries(self):
        self.assertFalse(overlaps(540, 630, 630, 720))
        self.assertFalse(overlaps(630, 720, 540, 630))

    def test_containment(self):
        self.assertTrue(overlaps(540, 720, 600, 660))
        self.assertTrue(overlaps(600, 660, 540, 720))

    def test_identical(self):
        self.assertTrue(overlaps(0, 1440, 0, 1440))

    def test_partial_overlap(self):
        self.assertTrue(overlaps(540, 631, 630, 720))

    def test_gap(self):
        self.assertFalse(overlaps(540, 600, 630, 720))

    def test_invalid_interval(self):
        for pair in [(0, 0), (700, 650), (-1, 200), (1400, 1441)]:
            with self.subTest(pair=pair), self.assertRaises(ValueError):
                overlaps(540, 630, *pair)
