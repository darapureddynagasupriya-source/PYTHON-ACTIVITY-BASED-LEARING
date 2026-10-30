
# Employee Payroll and Deduction Analysis

# Function to calculate progressive income tax
def calculate_tax(salary):

    tax = 0

    if salary > 40000:
        tax += (salary - 40000) * 0.15
        salary = 40000

    if salary > 20000:
        tax += (salary - 20000) * 0.10
        salary = 20000

    if salary > 10000:
        tax += (salary - 10000) * 0.05

    return tax


# Input employee details
print("===== EMPLOYEE PAYROLL SYSTEM =====")

name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")

basic = float(input("Enter Basic Pay: "))
allowances = float(input("Enter Allowances: "))

ot_hours = float(input("Enter Overtime Hours: "))
ot_rate = float(input("Enter Overtime Rate per Hour: "))

incentives = float(input("Enter Incentives: "))

# Calculate overtime pay
overtime_pay = ot_hours * ot_rate

# Calculate gross salary
gross_salary = basic + allowances + overtime_pay + incentives

# Calculate PF deduction (12% of basic pay)
pf = basic * 0.12

# Calculate progressive income tax
income_tax = calculate_tax(gross_salary)

# Calculate total deductions
total_deductions = pf + income_tax

# Calculate net salary
net_salary = gross_salary - total_deductions

# Display salary statement
print("\n========== SALARY STATEMENT ==========")

print("Employee Name       :", name)
print("Employee ID         :", emp_id)

print("--------------------------------------")
print("Basic Pay           : Rs.", basic)
print("Allowances          : Rs.", allowances)
print("Overtime Pay        : Rs.", overtime_pay)
print("Incentives          : Rs.", incentives)

print("--------------------------------------")
print("Gross Salary        : Rs.", gross_salary)

print("\n---------- DEDUCTIONS ----------------")
print("Provident Fund      : Rs.", pf)
print("Income Tax          : Rs.", income_tax)
print("Total Deductions    : Rs.", total_deductions)

print("--------------------------------------")
print("NET SALARY          : Rs.", net_salary)
print("======================================")

