# Sibtain Ahmed
# Date: 09-27-2025
# Lab 5


def studentLoanAmortization(principal, yearlyInterestRate, numberOfYears):
    # period = 0
    # totalPaymentDue = 0.0
    # computedInterestDue = 0.0
    # principalDue = 0.0
    principalBalance = principal
    monthlyInterestRate = yearlyInterestRate / 12
    # totalPaymentDue = principal * (monthlyInterestRate) / (1 - (1 + (monthlyInterestRate)) ** (-numberOfYears * 12))
    totalPaymentDue = (principal * (monthlyInterestRate * (1+monthlyInterestRate)**(numberOfYears*12))) / (((1+monthlyInterestRate)**(numberOfYears*12))-1)
    print(f"{'Period':<6} {'Total Payment Due':>20} {'Computed Interest':>20} {'Principal Due':>16} {'Principal Balance':>24}")
    for period in range(numberOfYears * 12):
        computedInterestDue = (monthlyInterestRate) * principalBalance
        principalDue = totalPaymentDue - computedInterestDue
        principalBalance -= principalDue
        if principalBalance < 0:
            principalBalance = 0
        print(f"{period+1:<9d} {totalPaymentDue:<20.2f} {computedInterestDue:<20.2f} {principalDue:<20.2f} {principalBalance:<20.2f}")



def main():
    principal = float(input("Enter the principal amount of the loan: "))
    yearlyInterestRate = float(input("Enter the yearly interest rate (as a percentage): "))
    numberOfYears = int(input("Enter the number of years to pay off the loan: "))

    studentLoanAmortization(principal, yearlyInterestRate, numberOfYears)  
    print("Amortization schedule has been generated.")

if __name__ == "__main__":
    main()