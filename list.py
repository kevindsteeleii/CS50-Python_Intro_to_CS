numbers = []

while True:
    number = input("Number: ")

    if not number:
        break
    if number not in numbers:
        numbers.append(number)

for num in numbers:
    print(num)
