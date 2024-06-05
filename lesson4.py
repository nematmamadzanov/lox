# import datetime

# def calculate_mortgage_payment_schedule(principal, annual_interest_rate, years, initial_payment):
#     monthly_interest_rate = annual_interest_rate / 12 / 100
#     months = years * 12
#     adjusted_principal = principal - initial_payment
#     monthly_payment = adjusted_principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -months)
    
#     schedule = []
#     current_principal = adjusted_principal
#     today = datetime.date.today()
    
#     for year in range(1, years + 1):
#         total_payment_year = 0
#         total_principal_payment_year = 0
#         total_interest_payment_year = 0
        
#         for month in range(1, 13):
#             interest_payment = current_principal * monthly_interest_rate
#             principal_payment = monthly_payment - interest_payment
#             remaining_principal = current_principal - principal_payment
            
#             total_payment_year += monthly_payment
#             total_principal_payment_year += principal_payment
#             total_interest_payment_year += interest_payment
            
#             current_principal = remaining_principal
        
#         schedule.append({
#             "Year": year,
#             "Date": today + datetime.timedelta(days=365 * year),
#             "Total Payment": round(total_payment_year, 2),
#             "Principal Payment": round(total_principal_payment_year, 2),
#             "Interest Payment": round(total_interest_payment_year, 2),
#             "Remaining Principal": round(current_principal, 2)
#         })
    
#     return schedule

# principal = 6000000  # Сумма ипотеки
# annual_interest_rate = 9.4  # Годовая процентная ставка
# years = 20  # Срок кредита в годах
# initial_payment = 1000000  # Первоначальный взнос

# payment_schedule = calculate_mortgage_payment_schedule(principal, annual_interest_rate, years, initial_payment)

# # Вывод первых 5 лет и последнего платежа
# for payment_info in payment_schedule[:5]:
#     print(payment_info)
# print(payment_schedule[-1])  # Печать последнего платежа


# # Вывод первых 5 месяцев и последнего платежа
# for payment_info in payment_schedule[:5]:  # Печать только первых 5 месяцев чтобы был кротким и не доходил до 240 тогда ноутбуку будет кирдык
#     print(payment_info)
# print(payment_schedule[-1])  # Печать последнего платежа


import datetime

def calculate_mortgage_payment_schedule(principal, annual_interest_rate, years, initial_payment):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    months = years * 12
    adjusted_principal = principal - initial_payment
    monthly_payment = adjusted_principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -months)
    
    schedule = []
    current_principal = adjusted_principal
    today = datetime.date.today()
    
    for month in range(1, months + 1):
        interest_payment = current_principal * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_principal = current_principal - principal_payment
        
        schedule.append({
            "Month": month,
            "Date": today + datetime.timedelta(days=30 * month),
            "Total Payment": round(monthly_payment, 2),
            "Principal Payment": round(principal_payment, 2),
            "Interest Payment": round(interest_payment, 2),
            "Remaining Principal": round(remaining_principal, 2)
        })
        
        current_principal = remaining_principal
    
    return schedule

principal = 6000000  # Сумма ипотеки
annual_interest_rate = 9.4  # Годовая процентная ставка
years = 20  # Срок кредита в годах
initial_payment = 1000000  # Первоначальный взнос

payment_schedule = calculate_mortgage_payment_schedule(principal, annual_interest_rate, years, initial_payment)

# Вывод первых 5 месяцев и последнего платежа
print("First 5 months and last month:")
for payment_info in payment_schedule[:5]:
    print(payment_info)
print(payment_schedule[-1])  # Печать последнего месячного платежа

# Вывод всех месяцев
print("\nMonthly payment schedule for the entire term:")
for payment_info in payment_schedule:
    print(payment_info)