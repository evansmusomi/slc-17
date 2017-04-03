import unittest
from loan_calculator import calculate_repayable_loan_amount


class LoanCalculator(unittest.TestCase):
    def test_it_works(self):
        self.assertEquals(calculate_repayable_loan_amount(100000,12,12), 112000)
