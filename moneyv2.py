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