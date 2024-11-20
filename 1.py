number_str = input("Введите десятичное число: ")
max_digit = 0
min_digit = 9
for i in range(len(number_str)):
    digit = int(number_str[i])
    if digit > max_digit:
        max_digit = digit
    if digit < min_digit:
        min_digit = digit
print("Самая большая цифра:", max_digit)
print("Самая маленькая цифра", min_digit)