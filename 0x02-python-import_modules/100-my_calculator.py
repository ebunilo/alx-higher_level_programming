#!/usr/bin/python3
if __name__ == "__main__":
    """Import all functions from the file calculator_1.py and
    handle basic operations
    """
    import sys
    from calculator_1 import add, sub, mul, div

    args = sys.argv
    args_count = len(args) - 1
    operators = ["+", "-", "*", "/"]
    a = int(args[1])
    b = int(args[3])
    operator = args[2]

    if args_count != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if operator not in operators:
        print("unknown operator. Available operators: +, -, * and /")
        exit(1)

    match operator:
        case "+":
            print("{} + {} = {}".format(a, b, add(a, b)))
        case "-":
            print("{} - {} = {}".format(a, b, sub(a, b)))
        case "*":
            print("{} * {} = {}".format(a, b, mul(a, b)))
        case "/":
            print("{} / {} = {}".format(a, b, div(a, b)))
