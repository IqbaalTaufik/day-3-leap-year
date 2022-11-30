year = int(input("Which year do you want to check? "))

if year % 4:
  print("Leap year.")
elif year % 100:
  print("Not leap year.")
elif year % 400:
  print("Leap year.")
else:
  print("Not Leap year.")