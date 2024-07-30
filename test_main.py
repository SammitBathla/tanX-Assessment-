import unittest
import pandas as pd
from main import dataFrame, monthlyRevenue, productRevenue, customerRevenue, top_10_Customers

class TestOrdersData(unittest.TestCase):

    def test_monthlyRevenue(self):
        self.assertGreater(len(monthlyRevenue), 0)

    def test_productRevenue(self):
        self.assertGreater(len(productRevenue), 0)

    def test_customerRevenue(self):
        self.assertGreater(len(customerRevenue), 0)

    def test_top_10Customers(self):
        self.assertEqual(len(top_10_Customers), 10)

if __name__ == '__main__':
    unittest.main()
