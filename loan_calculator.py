def calculate_repayable_loan_amount(loan_amount, interest_rate, loan_period):
    """Calculate the repayable loan amount

    Args:
        loan_amount: The amount of money loaned
        interest_rate: The interest rate per year
        loan_period: The loan period in months

    Returns: A number, the amount of money to be repaid
    """
    repayable_amount = loan_amount + (loan_amount * interest_rate/100 * loan_period/12)
    return repayable_amount

print(calculate_repayable_loan_amount(100000, 12, 12))
