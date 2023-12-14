# Mesa and Salas Program

# Compute the sum and product of a number
def result_triple(a, b, c):
    if a == b == c:
        result = a * b * c
    elif a != b != c:
        result = a + b + c
    return result


# Prompt user to input
num1 = eval(input("Enter your first number:"))
num2 = eval(input("Enter your second number:"))
num3 = eval(input("Enter your third number:"))
# Display result
result_num = result_triple(num1, num2, num3)

print(f"Result: {result_num}")
