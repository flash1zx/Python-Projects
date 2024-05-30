expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ("January", "February", "March", "April", "May")
e = input("Enter expense amount: ")
e = int(e)

for i in range(len(expense_list)):
    if e == expense_list[i]:
        month = i
        break
if month != -1:
    print(f"You spent {e} in {month_list[month]}")
else:
    print(f"You did not spend {e} in any month")
