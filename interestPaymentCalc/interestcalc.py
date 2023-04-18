# collect the necessary inputs: Pricipal, apr , years
# calculate the monthly payment
# show to the user

def main():
    print("This is a monthly payment loan calc ")
    print("")

    principal = float(input("Input the loan amount: "))
    apr = float(input("Input the annual interest rate:"))
    years = int(input("Input amount of years: "))

# This line calculates the monthly interest rate by dividing the APR (annual percentage rate) by 1200,
# which is the number of months in a year multiplied by 100 for converting APR to a decimal format.
    monthly_interest_rate = apr / 1200

# This line calculates the total number of months for the loan by multiplying the number of years by 12 months per year.
    amount_of_months = years * 12

# This line calculates the monthly payment using the formula for a fixed-rate loan,
# where P is the principal amount, r is the monthly interest rate, and n is the total number of months:
# monthly_payment = P * r / (1 - (1 + r) ** (-n))
# The formula calculates the monthly payment needed to pay off the loan over the given number of months.
# The "%.2f" syntax is used to format the output as a floating-point number with 2 decimal places.
    monthly_payment = principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-amount_of_months))

# This line prints the calculated monthly payment using string formatting to include the value of the variable.
    print("The monthly payment for this loan is: %.2f" % monthly_payment)

main()