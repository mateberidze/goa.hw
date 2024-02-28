is_student = False
age = 15
print(is_student and(age < 14))

# is_student = 17
# age = 18
# print(is_student and(age > 12))

# age = 20
# is_student = 21
# if age < 14 or is_student:
#  print("discount")
    

number = int(input("please enter the number between 1-10:"))
if number == 9:
    print("u won full prize")
elif number == 4:
    print("u won half prize")
else:
    print("u won")