def get_name():
    name=input("Enter your name: ")
    return name

def get_age():
    age=input("Enter your age: ")
    return age

def get_address():
    address=input("Enter your address: ")
    return address

def display(name1, age2, address3):
    print(f"Hi, my name is {name1}. I am {age2} years old and I live in {address3}.")

name=get_name()
age=get_age()
address=get_address()
display(name, age, address)