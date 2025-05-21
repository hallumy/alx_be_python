#!usr/bin/env python3

#User input for financial details
monthly_income = float(input('Enter your monthly income:'))
monthly_expenses = float(input('Enter your total monthly expenses:'))

#calculating monthly savings
monthly_savings = float(monthly_income) - float(monthly_expenses)

#calculating the annual savings
projected_savings = float(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print(f'Your monthly savings are ${monthly_savings:,.2f}.')
print(f'Projected savings after one year, with interest, is: ${projected_savings:,.2f}.')
