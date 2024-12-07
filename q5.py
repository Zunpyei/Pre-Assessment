def check_divisibility(num, divisor):
    """
    Task 1
    - Create a function to check if the number (num) is divisible by another number (divisor).
    - Both num and divisor must be numeric.
    - Return True if num is divisible by divisor, False otherwise.
    """
    if((type(num) == int and type(divisor) == int)
    or (type(num) == float and type(divisor) == float)
    or (type(num) == complex and type(divisor) == complex)):
        if(num % divisor == 0):
            return True
        
    return False


# Task 2
# Invoke the function "check_divisibility" using the following scenarios:
# - 10, 2
# - 7, 3


print(check_divisibility(10, 2))
print(check_divisibility(7, 3))