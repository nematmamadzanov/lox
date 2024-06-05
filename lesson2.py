user = {
    "Ali": "manger",
    "oroz": "admin"
}



def role(username):
    if username in user:
        return user[username]
    else:
        return"user not found"
    

print(user["oroz"])
def role(username):
    if username in user:
        return user[username]
    else:
        return"user not found"

def add_users(ali,admin):
    user[ali]=admin

add_users("ali","admin")
print(user)


def add_users(oroz,manger):
    user[oroz]=manger

add_users("oroz","manger")
print(user)

def del_ali(ali):
    del user[ali]
    print(user)



#     def calculate_mortgage_payment(principal, annual_interest_rate, years, initial_payment):
#     monthly_interest_rate = annual_interest_rate / 12 / 100
#     months = years * 12
#     adjusted_principal = principal - initial_payment
#     monthly_payment = adjusted_principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -months)
#     return monthly_payment, monthly_payment - (adjusted_principal * monthly_interest_rate), (principal * monthly_interest_rate), principal


# principal = 6000000  # Основная сумма ипотеки
# annual_interest_rate = 9.4  # Годовая процентная ставка
# years = 20  # Срок кредита в год
# initial_payment = 1000000 # Величина первоначального взноса в рублях

# monthly_payment, principal_portion, interest_portion, total_mortgage = calculate_mortgage_payment(principal, annual_interest_rate, years, initial_payment)
# print("Ежемесячный платеж:", round(monthly_payment, 2))
# print("Погашение основного долга:", round(principal_portion, 2))
# print("Процент выплаты:", round(interest_portion, 2))
# print("Общая сумма ипотеки:", principal)
# print("Взнос:", initial_payment)





# 2
# import datetime

# def calculate_mortgage_payment_schedule(principal, annual_interest_rate, years, initial_payment):
#     monthly_interest_rate = annual_interest_rate / 12 / 100
#     months = years * 12
#     adjusted_principal = principal - initial_payment
#     monthly_payment = adjusted_principal * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -months)
    
   
#     schedule = []
#     current_principal = adjusted_principal
#     today = datetime.date.today()
    
#     for month in range(1, months + 1):
#         interest_payment = current_principal * monthly_interest_rate
#         principal_payment = monthly_payment - interest_payment
#         remaining_principal = current_principal - principal_payment
        
      
#         payment_info = {
#             "Month": month,
#             "Date": today + datetime.timedelta(days=30 * month),
#             "Total Payment": round(monthly_payment, 2),
#             "Principal Payment": round(principal_payment, 2),
#             "Interest Payment": round(interest_payment, 2),
#             "Remaining Principal": round(remaining_principal, 2)
#         }
#         schedule.append(payment_info)
        
       
#         current_principal = remaining_principal
    
#     return schedule


# principal = 6000000  # Основная сумма ипотеки
# annual_interest_rate = 9.4  # Годовая процентная ставка
# years = 20  # Срок кредита в годах
# initial_payment = 1000000  # Величина первоначального взноса в рублях


# payment_schedule = calculate_mortgage_payment_schedule(principal, annual_interest_rate, years, initial_payment)


# for payment_info in payment_schedule[:5]:  
#     print(payment_info)


# print(payment_schedule[-1])




