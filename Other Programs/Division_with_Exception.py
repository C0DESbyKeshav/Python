def perform_division():
    print("="*40)
    print("         DIVISION CALCULATOR        ")
    print("="*40)

    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))

        result = num1 / num2
        print("-" * 40)
        print(f"Result: {num1} ÷ {num2} = {result:.2f}")

    except ValueError:
        print("-" * 40)
        print("Error: Please enter valid numbers only.")

    except ZeroDivisionError:
        print("-" * 40)
        print("Error: Division by zero is not allowed.")

    print("="*40)


if __name__ == "__main__":
    perform_division()
