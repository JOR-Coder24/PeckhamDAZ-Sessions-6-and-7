
usernumber=int(input("Enter number"))

def odd_number_check(number):
    remainder=number % 2
    if remainder == 1:
        print("number is odd")
    else:
        print("number is even")

odd_number_check(usernumber)