#shop.py


def check_money(total_cost, customer_money):
    if total_cost < customer_money:
        return True
    elif customer_money < total_cost:
        return False


#This should print False
can_pay = check_money(107, 49)
print(can_pay)

#This should print True
can_pay = check_money(6, 88)
print(can_pay)
