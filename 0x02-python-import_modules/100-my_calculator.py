#!/usr/bin/python3
if __name__ == "__main__":
    """Import all functions from the file calculator_1.py and
    handle basic operations
    """
    import sys
    from calculator_1 import add, sub, mul, div

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = sys.argv[2]

    try:
        len(sys.argv) - 1 != 3
    except:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operators = {"+": add, "-": sub, "*": mul, "/": div}
    try:
        operator in list(operators.keys())
    except:
        print("unknown operator. Available operators: +, -, * and /")
        exit(1)

    print("{} {} {} = {}".format(a, operator, b, operators[operator](a, b)))
