#Реализовать функцию, принимающую два числа(позиционные аргументы) и выполняющую их деление.
#Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

while True:
        control = input("For quit press 'q', for continue press 'Enter' ").upper()
        if control == 'Q':
                break
        else:
                def division(num,den):
                        try:
                                res = num / den
                                return res
                        except ZeroDivisionError:
                                print ("Division by zero is not possible")
                        except ValueError:
                                print ('Enter only number')

                print(division(int(input('Enter numerator: ')), int(input('Enter denominator: '))))


