import unittest
from fund import Fund

class TestFund(unittest.TestCase):
    """Tests for the class Fund."""

    def test_init(self):
        # Test default initialization
        fund = Fund()
        self.assertEqual(fund.value, 0)
        self.assertEqual(fund.min_value, 0)

        # Test custom initialization
        fund = Fund(value=50, min_value=25)
        self.assertEqual(fund.value, 50)
        self.assertEqual(fund.min_value, 25)

    
    def test_update(self):
        # Test updating with positive values
        fund = Fund(value=100)
        result = fund.update(50)
        self.assertEqual(result, 1)
        self.assertEqual(fund.value, 150)

        # Test updating with negative values
        fund = Fund(value=100)
        result = fund.update(-50)
        self.assertEqual(result, 1)
        self.assertEqual(fund.value, 50)

        # Test updating with value that would exceel min_value
        fund = Fund(value=50)
        result = fund.update(-60)
        self.assertEqual(result, -1)
        self.assertEqual(fund.value, 50)

    
    def test_get_value(self):
        # Test getting current value of fund
        fund = Fund(value=50)
        self.assertEqual(fund.get_value(), 50)

    def test_get_min_value(self):
        # Test getting minimum value of a fund
        fund = Fund(min_value=5)
        self.assertEqual(fund.get_min_value(), 5)

if __name__ == '__main__':
    unittest.main()
