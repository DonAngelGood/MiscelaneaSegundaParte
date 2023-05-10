exercises = 0

while exercises < 99:

    exercises = int(input("Enter the number of the exercise you want to run: "))

    elif exercises == 17:
        #Entries
        number = float(input("Enter the number: "))
        # Process and Outputs
        if number > 0:
            print("The number " + str(number) + " is positive")
        elif number < 0:
            print("The number " + str(number) + " is negative")
        else:
            print("The number " + str(number) + " is neutral")

    elif exercises == 18:
        # Entries
        higher = float(input("Enter the first number: "))
        number = float(input("Enter the second number: "))
        # Process and Outputs
        if higher > number:
            print("The higher number is " + str(higher))
        else:
            print("The higher number is " + str(number))

    elif exercises == 19:
        # Entries
        first_number = int(input("Enter the first number: "))
        second_number = int(input("Enter the second number: "))
        third_number = int(input("Enter the third number: "))
        # Process and Outputs
        if first_number > second_number > third_number:
            print("The higher number is " + str(first_number) + " and the lower number is " + str(third_number))
        elif first_number > third_number > second_number:
            print("The higher number is " + str(first_number) + " and the lower number is " + str(second_number))
        elif second_number > first_number > third_number:
            print("The higher number is " + str(second_number) + " and the lower number is " + str(third_number))
        elif second_number > third_number > first_number:
            print("The higher number is " + str(second_number) + " and the lower number is " + str(first_number))
        elif third_number > first_number > second_number:
            print("The higher number is " + str(third_number) + " and the lower number is " + str(second_number))
        else:
            print("The higher number is " + str(third_number) + " and the lower number is " + str(first_number))

    elif exercises == 20:
        # Entries
        name = str(input("Enter the name of the employee: "))
        normal_hours = float(input("Enter the number of normal hours worked: "))
        extra_hours = float(input("Enter the number of extra hours worked: "))
        # Process
        salary = normal_hours * 4 + extra_hours * 8
        # Outputs
        print("The salary of the employee " + name + " is " + str(salary))

    elif exercises == 21:
        # Entries
        number_a = float(input("Enter the number A: "))
        number_b = float(input("Enter the number B: "))
        # Process and Outputs
        if number_a < number_b:
            print("The addition is " + str(number_a + number_b))
        else:
            print("The subtraction is " + str(number_a - number_b))

    elif exercises == 22:
        # Entries
        divider = float(input("Enter the divider: "))
        dividend = float(input("Enter the dividend: "))
        # Process and Outputs
        if dividend == 0:
            print("Cannot be divided by 0")
        else:
            print("The result of division is " + str(divider / dividend))

    elif exercises == 23:
        # Entries
        number_day = int(input("Enter the number of day: "))
        # Process and Outputs
        if number_day == 1:
            print("Monday")
        elif number_day == 2:
            print("Tuesday")
        elif number_day == 3:
            print("Wednesday")
        elif number_day == 4:
            print("Thursday")
        elif number_day == 5:
            print("Friday")
        elif number_day == 6:
            print("Saturday")
        elif number_day == 7:
            print("Sunday")

    elif exercises == 24:
        # Entries
        first_side = float(input("Enter the first side: "))
        second_side = float(input("Enter the second side: "))
        third_side = float(input("Enter the third side: "))
        # Process and Outputs
        if first_side == second_side == third_side:
            print("The triangle is equilateral")
        else:
            print("The triangle is not equilateral")

    elif exercises == 25:
        # Entries
        number_a = float(input("Enter the number A: "))
        number_b = float(input("Enter the number B: "))
        # Process and Outputs
        if number_a < 0 or number_b < 0:
            print("The addition is " + str(number_a + number_b))
        else:
            print("The multiplication is " + str(number_a * number_b))

    elif exercises == 26:
        # Entries
        day = int(input("Enter your day of birth: "))
        month = int(input("Enter the number of your month birth: "))
        # Process and Outputs
        if (month == 1 and 31 >= day >= 20) or (month == 2 and 31 >= day <= 18):
            print("Acuario")
        elif (month == 2 and 28 >= day >= 19) or (month == 3 and 31 >= day <= 20):
            print("Piscis")
        elif (month == 3 and 31 >= day >= 21) or (month == 4 and 31 >= day <= 19):
            print("Aries")
        elif (month == 4 and 31 >= day >= 20) or (month == 5 and 31 >= day <= 20):
            print("Tauro")
        elif (month == 5 and 31 >= day >= 21) or (month == 6 and 31 >= day <= 20):
            print("Géminis")
        elif (month == 6 and 31 >= day >= 21) or (month == 7 and 31 >= day <= 22):
            print("Cáncer")
        elif (month == 7 and 31 >= day >= 23) or (month == 8 and 31 >= day <= 22):
            print("Leo")
        elif (month == 8 and 31 >= day >= 23) or (month == 9 and 31 >= day <= 22):
            print("Virgo")
        elif (month == 9 and 31 >= day >= 23) or (month == 10 and 31 >= day <= 22):
            print("Libra")
        elif (month == 10 and 31 >= day >= 23) or (month == 11 and 31 >= day <= 21):
            print("Escorpio")
        elif (month == 11 and 31 >= day >= 22) or (month == 12 and 31 >= day <= 21):
            print("Sagitario")
        else:
            print("Capricornio")

    elif exercises == 27:
        # Entries
        base = float(input("Enter the base of the quadrilateral: "))
        height = float(input("Enter the height of the quadrilateral: "))
        # Process and Outputs
        if base == height:
            print("The figure is square")
        else:
            print("The figure is rectangular")
        # Outputs
        print("The perimeter of the figure is " + str(base*2 + height*2))
        print("The area of the figure is " + str(base * height))

    elif exercises == 28:
        # Entries
        price = float(input("Enter the sale price: "))
        # Process and Outputs
        if price < 100:
            price -= price * 0.05
            print("The discount is " + str(price * 0.05))
        elif 100 <= price < 200:
            price -= price * 0.10
            print("The discount is " + str(price * 0.10))
        else:
            price -= price * 0.15
            print("The discount is " + str(price * 0.15))
        # Outputs
        print("The price to pay is " + str(price))

    elif exercises == 29:
        # Entries
        year = int(input("Enter year: "))
        # Process and Outputs
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            print(str(year) + " it's a leap year")
        else:
            print(str(year) + " not a leap year")
