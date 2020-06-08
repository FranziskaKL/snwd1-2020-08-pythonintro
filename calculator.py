first_num = int(input("Erste Zahl eingeben: "))
operation = input("+ - * or /.")
sec_num = int(input("Zweite Zahl eingeben: "))

if operation == "+":
    print(first_num + sec_num)
elif operation == "-":
    print(first_num - sec_num)
elif operation == "*":
    print(first_num * sec_num)
elif operation == "/":
    print(first_num / sec_num)
else:
    print("Sorry, andere Rechnungen kann ich nicht ausführen.")