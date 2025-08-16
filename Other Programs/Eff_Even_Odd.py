def is_even(number) -> bool:
    """
    Checks if the input number is even.
    Returns True if even, False if odd.
    Handles large integers and invalid inputs gracefully.
    """
    try:
        number = int(number)
        return (number & 1) == 0
    # Bitwise AND (&) is faster than modulus (%) or division (/).
    # (number & 1) checks the least significant bit — if it's 0, the number is even; if it's 1, the number is odd.
    
    except (ValueError, TypeError):
        raise ValueError("Input must be a valid integer.")
        # Sometimes we want that the program should crash when it encounters only that one specific error instead of just continuing further after printing the error message.


def main():
    try:
        num = input("Enter a number: ").strip()
        # Passing " 42 " (with spaces) directly to int() will still work — Python is lenient — but using .strip() is a good practice
        
        if is_even(num):
            print("Even")
        else:
            print("Odd")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
