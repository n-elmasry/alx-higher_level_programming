#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    arguments = sys.argv[1:]

    if len(arguments) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operators = ("+", "-", "*", "/")

    if arguments[1] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a, operator, b = int(arguments[0]), arguments[1], int(arguments[2])

    if operator == "+":
        result = add(a, b)
    elif operator == "-":
        result = sub(a, b)
    elif operator == "*":
        result = mul(a, b)
    elif operator == "/":
        result = div(a, b)

    print("{} {} {} = {}".format(a, operator, b, result))
else:
    print("{} {} {} = {}".format(a, operator, b, result))
