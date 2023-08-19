number = "01033334444"

number = number.replace(number[:-4], len(number[:-4])*"*")

print(number)