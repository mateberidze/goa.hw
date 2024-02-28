def calculated_expression(age1, age2, age3, age4, age5):
    result = (age1 * age2) / age3 + (age4 + age5) * (age1 + age2)
    return result

# Example ages
age1 = int(input('Enter age 1: '))
age2 = int(input('Enter age 2: '))
age3 = int(input('Enter age 3: '))
age4 = int(input('Enter age 4: '))
age5 = int(input('Enter age 5: '))

# Calculate the expression
result = calculated_expression(age1, age2, age3, age4, age5)
print("Result:", result)
