import math

def apls_quant():
    apples=int(input("How many apples do you want?: "))
    return apples

def orngs_quant():
    oranges=int(input("How many oranges do you want?: "))
    return oranges

def apls_cost():
    apls_amount=apples*20
    return apls_amount

def orngs_cost():
    orngs_amount=oranges*25
    return orngs_amount

def total_cost():
    total=apls_amount+orngs_amount   
    return total

def display(totalcst):
    print(f"The total amount is {totalcst}")

