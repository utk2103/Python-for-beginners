import argparse  # Why: Handles command-line args, avoids manual parsing

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Simple calculator for basic arithmetic operations.')  # Why: Shows help/usage for users

    parser.add_argument("number1", help='First number', type=int)  # Why: Forces user to provide an int
    parser.add_argument("number2", help='Second number', type=int) # Why: Ensures both numbers are present
    parser.add_argument("operation", help='Operation (add, subtract, multiply)', choices=["add", "subtract", "multiply"])  # Why: Prevents invalid operations

    args = parser.parse_args()  # Why: Converts input to usable vars

    print(f'Number 1: {args.number1}')
    print(f'Number 2: {args.number2}')
    print(f'Operation: {args.operation}')

    n1 = args.number1
    n2 = args.number2
    result = None

    # Why: Simple branching, avoids eval/injection
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
