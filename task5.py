company_income = int(input("Введите прибыль компании - "))
company_loss = int(input("Введите убыль компании - "))
if company_income > company_loss:
    print("Компания работает с прибылью")
    print(f"{int((company_income/company_loss) * 100)}% - рентабельность") # Формула рентабельности: (доход/расход)*100%
    employee = int(input("Введите кол-во сотрудников - "))
    print(f"{company_income/employee} - прибыль на одного сотрудника")
else:
    print("Компания работает в убыток")