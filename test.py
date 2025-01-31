def check_number(n):
    """Check if a number is even or odd and print the result."""
    if n % 2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

# Example usage
num = int(input("Enter a number: "))
check_number(num)
