import unittest
from TODO_number_to_words import number_to_words

class TestNums(unittest.TestCase):
    
    # Adauga codul pentru unit tests aici

    def sample_unit_test(self):
        return None
    def test_zero(self):
        self.assertEqual(number_to_words(0), "zero")
    def test_one(self):
        self.assertEqual(number_to_words(1), "one")
    def test_two(self):
        self.assertEqual(number_to_words(2), "two")
    def test_three(self):
        self.assertEqual(number_to_words(3), "three")               
    def test_four(self):
        self.assertEqual(number_to_words(4), "four")
    def test_five(self):
        self.assertEqual(number_to_words(5), "five")
    def test_six(self):
        self.assertEqual(number_to_words(6), "six")
    def test_seven(self):
        self.assertEqual(number_to_words(7), "seven")
    def test_eight(self):
        self.assertEqual(number_to_words(8), "eight")
    def test_nine(self):
        self.assertEqual(number_to_words(9), "nine")
    
    # Test teens (10-19) - these are special cases
    def test_ten(self):
        self.assertEqual(number_to_words(10), "ten")
    
    def test_eleven(self):
        self.assertEqual(number_to_words(11), "eleven")
    
    def test_fifteen(self):
        self.assertEqual(number_to_words(15), "fifteen")
    
    def test_nineteen(self):
        self.assertEqual(number_to_words(19), "nineteen")
    
    # Test exact tens (20, 30, 40, etc.) - no ones digit
    def test_twenty(self):
        self.assertEqual(number_to_words(20), "twenty")
    
    def test_thirty(self):
        self.assertEqual(number_to_words(30), "thirty")
    
    def test_fifty(self):
        self.assertEqual(number_to_words(50), "fifty")
    
    def test_ninety(self):
        self.assertEqual(number_to_words(90), "ninety")
    
    # Test compound numbers (20-99 with ones digit)
    def test_twenty_one(self):
        self.assertEqual(number_to_words(21), "twenty one")
    
    def test_thirty_seven(self):
        self.assertEqual(number_to_words(37), "thirty seven")
    
    def test_forty_two(self):
        self.assertEqual(number_to_words(42), "forty two")
    
    def test_ninety_nine(self):
        self.assertEqual(number_to_words(99), "ninety nine")
    
