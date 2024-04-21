def add(x, y):
    print("the added number is ", x + y)


def subtract(x, y):
    print("the subtracted number is", x - y)


def multiplication(x, y):
    print("the multiplied number is", x * y)


def division(x, y):
    print("the divided number is ", x / y)


while True:
    user_choice = input("please  1 to add 2 to subtract 3 for division and 4 for multiplication")
    if user_choice in ('1', '2', '3', '4'):
        try:
            n1 = float(input("enter the first element"))
            n2 = float(input("enter the second element"))
        except ValueError:
            print("Enter a valid number")
            continue
        if user_choice == '1':
            add(n1, n2)
        elif user_choice == '2':
            subtract(n1, n2)
        elif user_choice == '3':
            division(n1, n2)
        elif user_choice == '4':
            multiplication(n1, n2)
    contd = input("do you want to continue? press y")
    if contd.lower() != "y":
        break
else:
    print("invalid input")
