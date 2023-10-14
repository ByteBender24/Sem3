'''
The purpose of this exercise is to analyse, design, and implement the concept of abstract base class and 
exceptions.Apply the object-oriented knowledge to model a Loan package. The Loan class should be the parent 
ABC. The education loan, home loan, and personal loans are inherited from the Loan class and should have 
abstract methods. The loan interest should vary based on the type of account (Savings or Current). The 
interest amount vested on the loan amount will vary according to the location (rural or urban) and the 
sanctioned loan amount. Demonstrate the use of ABC, inheritance, and raising and handling of exceptions 
for appropriate conditions

Author : Harishraj S
Date : 11-10-2023
'''

from abc import ABC, abstractmethod


class Loan(ABC):
    def __init__(self, loan_amount, location, account_type, credit_score, secured=True, collateral=None):
        """
        The Loan class is an abstract base class (ABC) that defines the common structure for all types of loans.
        It has an abstract method calculate_interest, which must be implemented by its subclasses.

        Initialize a loan with loan amount, location, account type, credit score, and a flag indicating whether it's secured.

        :param loan_amount: The amount of the loan.
        :param location: The location of the borrower (e.g., "Urban", "Rural").
        :param account_type: The type of the borrower's account (e.g., "Savings", "Current").
        :param credit_score: The credit score of the borrower.
        :param secured: A flag indicating whether the loan is secured (default is True).
        """
        self.loan_amount = loan_amount
        self.location = location
        self.account_type = account_type
        self.secured = secured
        self.credit_score = credit_score
        self.collateral = collateral

    @abstractmethod
    def calculate_interest(self):
        """
        Abstract method to calculate the interest for a loan.
        This method should be implemented by subclasses.

        :return: The calculated interest for the loan.
        """
        pass


class InsufficientCreditsError(Exception):
    def __init__(self, message="Insufficient credit score for the loan"):
        '''
        Custom exception for cases of insufficient credit scores
        '''

        self.message = message
        super().__init__(self.message)


class NoCollateralError(Exception):
    def __init__(self, message="Collateral required for the loan"):
        '''
        Custom exception for cases where collateral is required but not provided
        '''

        self.message = message
        super().__init__(self.message)


class EducationLoan(Loan):
    def calculate_interest(self):
        if self.secured:
            credit_score_requirement = 650
            collateral_required = True
        else:
            credit_score_requirement = 600
            collateral_required = False

        if self.credit_score < credit_score_requirement:
            raise InsufficientCreditsError()

        if collateral_required and not self.collateral:
            raise NoCollateralError()

        if self.account_type == "Savings":
            interest_rate = 0.08
        else:
            interest_rate = 0.1

        if self.location == "Rural":
            interest_rate -= 0.02

        return self.loan_amount * interest_rate


class HomeLoan(Loan):
    def calculate_interest(self):
        if self.secured:
            credit_score_requirement = 700
            collateral_required = True
        else:
            credit_score_requirement = 650
            collateral_required = False

        if self.credit_score < credit_score_requirement:
            raise InsufficientCreditsError()

        if collateral_required and not self.collateral:
            raise NoCollateralError()

        if self.account_type == "Savings":
            interest_rate = 0.07
        else:
            interest_rate = 0.09

        if self.location == "Rural":
            interest_rate -= 0.03

        return self.loan_amount * interest_rate


class PersonalLoan(Loan):
    def calculate_interest(self):
        if self.secured:
            credit_score_requirement = 680
            collateral_required = True
        else:
            credit_score_requirement = 620
            collateral_required = False

        if self.credit_score < credit_score_requirement:
            raise InsufficientCreditsError()

        if collateral_required and not self.collateral:
            raise NoCollateralError()

        if self.account_type == "Savings":
            interest_rate = 0.12
        else:
            interest_rate = 0.15

        if self.location == "Rural":
            interest_rate -= 0.04

        return self.loan_amount * interest_rate


def main():
    try:
        # Example credit scores:
        # - Secured Education Loan requires a credit score of 650 or higher
        # - Unsecured Home Loan requires a credit score of 650 or higher
        # - Secured Personal Loan requires a credit score of 620 or higher
        secured_education_loan = EducationLoan(
            10000, "Urban", "Savings", 700, True, 15000)
        print(
            f"Secured Education Loan Interest: ${secured_education_loan.calculate_interest()}")

        unsecured_home_loan = HomeLoan(100000, "Rural", "Current", 680, False)
        print(
            f"Unsecured Home Loan Interest: ${unsecured_home_loan.calculate_interest()}")

        secured_personal_loan = PersonalLoan(
            5000, "Urban", "Savings", 720, True, 10000)
        print(
            f"Secured Personal Loan Interest: ${secured_personal_loan.calculate_interest()}")

    except InsufficientCreditsError as e:
        print(f"Error: {e}")

    except NoCollateralError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
