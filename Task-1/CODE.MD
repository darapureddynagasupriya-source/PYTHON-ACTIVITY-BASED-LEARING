# Employee Payroll and Deduction Analysis Using Python

## 1. Problem Statement

Employee Payroll and Deduction Analysis: Calculate gross salary from basic pay, allowances, 
overtime, and incentives; apply progressive deductions and generate a formatted salary statement

## 2. Algorithm

1. Start the program.
2. Enter the employee name and employee ID.
3. Input basic pay, allowances, overtime hours, overtime rate, and incentives.
4. Calculate overtime pay.

\\[ \text{Overtime Pay} = \text{Overtime Hours} \times \text{Overtime Rate} \\]

5. Calculate gross salary by adding basic pay, allowances, overtime pay, and incentives.
6. Calculate Provident Fund (PF) deduction as 12% of basic pay.
7. Calculate progressive income tax using the following tax slabs:

| Salary Slab   | Tax Rate |
| ------------- | -------- |
| First ₹10,000 | 0%       |
| Next ₹10,000  | 5%       |
| Next ₹20,000  | 10%      |
| Above ₹40,000 | 15%      |

8. Calculate total deductions by adding PF and income tax.
9. Calculate net salary.
10. Display the formatted salary statement.
11. Stop the program.

Note: These tax slabs and the PF rate are illustrative assumptions for this programming example, not actual statutory payroll rates.

## 3. Flowchart (Mermaid)


flowchart TD
    A([START]) --> B[/Enter Employee Name and ID/]
    B --> C[/Input Basic Pay, Allowances/]
    C --> D[/Input Overtime Hours, Rate and Incentives/]
    D --> E[Calculate Overtime Pay]
    E --> F[Calculate Gross Salary]
    F --> G[Calculate PF Deduction]
    G --> H[Calculate Progressive Income Tax]
    H --> I[Calculate Total Deductions]
    I --> J[Calculate Net Salary]
    J --> K[/Display Salary Statement/]
    K --> L([STOP])



## 5. Sample Input

```
===== EMPLOYEE PAYROLL SYSTEM =====

Enter Employee Name: Rahul
Enter Employee ID: EMP101
Enter Basic Pay: 30000
Enter Allowances: 5000
Enter Overtime Hours: 10
Enter Overtime Rate per Hour: 200
Enter Incentives: 3000
```

## 6. Sample Output

```
========== SALARY STATEMENT ==========

Employee Name       : Rahul
Employee ID         : EMP101

--------------------------------------
Basic Pay           : Rs. 30000.0
Allowances          : Rs. 5000.0
Overtime Pay        : Rs. 2000.0
Incentives          : Rs. 3000.0

--------------------------------------
Gross Salary        : Rs. 40000.0

---------- DEDUCTIONS ----------------
Provident Fund      : Rs. 3600.0
Income Tax          : Rs. 2500.0
Total Deductions    : Rs. 6100.0

--------------------------------------
NET SALARY          : Rs. 33900.0
======================================
```

