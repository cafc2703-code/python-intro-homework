# Warmup 4: Sign and Parity

number = int(input("Enter a number: "))
# Check the sign
if number > 0:
print(number, "is positive.")
elif number < 0:
print(number, "is negative.")
else:
print(number, "is zero.")

# Check if the number is even or odd
if number % 2 == 0:
print(number, "is even.")
else:
print(number, "is odd.")
