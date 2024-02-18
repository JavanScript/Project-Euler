# num1 = 1
# num2 = 2
# sum = 0

# while num1 < 4000000:
#     if num1 % 2 == 0:
#         print(num1)
#         sum += num1
#     num1, num2 = num2, num1+num2

# print(sum)


num1 = 1
num2 = 1
num3 = num1 + num2
sum = 0

while num3 < 4000000:
    sum += num3
    num1 = num2 + num3
    num2 = num1 + num3
    num3 = num1 + num2

print(sum)
