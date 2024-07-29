import unittest
import pandas as pd
from main import dataFrame, monthly_revenue, product_revenue, customer_revenue, top_10_Customers

class TestOrdersData(unittest.TestCase):

    def test_monthlyRevenue(self):
        self.assertGreater(len(monthly_revenue), 0)

    def test_productRevenue(self):
        self.assertGreater(len(product_revenue), 0)

    def test_customerRevenue(self):
        self.assertGreater(len(customer_revenue), 0)

    def test_top_10Customers(self):
        self.assertEqual(len(top_10_Customers), 5)

if __name__ == '__main__':
    unittest.main()
