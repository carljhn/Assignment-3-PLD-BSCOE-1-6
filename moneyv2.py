import math

def _money():
    money=int(input("You have an amount of: "))
    return money

def aplprc():
    apl_price=int(input("An apple costs: "))
    return apl_price

def maxapls():
    max_apls=int(money/apl_price)
    return max_apls

def getTotal():
    total=apl_price * max_apls
    return total

def getChange():
    change=money-total
    return change

def display(max_apls, change):
    print(f"You can buy {max_apls} apples and your change is {change} pesos.") 

money=_money()
apl_price=aplprc()
max_apls=maxapls()
total=getTotal()
change=getChange()
display(max_apls, change)