expense_report =[]

expenses = open('expense_report.txt', 'r')
for expense in expenses:
    if expense != '':
        expense = expense.strip('\n')
        expense = int(expense)
        expense_report.append(expense)

sum = False
while sum == False:
    for expense in expense_report:
        for check_expense in expense_report:
            if expense + check_expense == 2020:
                first_expense = expense
                second_expense = check_expense
                sum = True

answer = first_expense * second_expense
print(answer)

sum = False
while sum == False:
    for expense in expense_report:
        for check_expense in expense_report:
            for second_check_expense in expense_report:
                if expense + check_expense + second_check_expense == 2020:
                    first_expense = expense
                    second_expense = check_expense
                    third_expense = second_check_expense
                    sum = True

answer = first_expense * second_expense * third_expense
print(answer)

expenses.close()