income = int(input("Enter your monthly income:"))
total_monthly_expenses = int(input("Enter yout  total monthly expenses:"))
monthly_savings = income - total_monthly_expenses
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)
print(monthly_savings)
print(projected_savings)
