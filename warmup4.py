# Warmup 4: Sign and Parity

number = int(input("Enter a number: "))

# Sign
if number > 0:
    print(f"{number} is positive.")
elif number < 0:
    print(f"{number} is negative.")
else:
    print(f"{number} is zero.")

# Parity
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
