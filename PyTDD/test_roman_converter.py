import unittest
from roman_converter import roman_converter

class TestInvalidInput(unittest.TestCase):
    # ======== Step 1 ======== no input, return None
    def test_no_input(self):
        self.assertEqual(roman_converter(None), None)

    def test_num_str(self):
        self.assertEqual(roman_converter("a"),None)

    def test_num_vir(self):
        self.assertEqual(roman_converter(123.4), None)
                          
    def test_range_min(self):
        self.assertEqual(roman_converter(0), None)

    def test_range_max(self):
        self.assertEqual(roman_converter(4000), None)

class TestOnes(unittest.TestCase):
    def test_base_1(self):
        self.assertEqual(roman_converter(1), "I")
    def test_two(self):
        self.assertEqual(roman_converter(2), "II")

class TestFives(unittest.TestCase):
    def test_base_5(self):
        self.assertEqual(roman_converter(5), "V")

    def test_six(self):
        self.assertEqual(roman_converter(6), "VI")

class TestTens(unittest.TestCase):
    def test_base_10(self):
        self.assertEqual(roman_converter(10), "X")

    def test_25(self):
        self.assertEqual(roman_converter(25), "XXV")

    def test_49(self):
        self.assertEqual(roman_converter(49), "XXXXVIIII")

class TestFifties(unittest.TestCase):
    def test_base_50(self):
        self.assertEqual(roman_converter(50), "L")

    def test_99(self):
        self.assertEqual(roman_converter(99), "LXXXXVIIII")
class TestHundreds(unittest.TestCase):
    def test_base_100(self):
        self.assertEqual(roman_converter(100), "C")

    def test_199(self):
        self.assertEqual(roman_converter(199), "CLXXXXVIIII")

class TestFHundreds(unittest.TestCase):
    def test_base_500(self):
        self.assertEqual(roman_converter(500), "D")

    def test_999(self):
        self.assertEqual(roman_converter(999), "DCCCCLXXXXVIIII")

class TestThousands(unittest.TestCase):
    def test_base_1000(self):
        self.assertEqual(roman_converter(1000), "M")

    def test_2500(self):
        self.assertEqual(roman_converter(2500), "MMD")
    def test_3999(self):
        self.assertEqual(roman_converter(3999), "MMMDCCCCLXXXXVIIII")