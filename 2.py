def is_lucky_ticket(number):
  number_str = str(number)
  first_part = int(number_str[:3])
  second_part = int(number_str[3:])
  if first_part == second_part:
    return True
  else:
    return False
number = int(input("Введите номер белета: "))
if is_lucky_ticket(number):
  print("Счастливый билет")
else:
  print("Несчастливый билет")