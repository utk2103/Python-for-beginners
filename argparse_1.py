import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple calculator for basic arithmetic operations.')

    # Adding positional arguments
    parser.add_argument("number1", help='First number', type=int)
    parser.add_argument("number2", help='Second number', type=int)
    parser.add_argument("operation", help='Operation (add, subtract, multiply)', choices=["add", "subtract", "multiply"])

    args = parser.parse_args()

    print(f'Number 1: {args.number1}')
    print(f'Number 2: {args.number2}')
    print(f'Operation: {args.operation}')

    n1 = args.number1
    n2 = args.number2
    result = None

    if args.operation == 'add':
        result = n1 + n2
    elif args.operation == 'subtract':
        result = n1 - n2
    elif args.operation == 'multiply':
        result = n1 * n2
    else:
        print(f'Invalid operation: {args.operation}')
        exit(1)

    print(f'Result: {result}')
