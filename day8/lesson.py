
print("Numbers from 1 to 100 inclusive using a while loop:")
num = 1
while num <= 100:
    print(num, end=" ")
    num += 1
print("\n")


sum_first_10 = 0
for i in range(1, 11):
    sum_first_10 += i
print("Sum of the first 10 numbers:", sum_first_10)


print("\nEven numbers from 1 to 20 using a for loop:")
for num in range(1, 21):
    if num % 2 == 0:
        print(num, end=" ")
