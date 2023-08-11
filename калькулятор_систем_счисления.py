def num_systems():
    def greeting():
        print("                **    **  ********  **        **            **      ")
        print("               **    **  ********  **        **         **     **   ")
        print("              ********  **        **        **         **      **  ")
        print("             ********  ********  **        **         **      **  ")
        print("            **    **  **        **        **         **      **  ")
        print("           **    **  ********  ********  ********    **    **   ")
        print("          **    **  ********  ********  ********       **      ")
        print("Приветствую вас программе для работы с числами различных систем счисления! ")
        questions()

    def convert_to(num, num_bas, bas):
        numbers = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23,
                   24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if num_bas == 10:
            n = ''
            num = int(num)
            while not num < bas:
                n += str(digits[num % bas])
                num //= bas
            n = str(num) + n[::-1]
        else:
            n = 0
            cnt = 0
            while num != '':
                if num[-1].isdigit():
                    last_digit = int(num[-1])
                else:
                    last_digit = numbers[digits.index(num[-1].upper()) - 10]
                n += int(last_digit) * num_bas ** cnt
                num = num[:-1]
                cnt += 1
        return str(n)

    def comparison():
        while True:
            num_bas_1 = input('В какой системе счисления первое число? (введите число) ')
            if num_bas_1.isdigit() and 1 < int(num_bas_1) < 37:
                num_bas_1 = int(num_bas_1)
                break
            elif num_bas_1.isdigit() and int(num_bas_1) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif num_bas_1.isdigit() and int(num_bas_1) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        while True:
            num_1 = input('Введите первое число: ')
            num_1 = num_1.strip()
            flag = True
            for i in num_1:
                res = convert_to(i, num_bas_1, 10)
                if int(res) >= num_bas_1:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('Указанное число содержит недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            num_bas_2 = input('В какой системе счисления второе число? (введите число) ')
            if num_bas_2.isdigit() and 1 < int(num_bas_2) < 37:
                num_bas_2 = int(num_bas_2)
                break
            elif num_bas_2.isdigit() and int(num_bas_2) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif num_bas_2.isdigit() and int(num_bas_2) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        while True:
            num_2 = input('Введите второе число: ')
            num_2 = num_2.strip()
            flag = True
            for i in num_2:
                res = convert_to(i, num_bas_2, 10)
                if int(res) >= num_bas_2:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('Указанное число содержит недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        if int(convert_to(num_1, num_bas_1, 10)) > int(convert_to(num_2, num_bas_2, 10)):
            print(f'{num_1} в {num_bas_1}-й системе счисления больше {num_2} в {num_bas_2}-й системе счисления')
        elif int(convert_to(num_1, num_bas_1, 10)) < int(convert_to(num_2, num_bas_2, 10)):
            print(f'{num_1} в {num_bas_1}-й системе счисления меньше {num_2} в {num_bas_2}-й системе счисления')
        else:
            print(f'{num_1} в {num_bas_1}-й системе счисления равно {num_2} в {num_bas_2}-й системе счисления')

    def addition():
        while True:
            num_bas_1 = input('В какой системе счисления первое слагаемое? (введите число) ')
            if num_bas_1.isdigit() and 1 < int(num_bas_1) < 37:
                num_bas_1 = int(num_bas_1)
                break
            elif num_bas_1.isdigit() and int(num_bas_1) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif num_bas_1.isdigit() and int(num_bas_1) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        while True:
            num_1 = input('Введите первое слагаемое: ')
            num_1 = num_1.strip()
            flag = True
            for i in num_1:
                res = convert_to(i, num_bas_1, 10)
                if int(res) >= num_bas_1:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('Указанное число содержит недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            num_bas_2 = input('В какой системе счисления второе слагаемое? (введите число) ')
            if num_bas_2.isdigit() and 1 < int(num_bas_2) < 37:
                num_bas_2 = int(num_bas_2)
                break
            elif num_bas_2.isdigit() and int(num_bas_2) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif num_bas_2.isdigit() and int(num_bas_2) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        while True:
            num_2 = input('Введите второе слагаемое: ')
            num_2 = num_2.strip()
            flag = True
            for i in num_2:
                res = convert_to(i, num_bas_2, 10)
                if int(res) >= num_bas_2:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('Указанное число содержит недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            res_bas = input('В какой системе счисления вы хотите сумму? (введите число) ')
            if res_bas.isdigit() and 1 < int(res_bas) < 37:
                res_bas = int(res_bas)
                break
            elif res_bas.isdigit() and int(res_bas) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif res_bas.isdigit() and int(res_bas) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        print(convert_to(int(convert_to(num_1, num_bas_1, 10)) + int(convert_to(num_2, num_bas_2, 10)), 10, res_bas))

    def subtraction():
        while True:
            num_bas_1 = input('В какой системе счисления уменьшаемое? (введите число) ')
            if num_bas_1.isdigit() and 1 < int(num_bas_1) < 37:
                num_bas_1 = int(num_bas_1)
                break
            elif num_bas_1.isdigit() and int(num_bas_1) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif num_bas_1.isdigit() and int(num_bas_1) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        while True:
            num_1 = input('Введите уменьшаемое: ')
            num_1 = num_1.strip()
            flag = True
            for i in num_1:
                res = convert_to(i, num_bas_1, 10)
                if int(res) >= num_bas_1:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('Указанное число содержит недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            num_bas_2 = input('В какой системе счисления вычитаемое? (введите число) ')
            if num_bas_2.isdigit() and 1 < int(num_bas_2) < 37:
                num_bas_2 = int(num_bas_2)
                break
            elif num_bas_2.isdigit() and int(num_bas_2) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif num_bas_2.isdigit() and int(num_bas_2) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        while True:
            num_2 = input('Введите вычитаемое: ')
            num_2 = num_2.strip()
            flag = True
            for i in num_2:
                res = convert_to(i, num_bas_2, 10)
                if int(res) >= num_bas_2:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('Указанное число содержит недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            res_bas = input('В какой системе счисления вы хотите разность? (введите число) ')
            if res_bas.isdigit() and 1 < int(res_bas) < 37:
                res_bas = int(res_bas)
                break
            elif res_bas.isdigit() and int(res_bas) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif res_bas.isdigit() and int(res_bas) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        print(convert_to(int(convert_to(num_1, num_bas_1, 10)) - int(convert_to(num_2, num_bas_2, 10)), 10, res_bas))

    def multiplication():
        while True:
            num_bas_1 = input('В какой системе счисления первый множитель? (введите число) ')
            if num_bas_1.isdigit() and 1 < int(num_bas_1) < 37:
                num_bas_1 = int(num_bas_1)
                break
            elif num_bas_1.isdigit() and int(num_bas_1) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif num_bas_1.isdigit() and int(num_bas_1) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        while True:
            num_1 = input('Введите первый множитель: ')
            num_1 = num_1.strip()
            flag = True
            for i in num_1:
                res = convert_to(i, num_bas_1, 10)
                if int(res) >= num_bas_1:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('Указанное число содержит недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            num_bas_2 = input('В какой системе счисления второй множитель? (введите число) ')
            if num_bas_2.isdigit() and 1 < int(num_bas_2) < 37:
                num_bas_2 = int(num_bas_2)
                break
            elif num_bas_2.isdigit() and int(num_bas_2) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif num_bas_2.isdigit() and int(num_bas_2) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        while True:
            num_2 = input('Введите вторый множитель: ')
            num_2 = num_2.strip()
            flag = True
            for i in num_2:
                res = convert_to(i, num_bas_2, 10)
                if int(res) >= num_bas_2:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('Указанное число содержит недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            res_bas = input('В какой системе счисления вы хотите произведение? (введите число) ')
            if res_bas.isdigit() and 1 < int(res_bas) < 37:
                res_bas = int(res_bas)
                break
            elif res_bas.isdigit() and int(res_bas) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif res_bas.isdigit() and int(res_bas) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        print(convert_to(int(convert_to(num_1, num_bas_1, 10)) * int(convert_to(num_2, num_bas_2, 10)), 10, res_bas))

    def division():
        while True:
            num_bas_1 = input('В какой системе счисления делимое? (введите число) ')
            if num_bas_1.isdigit() and 1 < int(num_bas_1) < 37:
                num_bas_1 = int(num_bas_1)
                break
            elif num_bas_1.isdigit() and int(num_bas_1) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif num_bas_1.isdigit() and int(num_bas_1) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        while True:
            num_1 = input('Введите делимое: ')
            num_1 = num_1.strip()
            flag = True
            for i in num_1:
                res = convert_to(i, num_bas_1, 10)
                if int(res) >= num_bas_1:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('Указанное число содержит недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            num_bas_2 = input('В какой системе счисления делитель? (введите число) ')
            if num_bas_2.isdigit() and 1 < int(num_bas_2) < 37:
                num_bas_2 = int(num_bas_2)
                break
            elif num_bas_2.isdigit() and int(num_bas_2) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif num_bas_2.isdigit() and int(num_bas_2) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        while True:
            num_2 = input('Введите делитель: ')
            num_2 = num_2.strip()
            flag = True
            for i in num_2:
                res = convert_to(i, num_bas_2, 10)
                if int(res) >= num_bas_2:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('Указанное число содержит недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            res_bas = input('В какой системе счисления вы хотите частное? (введите число) ')
            if res_bas.isdigit() and 1 < int(res_bas) < 37:
                res_bas = int(res_bas)
                break
            elif res_bas.isdigit() and int(res_bas) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif res_bas.isdigit() and int(res_bas) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        print(convert_to(int(convert_to(num_1, num_bas_1, 10)) / int(convert_to(num_2, num_bas_2, 10)), 10, res_bas))

    def degree():
        while True:
            num_bas = input('В какой системе счисления число основание степени? (введите число) ')
            if num_bas.isdigit() and 1 < int(num_bas) < 37:
                num_bas = int(num_bas)
                break
            elif num_bas.isdigit() and int(num_bas) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif num_bas.isdigit() and int(num_bas) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        while True:
            num = input('Введите основание степени: ')
            num = num.strip()
            flag = True
            for i in num:
                res = convert_to(i, num_bas, 10)
                if int(res) >= num_bas:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('Указанное число содержит недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            degree_bas = input('В какой системе счисления показатель степени? (введите число) ')
            if degree_bas.isdigit() and 1 < int(degree_bas) < 37:
                degree_bas = int(degree_bas)
                break
            elif degree_bas.isdigit() and int(degree_bas) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif degree_bas.isdigit() and int(degree_bas) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
        while True:
            degree_ = input('Введите показатель степени: ')
            for i in degree_:
                flag = True
                if i in '0123456789.,':
                    if i == ',':
                        degree_.replace(i, '.')
                else:
                    flag = False
                    break
            if flag:
                degree_ = int(degree_)
                break
            else:
                print('А может быть все-таки введём рациональное число? ')
                continue
        while True:
            res_bas = input('В какой системе счисления вы хотите результат? (введите число) ')
            if res_bas.isdigit() and 1 < int(res_bas) < 37:
                res_bas = int(res_bas)
                break
            elif res_bas.isdigit() and 37 < int(res_bas):
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif res_bas.isdigit() and int(res_bas) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        print(convert_to(int(convert_to(num, num_bas, 10)) ** int(convert_to(degree_, degree_bas, 10)), 10, res_bas))

    def root():
        while True:
            num_bas = input('В какой системе счисления данное число? (введите число) ')
            if num_bas.isdigit() and 1 < int(num_bas) < 37:
                num_bas = int(num_bas)
                break
            elif num_bas.isdigit() and int(num_bas) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif num_bas.isdigit() and int(num_bas) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        while True:
            num = input('Введите число для извлечения из него корня: ')
            num = num.strip()
            flag = True
            for i in num:
                res = convert_to(i,  num_bas, 10)
                if int(res) >= num_bas:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('Указанное число содержит недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            root_ = input('Какой корень вы хотите извлечь из данного числа? (введите число) ')
            for i in root_:
                flag = True
                if i in '0123456789.,':
                    if i == ',':
                        i = '.'
                else:
                    flag = False
                    break
            if flag and int(convert_to(num, num_bas, 10)) < 0 and int(root_) % 2 == 0:
                print('Нельзя извлекать чётный корень из отрицательного числа! ')
            elif flag:
                root_ = int(root_)
                break
            else:
                print('А может быть все-таки введём рациональное число? ')
                continue
        while True:
            signs = input('Сколько цифр вам нужно после запятой? (введите число) ')
            print('P.S. программа не показывает нули после запятой')
            for i in signs:
                flag = True
                if i not in '0123456789':
                    flag = False
                    break
            if flag:
                signs = int(signs)
                break
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        import math
        print(round(pow(float(convert_to(num, num_bas, 10)), 1 / root_), signs))

    def factorial():
        while True:
            num_bas = input('В какой системе счисления данное число? (введите число) ')
            if num_bas.isdigit() and 1 < int(num_bas) < 37:
                num_bas = int(num_bas)
                break
            elif num_bas.isdigit() and int(num_bas) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif num_bas.isdigit() and int(num_bas) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        while True:
            num = input('Введите число для факториала: ')
            num = num.strip()
            flag = True
            for i in num:
                res = convert_to(i,  num_bas, 10)
                if int(res) >= num_bas:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('Указанное число содержит недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            res_bas = input('В какой системе счисления вы хотите результат? (введите число) ')
            if res_bas.isdigit() and 1 < int(res_bas) < 37:
                res_bas = int(res_bas)
                break
            elif res_bas.isdigit() and int(res_bas) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif res_bas.isdigit() and int(res_bas) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        factorial_ = 1
        for i in range(1, int(convert_to(num, num_bas, 10)) + 1):
            factorial_ *= i
        factorial_ = convert_to(factorial_, 10, res_bas)
        print(factorial_)

    def percent():
        while True:
            num_bas = input('В какой системе счисления данное число? (введите число) ')
            if num_bas.isdigit() and 1 < int(num_bas) < 37:
                num_bas = int(num_bas)
                break
            elif num_bas.isdigit() and int(num_bas) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif num_bas.isdigit() and int(num_bas) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        while True:
            num = input('Введите число для извлечения процента из него : ')
            num = num.strip()
            flag = True
            for i in num:
                res = convert_to(i,  num_bas, 10)
                if int(res) >= num_bas:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('Указанное число содержит недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            percent_ = input('Какой процент вы хотите извлечь из данного числа? (введите число) ')
            for i in percent_:
                flag = True
                if i in '0123456789.,':
                    if i == ',':
                        i = '.'
                else:
                    flag = False
                    break
            if flag:
                percent_ = int(percent_)
                break
            else:
                print('А может быть все-таки введём рациональное число? ')
                continue
        while True:
            res_bas = input('В какой системе счисления вы хотите результат? (введите число) ')
            if res_bas.isdigit() and 1 < int(res_bas) < 37:
                res_bas = int(res_bas)
                break
            elif res_bas.isdigit() and int(res_bas) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif res_bas.isdigit() and int(res_bas) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        print(convert_to(int(convert_to(num, num_bas, 10)) * (percent_ / 100), 10, res_bas))

    def grad_to_rad(grad):
        from math import pi as p
        return float(grad) * p / 180

    def hail_to_rad(hail):
        return float(hail) * 0.015707963267949

    def rad_to_grad(rad):
        from math import pi as p
        return float(rad) * 180 / p

    def rad_to_hail(rad):
        return float(rad) * 63.661977236758

    def grad_to_hail(grad):
        return float(grad) * 10 / 9

    def hail_to_grad(hail):
        return float(hail) * 0.9

    def sin():
        while True:
            print('В какой системе измерения плоских углов данный угол?')
            print('Введите "grad" - градусы, или "rad" - радианы, или "hail" - грады')
            unit_change = input().strip().lower()
            if unit_change == "grad" or unit_change == "rad" or unit_change == "hail":
                break
            else:
                print('Я не понимаю ')
                continue
        while True:
            num_bas = input('В какой системе счисления данный угол? (введите целое число) ')
            if num_bas.isdigit() and 1 < int(num_bas) < 37:
                num_bas = int(num_bas)
                break
            elif num_bas.isdigit() and int(num_bas) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif num_bas.isdigit() and int(num_bas) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        while True:
            num = input('Введите угол для нахождения синуса (введите целое число) ')
            num = num.strip()
            flag = True
            for i in num:
                digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                if digits.index(i) >= num_bas:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('Указанное число содержит недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            signs = input('Сколько цифр вам нужно после запятой? (введите число) ')
            for i in signs:
                flag = True
                if i not in '0123456789':
                    flag = False
                    break
            if flag:
                signs = int(signs)
                break
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        print('P.S. Программа не выводит нули после запятой! ')
        print('P.S. Программа выводит результат в десятичной системе счисления! ')
        import math
        if unit_change == 'grad':
            print(round(math.sin(grad_to_rad(int(convert_to(num, num_bas, 10)))), signs))
        elif unit_change == 'hail':
            print(round(math.sin(hail_to_rad(int(convert_to(num, num_bas, 10)))), signs))
        else:
            print(round(math.sin(int(convert_to(num, num_bas, 10))), signs))

    def cos():
        while True:
            print('В какой системе измерения плоских углов данный угол?')
            print('Введите "grad" - градусы, или "rad" - радианы, или "hail" - грады')
            unit_change = input().strip().lower()
            if unit_change == "grad" or unit_change == "rad" or unit_change == "hail":
                break
            else:
                print('Я не понимаю ')
                continue
        while True:
            num_bas = input('В какой системе счисления данный угол? (введите целое число) ')
            if num_bas.isdigit() and 1 < int(num_bas) < 37:
                num_bas = int(num_bas)
                break
            elif num_bas.isdigit() and int(num_bas) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif num_bas.isdigit() and int(num_bas) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        while True:
            num = input('Введите угол для нахождения косинуса (введите целое число) ')
            num = num.strip()
            flag = True
            for i in num:
                digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                if digits.index(i) >= num_bas:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('Указанное число содержит недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            signs = input('Сколько цифр вам нужно после запятой? (введите число) ')
            for i in signs:
                flag = True
                if i not in '0123456789':
                    flag = False
                    break
            if flag:
                signs = int(signs)
                break
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        print('P.S. Программа не выводит нули после запятой! ')
        print('P.S. Программа выводит результат в десятичной системе счисления! ')
        import math
        if unit_change == 'grad':
            print(round(math.cos(grad_to_rad(int(convert_to(num, num_bas, 10)))), signs))
        elif unit_change == 'hail':
            print(round(math.cos(hail_to_rad(int(convert_to(num, num_bas, 10)))), signs))
        else:
            print(round(math.cos(int(convert_to(num, num_bas, 10))), signs))

    def tg():
        while True:
            print('В какой системе измерения плоских углов данный угол?')
            print('Введите "grad" - градусы, или "rad" - радианы, или "hail" - грады')
            unit_change = input().strip().lower()
            if unit_change == "grad" or unit_change == "rad" or unit_change == "hail":
                break
            else:
                print('Я не понимаю ')
                continue
        while True:
            num_bas = input('В какой системе счисления данный угол? (введите целое число) ')
            if num_bas.isdigit() and 1 < int(num_bas) < 37:
                num_bas = int(num_bas)
                break
            elif num_bas.isdigit() and int(num_bas) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif num_bas.isdigit() and int(num_bas) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        while True:
            num = input('Введите угол для нахождения тангенса (введите целое число) ')
            num = num.strip()
            flag = True
            for i in num:
                digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                if digits.index(i) >= num_bas:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('Указанное число содержит недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            signs = input('Сколько цифр вам нужно после запятой? (введите число) ')
            for i in signs:
                flag = True
                if i not in '0123456789':
                    flag = False
                    break
            if flag:
                signs = int(signs)
                break
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        print('P.S. Программа не выводит нули после запятой! ')
        print('P.S. Программа выводит результат в десятичной системе счисления! ')
        import math
        if unit_change == 'grad':
            print(round(math.tan(grad_to_rad(int(convert_to(num, num_bas, 10)))), signs))
        elif unit_change == 'hail':
            print(round(math.tan(hail_to_rad(int(convert_to(num, num_bas, 10)))), signs))
        else:
            print(round(math.tan(int(convert_to(num, num_bas, 10))), signs))

    def ctg():
        while True:
            print('В какой системе измерения плоских углов данный угол?')
            print('Введите "grad" - градусы, или "rad" - радианы, или "hail" - грады')
            unit_change = input().strip().lower()
            if unit_change == "grad" or unit_change == "rad" or unit_change == "hail":
                break
            else:
                print('Я не понимаю ')
                continue
        while True:
            num_bas = input('В какой системе счисления данный угол? (введите целое число) ')
            if num_bas.isdigit() and 1 < int(num_bas) < 37:
                num_bas = int(num_bas)
                break
            elif num_bas.isdigit() and int(num_bas) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif num_bas.isdigit() and int(num_bas) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        while True:
            num = input('Введите угол для нахождения котангенса (введите целое число) ')
            num = num.strip()
            flag = True
            for i in num:
                digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                if digits.index(i) >= num_bas:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('Указанное число содержит недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        while True:
            signs = input('Сколько цифр вам нужно после запятой? (введите число) ')
            for i in signs:
                flag = True
                if i not in '0123456789':
                    flag = False
                    break
            if flag:
                signs = int(signs)
                break
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        print('P.S. Программа не выводит нули после запятой! ')
        print('P.S. Программа выводит результат в десятичной системе счисления! ')
        import math
        if unit_change == 'grad':
            print(round(1 / (math.tan(grad_to_rad(int(convert_to(num, num_bas, 10))))), signs))
        elif unit_change == 'hail':
            print(round(1 / (math.tan(hail_to_rad(int(convert_to(num, num_bas, 10))))), signs))
        else:
            print(round(1 / (math.tan(int(convert_to(num, num_bas, 10)))), signs))

    def reverse_sin():
        while True:
            sine = input('По какому синусу вы хотите найти угол? ')
            for i in sine:
                if i == ',':
                    ind = sine.index(',')
                    sine = sine[:ind] + '.' + sine[ind + 1:]
                flag = True
                if i not in '0123456789.,' or sine.count('.') > 1 or sine.count(',') > 1:
                    flag = False
                    break
            if flag and 0 <= float(sine) <= 1:
                sine = float(sine)
                break
            elif flag and 0 <= float(sine) <= 1:
                print('Отношение сторон всегда больше или равно 0 и меньше или равно 1! ')
            else:
                print('А может быть все-таки введём рациональное число? ')
                continue
        while True:
            print('В какой системе измерения плоских углов вы хотите получить угол?')
            print('Введите "grad" - градусы, или "rad" - радианы, или "hail" - грады')
            unit_change = input().strip().lower()
            if unit_change == "grad" or unit_change == "rad" or unit_change == "hail":
                break
            else:
                print('Я не понимаю ')
                continue
        while True:
            res_bas = input('В какой системе счисления вы хотите получить угол? (введите число) ')
            if res_bas.isdigit() and 1 < int(res_bas) < 37:
                res_bas = int(res_bas)
                break
            elif res_bas.isdigit() and int(res_bas) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif res_bas.isdigit() and int(res_bas) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        print('P.S. Результат будет целым числом! ')
        import math
        if unit_change == 'grad':
            print(convert_to(int(rad_to_grad(math.asin(sine))), 10, res_bas))
        elif unit_change == 'hail':
            print(convert_to(int(rad_to_hail(math.asin(sine))), 10, res_bas))
        else:
            print(convert_to(int(math.asin(sine)), 10, res_bas))

    def reverse_cos():
        while True:
            cosine = input('По какому синусу вы хотите найти угол? ')
            for i in cosine:
                if i == ',':
                    ind = cosine.index(',')
                    cosine = cosine[:ind] + '.' + cosine[ind + 1:]
                flag = True
                if i not in '0123456789.,' or cosine.count('.') > 1 or cosine.count(',') > 1:
                    flag = False
                    break
            if flag and 0 <= float(cosine) <= 1:
                cosine = float(cosine)
                break
            elif flag and 0 <= float(cosine) <= 1:
                print('Отношение сторон всегда больше или равно 0 и меньше или равно 1! ')
            else:
                print('А может быть все-таки введём рациональное число? ')
                continue
        while True:
            print('В какой системе измерения плоских углов вы хотите получить угол?')
            print('Введите "grad" - градусы, или "rad" - радианы, или "hail" - грады')
            unit_change = input().strip().lower()
            if unit_change == "grad" or unit_change == "rad" or unit_change == "hail":
                break
            else:
                print('Я не понимаю ')
                continue
        while True:
            res_bas = input('В какой системе счисления вы хотите получить угол? (введите число) ')
            if res_bas.isdigit() and 1 < int(res_bas) < 37:
                res_bas = int(res_bas)
                break
            elif res_bas.isdigit() and int(res_bas) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif res_bas.isdigit() and int(res_bas) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        print('P.S. Результат будет целым числом! ')
        import math
        if unit_change == 'grad':
            print(convert_to(int(rad_to_grad(math.acos(cosine))), 10, res_bas))
        elif unit_change == 'hail':
            print(convert_to(int(rad_to_hail(math.acos(cosine))), 10, res_bas))
        else:
            print(convert_to(int(math.acos(cosine)), 10, res_bas))

    def reverse_tg():
        while True:
            tangent = input('По какому синусу вы хотите найти угол? ')
            for i in tangent:
                if i == ',':
                    ind = tangent.index(',')
                    tangent = tangent[:ind] + '.' + tangent[ind + 1:]
                flag = True
                if i not in '0123456789.,' or tangent.count('.') > 1 or tangent.count(',') > 1:
                    flag = False
                    break
            if flag and 0 <= float(tangent) <= 1:
                tangent = float(tangent)
                break
            elif flag and 0 <= float(tangent) <= 1:
                print('Отношение сторон всегда больше или равно 0 и меньше или равно 1! ')
            else:
                print('А может быть все-таки введём рациональное число? ')
                continue
        while True:
            print('В какой системе измерения плоских углов вы хотите получить угол?')
            print('Введите "grad" - градусы, или "rad" - радианы, или "hail" - грады')
            unit_change = input().strip().lower()
            if unit_change == "grad" or unit_change == "rad" or unit_change == "hail":
                break
            else:
                print('Я не понимаю ')
                continue
        while True:
            res_bas = input('В какой системе счисления вы хотите получить угол? (введите число) ')
            if res_bas.isdigit() and 1 < int(res_bas) < 37:
                res_bas = int(res_bas)
                break
            elif res_bas.isdigit() and int(res_bas) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif res_bas.isdigit() and int(res_bas) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        print('P.S. Результат будет целым числом! ')
        import math
        if unit_change == 'grad':
            print(convert_to(int(rad_to_grad(math.atan(tangent))), 10, res_bas))
        elif unit_change == 'hail':
            print(convert_to(int(rad_to_hail(math.atan(tangent))), 10, res_bas))
        else:
            print(convert_to(int(math.atan(tangent)), 10, res_bas))

    def reverse_ctg():
        while True:
            cotangence = input('По какому синусу вы хотите найти угол? ')
            for i in cotangence:
                if i == ',':
                    ind = cotangence.index(',')
                    cotangence = cotangence[:ind] + '.' + cotangence[ind + 1:]
                flag = True
                if i not in '0123456789.,' or cotangence.count('.') > 1 or cotangence.count(',') > 1:
                    flag = False
                    break
            if flag and 0 <= float(cotangence) <= 1:
                cotangence = float(cotangence)
                break
            elif flag and 0 <= float(cotangence) <= 1:
                print('Отношение сторон всегда больше или равно 0 и меньше или равно 1! ')
            else:
                print('А может быть все-таки введём рациональное число? ')
                continue
        while True:
            print('В какой системе измерения плоских углов вы хотите получить угол?')
            print('Введите "grad" - градусы, или "rad" - радианы, или "hail" - грады')
            unit_change = input().strip().lower()
            if unit_change == "grad" or unit_change == "rad" or unit_change == "hail":
                break
            else:
                print('Я не понимаю ')
                continue
        while True:
            res_bas = input('В какой системе счисления вы хотите получить угол? (введите число) ')
            if res_bas.isdigit() and 1 < int(res_bas) < 37:
                res_bas = int(res_bas)
                break
            elif res_bas.isdigit() and int(res_bas) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif res_bas.isdigit() and int(res_bas) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        print('P.S. Результат будет целым числом! ')
        import math
        if unit_change == 'grad':
            print(convert_to(int(rad_to_grad(math.atan(1 / cotangence))), 10, res_bas))
        elif unit_change == 'hail':
            print(convert_to(int(rad_to_hail(math.atan(1 / cotangence))), 10, res_bas))
        else:
            print(convert_to(int(math.atan(1 / cotangence)), 10, res_bas))

    def convert_corners():
        global signs, res_bas
        while True:
            print('В какой системе измерения плоских углов данный угол?')
            print('Введите "grad" - градусы, или "rad" - радианы, или "hail" - грады')
            unit_corner = input().strip().lower()
            if unit_corner == "grad" or unit_corner == "rad" or unit_corner == "hail":
                break
            else:
                print('Я не понимаю ')
                continue
        while True:
            bas = input('В какой системе счисления данный угол? (введите число) ')
            if bas.isdigit() and 1 < int(bas) < 37:
                bas = int(bas)
                break
            elif bas.isdigit() and int(bas) > 37:
                print('Основание системы счисления не может превышать 36! ')
                continue
            elif bas.isdigit() and int(bas) < 2:
                print('Основание системы счисления не может быть меньше 2! ')
                continue
            else:
                print('А может быть все-таки введём целое число? ')
                continue
        while True:
            print('В какую систему измерения плоских углов вы хотите перевести данный угол?')
            print('Введите "grad" - градусы, или "rad" - радианы, или "hail" - грады')
            res_unit_corner = input().strip().lower()
            if res_unit_corner == unit_corner:
                print('Это бесмысленно!')
                continue
            elif res_unit_corner == "grad" or res_unit_corner == "rad" or res_unit_corner == "hail" and \
                    res_unit_corner != unit_corner:
                break
            else:
                print('Я не понимаю ')
                continue
        if res_unit_corner == 'rad':
            print('P.S. Результат конвертации будет в десятичной системе счисления! ')
            while True:
                signs = input('Сколько цифр вам нужно после запятой? (введите число) ')
                for i in signs:
                    flag = True
                    if i not in '0123456789':
                        flag = False
                        break
                if flag:
                    signs = int(signs)
                    break
                else:
                    print('А может быть все-таки введём целое число? ')
                    continue
        else:
            while True:
                print('P.S. Результат будет целым числом! ')
                res_bas = input('В какой системе счисления вы хотите результат? (введите число) ')
                if res_bas.isdigit() and 1 < int(res_bas) < 37:
                    res_bas = int(res_bas)
                    break
                elif res_bas.isdigit() and int(res_bas) > 37:
                    print('Основание системы счисления не может превышать 36! ')
                    continue
                elif res_bas.isdigit() and int(res_bas) < 2:
                    print('Основание системы счисления не может быть меньше 2! ')
                    continue
                else:
                    print('А может быть все-таки введём целое число? ')
                    continue
        while True:
            num = input('Введите угол для конвертации (введите целое число) ')
            num = num.strip()
            flag = True
            for i in num:
                res = convert_to(i, bas, 10)
                if int(res) >= bas:
                    flag = False
                elif not i.isdigit() and not i.isalpha():
                    flag = False
            if not flag:
                print('Указанное число содержит недопустимые для исходной системы счисления символы')
                continue
            else:
                break
        if unit_corner == 'rad' and res_unit_corner == 'grad':
            print(convert_to(rad_to_grad(convert_to(num, bas, 10)), 10, res_bas))
        elif unit_corner == 'rad' and res_unit_corner == 'hail':
            print(convert_to(rad_to_hail(convert_to(num, bas, 10)), 10, res_bas))
        elif unit_corner == 'grad' and res_unit_corner == 'hail':
            print(convert_to(grad_to_hail(convert_to(num, bas, 10)), 10, res_bas))
        elif unit_corner == 'grad' and res_unit_corner == 'rad':
            print(round(grad_to_rad(convert_to(num, bas, 10)), signs))
        elif unit_corner == 'hail' and res_unit_corner == 'grad':
            print(convert_to(hail_to_grad(convert_to(num, bas, 10)), 10, res_bas))
        else:
            print(round(hail_to_rad(convert_to(num, bas, 10)), signs))

    def questions():
        print('Выберите какие именно операции вы хотите делать над числами:')
        print('Введите "1", если вы хотите конвертировать число из одной системы счисления в другую ')
        print('Введите "2", если вы хотите произвести математические операции над двумя числами разных систем '
              'счисления ')
        while True:
            choice = input().strip()
            if choice == '1':
                while True:
                    num_bas = input('В какой системе счисления данное число? (введите число) ')
                    if num_bas.isdigit() and 1 < int(num_bas) < 37:
                        num_bas = int(num_bas)
                        break
                    elif num_bas.isdigit() and int(num_bas) > 37:
                        print('Основание системы счисления не может превышать 36! ')
                        continue
                    elif num_bas.isdigit() and int(num_bas) < 2:
                        print('Основание системы счисления не может быть меньше 2! ')
                        continue
                    else:
                        print('А может быть все-таки введём целое число? ')
                        continue
                while True:
                    num = input('Введите число для преобразования: ')
                    num = num.strip()
                    flag = True
                    for i in num:
                        res = convert_to(i, num_bas, 10)
                        if int(res) >= num_bas:
                            flag = False
                        elif not i.isdigit() and not i.isalpha():
                            flag = False
                    if not flag:
                        print('Указанное число содержит недопустимые для исходной системы счисления символы')
                        continue
                    else:
                        break
                while True:
                    bas = input('В какую систему счисления нужно перевести число? (введите число) ')
                    if bas.isdigit() and 1 < int(bas) < 37:
                        bas = int(bas)
                        break
                    elif bas.isdigit() and int(bas) > 37:
                        print('Основание системы счисления не может превышать 36! ')
                        continue
                    elif bas.isdigit() and int(bas) < 2:
                        print('Основание системы счисления не может быть меньше 2! ')
                        continue
                    else:
                        print('А может быть все-таки введём целое число? ')
                        continue
                print(convert_to(num, num_bas, bas))
                restart()
                break
            elif choice == '2':
                print('Ниже будут представлены все возможные операции с числами различных систем счисления')
                print('Выберите необходимую вам ')
                print('1. Сравнение. Введите ">=<" ')
                print('2. Сложение. Введите "+" ')
                print('3. Вычитание. Введите "-" ')
                print('4. Умножение. Введите "*" ')
                print('5. Деление. Введите ":" ')
                print('6. Возведение в степень. Введите "**" ')
                print('7. Извлечения корня. Введите "√", для этого зажмите на клавишу Alt и, удерживая ее, ')
                print('наберите на цифровой клавиатуре 251 (поочередно, то есть сначала 2, затем 5 и, наконец, — 1)  ')
                print('8. Факториал. Введите "!" ')
                print('9. Процент от числа. Введите "%" ')
                print('10. Синус. Введите "sin" ')
                print('11. Косинус. Введите "cos" ')
                print('12. Тангенс. Введите "tg" ')
                print('13. Котангенс. Введите "ctg" ')
                print('14. Угол по синусу. Введите "sin ** -1" ')
                print('15. Угол по косинусу. Введите "cos ** -1" ')
                print('16. Угол по тангенсу. Введите "tg ** -1" ')
                print('17. Угол по котангенсу. Введите "ctg ** -1" ')
                print('18. Конвентатор единиц измерения плоских углов. Введите "convert" ')
                while True:
                    operation = input().strip().lower()
                    if operation == ">=<" or operation == "+" or operation == "-" or operation == "*" or \
                            operation == ":" or operation == "**" or operation == "√" or operation == "!" or \
                            operation == "%" or operation == "sin" or operation == "cos" or operation == "tg" or \
                            operation == "ctg" or operation == "sin ** -1" or operation == "cos ** -1" or\
                            operation == "tg ** -1" or operation == "ctg ** -1" or operation == "convert":
                        if operation == '>=<':
                            comparison()
                            break
                        elif operation == '+':
                            addition()
                            break
                        elif operation == '-':
                            subtraction()
                            break
                        elif operation == '*':
                            multiplication()
                            break
                        elif operation == ':':
                            division()
                            break
                        elif operation == '**':
                            degree()
                            break
                        elif operation == '√':
                            root()
                            break
                        elif operation == '!':
                            factorial()
                            break
                        elif operation == '%':
                            percent()
                            break
                        elif operation == 'sin':
                            sin()
                            break
                        elif operation == 'cos':
                            cos()
                            break
                        elif operation == 'tg':
                            tg()
                            break
                        elif operation == 'ctg':
                            ctg()
                            break
                        elif operation == 'sin ** -1':
                            reverse_sin()
                            break
                        elif operation == 'cos ** -1':
                            reverse_cos()
                            break
                        elif operation == 'tg ** -1':
                            reverse_tg()
                            break
                        elif operation == 'ctg ** -1':
                            reverse_ctg()
                            break
                        elif operation == "convert":
                            convert_corners()
                            break
                    else:
                        print('Я не понимаю. Введите желаемую операцию ')
                        continue
                restart()
                break
            else:
                print('Я не понимаю. Введите "1" или "2" ')
                continue

    def restart():
        while True:
            restart_ = input('Хотите задать ещё раз воспользоваться нашей программой? (Введите "да" или "нет"): ')
            if restart_.strip().lower() == 'да':
                questions()
            elif restart_.strip().lower() == 'нет':
                print('Возвращайся ещё, если понадобится работа с числами различных систем счисления !')
                print('Пока!')
                break
            else:
                print('Я не понимаю. Введите "да" или "нет" ')
                continue

    greeting()


num_systems()

