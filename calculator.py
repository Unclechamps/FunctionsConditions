# Calculator builder
def math(first_number,second_number, operand):
    if operand == "+":
        print(first_number + second_number)
    elif operand == "-":
        print(first_number - second_number)
    elif operand == "*":
        print(first_number * second_number)
    elif operand == "/":
        print(first_number / second_number)
    else:
        print("You need an operand!")
