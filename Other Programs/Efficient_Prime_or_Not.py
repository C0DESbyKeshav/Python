def is_prime(n):
    
    if n <= 1:
        return False
    
    if n == 2:
        return True
        # 2 is the only even prime number jo yahi pe handle ho gaya so no need to consider it for the further lines in this code.
    
    # All even numbers excluded
    if n % 2 == 0:
        return False
        # This line already eliminates all even numbers (except 2). So no need to check even i values again!
        # Jo number 2 se divide hoga woh even hi hoga aur jo bhi even numbers hoga woh kabhi bhi prime nahi hoga.
        # So jo bhi even number aayega woh directly not_prime ho jaayega yeh condition ke wajah se toh less time lagega.
    
    # Separated computation only on odd prime numbers
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
        # Hum log sirf odd i numbers 1, 3, 5, 7,... ke liye hi loop ko run karenge kyuki even numbers already previous conditional statement mein handle ho gaya hai.
        # But kyuki humne loop ko 3 se start kiya hai toh ab i = 3, 5, 7, 9,....
        # * We skip even i because they can’t divide any odd prime number (except 2)
        # Odd prime numbers are not divisible by any number other than 1 and themselves.
        # Why go only up to √n and not all the way to n-1?
        # If a number n is divisible by some number i, then it's also divisible by n // i.
        # n//i ==> It divides the number like normal, but discards anything after the decimal point (rounds down to the nearest whole number).
    return True


def main():
    print("="*40)
    print("        PRIME NUMBER CHECKER        ")
    print("="*40)

    try:
        num = int(input("Enter a number to check: "))
        print("-" * 40)

        if is_prime(num):
            print(f"{num} is a Prime Number.")
        else:
            print(f"{num} is NOT a Prime Number.")
    
    except ValueError:
        print("Invalid input. Please enter an integer.")

    print("="*40)


if __name__ == "__main__":
    main()
