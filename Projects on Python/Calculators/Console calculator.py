def check_answer(prompt):
    while 1:
        answer = input(prompt)
        if answer == "no":
            return False
        elif answer == "yes":
            return True
        print('Error. Please, enter "yes" or "no".')


def add(number1, number2):
    return number1 + number2


def sub(number1, number2):
    return number1 - number2


def mult(number1, number2):
    return number1 * number2


def div(number1, number2):
    return number1 / number2


def int_div(number1, number2):
    return number1 // number2


def rem_div(number1, number2):
    return number1 % number2


def degree(number1, number2):
    return number1 ** number2


def factorial(number):
    b = 1
    result = 1
    number = int(number)
    for _ in range(number):
        result *= b
        b += 1
    return result


def square_root(number):
    return number ** 0.5


def check_sign(sign):
    if sign == "!" or sign == "+" or sign == "-" or sign == "*" or sign == "*/":
        return True
    elif sign == "/" or sign == "^" or sign == "%" or sign == "//":
        return True
    else:
        return False


def help_sign():
    print('Help1: "+" - Addition; "-" - Subtraction; "*" - Multiplication.')
    print('Help2: "/" - Division; "//" - Integer division; "%" - The remainder of the division.')
    print('Help3: "^" - Degree of number; "!" - Factorial; "*/" - Square root.')


def unsupported_sign():
    print("This sign is not supported!")
    print("Supported operations: +, -, *, ^, /, %, //, !, */.")
    answer = check_answer("Do you need help? (yes/no) ")
    if answer is True:
        help_sign()


print("This is a calculator. Hurray!")
print("Supported operations: +, -, *, ^, /, %, //, !, */.")
while 1:
    answer = check_answer("Do you need help? (yes/no) ")
    if answer is True:
        help_sign()
    break
input("To continue, enter any key: ")
while 1:
    while 1:
        while 1:
            print("Type simple arithmetic expression (e.g. '2 + 2')")
            expression = input(">")
            parts = expression.split()
            if len(parts) == 2:
                num1 = parts[0]
                sign = parts[1]
                if num1 != "-0" and num1 != "+0":
                    try:
                        num1 = float(num1)
                    except ValueError:
                        print('Error! Enter the numbers correctly.')
                        continue
                    if sign == "!" or sign == "*/":
                        if sign == "!":
                            if num1 >= 0 and num1 * 10 % 10 == 0:
                                break
                            print('Wrong number! Enter a natural number or "0".')
                            continue
                        elif sign == "*/":
                            if num1 >= 0:
                                break
                            print('Wrong number! Enter a positive number or "0".')
                            continue
                    if check_sign(sign) is True:
                        print('An expression must consist of three parts.')
                        continue
                    unsupported_sign()
                    continue
                print('I do not like "-0" and "+0".')
                print('Please, enter "0"(without sign) or another number.')
                continue

            if len(parts) == 3:
                num1 = parts[0]
                sign = parts[1]
                num2 = parts[2]
                if num1 != "-0" and num1 != "+0" and num2 != "-0" and num2 != "+0":
                    try:
                        num1 = float(num1)
                        num2 = float(num2)
                    except ValueError:
                        print('Error! Enter the numbers correctly.')
                        continue
                    if check_sign(sign) is True:
                        if sign == "!" or sign == "*/":
                            print('An expression with "!" or "*/" must consist of two parts.')
                            continue
                        break
                    unsupported_sign()
                    continue
                print('I do not like "-0" and "+0".')
                print('Please, enter "0"(without sign) or another number.')
                continue
            print("Error! Please enter correct expression!")

        if sign == "!":
            result = factorial(num1)
        elif sign == "*/":
            result = square_root(num1)
        elif sign == "+":
            result = add(num1, num2)
        elif sign == "-":
            result = sub(num1, num2)
        elif sign == "*":
            result = mult(num1, num2)
        elif sign == "^":
            result = degree(num1, num2)
        elif sign == "/" or sign == "//" or sign == "%":
            try:
                if sign == "/":
                    result = div(num1, num2)
                elif sign == "//":
                    result = int_div(num1, num2)
                elif sign == "%":
                    result = rem_div(num1, num2)
            except ZeroDivisionError:
                print("Error! Cannot divide by zero!")
                continue
        else:
            print("ПАНИК! ЗИС ШУДЭНТ ЭВЕ ХЕПЭН!ahahaha)")
            print("РЕЗУЛТ 0 ИЗ ИНСОРРЕКТ!!!")
            print("Сигн ваз: ", sign)
            result = 0
        break
    parts.append('=')
    parts.append(str(result))
    print("Your result: " + ' '.join(parts))
    answer = check_answer("Would you like to do something else? (yes/no) ")
    if answer is False:
        break
print("Thanks for the use!")
print("do svyazi!")
