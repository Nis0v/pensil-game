import string, random
Name1 = "John"
Name2 = "Jack"
pencil = "|"
msg_1 = "The number of pencils should be numeric"
msg_2 = "The number of pencils should be positive"
msg_3 = f"Choose between {Name1} and {Name2}"
msg_4 = "Possible values: '1', '2' or '3'"
msg_5 = "Too many pencils were taken"
number = input("How many pencils would you like to use:")
Activ = True
def bot_player(): ###Бот с которым будет играть игрок###
    ###Имя бота###
    global bot_name
    global number2
    global number
    global win_player
    ###Принятие решений###
    if number > 0:
        if number == 5:
            number2 = random.randint(1, 3)
            print(f"{bot_name}'s turn!\n{number2}")
            number = number - int(number2)
            print(pencil * number)
        elif number % 5 == 0:
            number2 = 2
            print(f"{bot_name}'s turn!\n{number2}")
            number = number - int(number2)
            print(pencil * number)
        elif number % 4 == 0:
            number2 = 3
            print(f"{bot_name}'s turn!\n{number2}")
            number = number - int(number2)
            print(pencil * number)
        elif number % 3 == 0:
            number2 = 2
            print(f"{bot_name}'s turn!\n{number2}")
            number = number - int(number2)
            print(pencil * number)
        elif number % 5 > 3:
            number2 = random.randint(1, 3)
            print(f"{bot_name}'s turn!\n{number2}")
            number = number - int(number2)
            print(pencil * number)
        elif number % 5 == 3:
            number2 = 3
            print(f"{bot_name}'s turn!\n{number2}")
            number = number - int(number2)
            print(pencil * number)
        elif number % 5 == 2:
            number2 = 2
            print(f"{bot_name}'s turn!\n{number2}")
            number = number - int(number2)
            print(pencil * number)
        else:
            number2 = 1
            print(f"{bot_name}'s turn!\n{number2}")
            number = number - int(number2)
            print(pencil * number)
        win_player = name
        return

###Проверка начального количества карандашей###

while Activ:
    if number.isnumeric() != True:
        number = input(msg_1)
        continue
    if number.isdigit() == False:
        number = input(msg_1)
    number = int(number)
    if number == 0:
        number = input(msg_2)
        ###Проверка имени###
    else:
        name = input(f"Who will be the first ({Name1}, {Name2}):")
        break
while number != 0:
    if name != Name1 and name != Name2:
        name = input(msg_3)
        continue
    ###Проверка числа введённого игроком###
    else:
        if name == Name1:
            bot_name = Name2
        else:
            bot_name = Name1
        print(pencil * number)
        break
while number != 0:
    number2 = input(f"{name}'s turn:")
    while number != 0:
        if number2.isnumeric() == True:
            number2 = int(number2)
            if number2 <= 3 and number2 >= 1:
                if number2 > number:
                    number2 = input(msg_5)
                else:
                    number = number - int(number2)
                    print(pencil * number)
                    win_player = bot_name
                    bot_player()
                    break
            else:
                number2 = input(msg_4)
            continue
        else:
            number2 = input(msg_4)
print(f"{win_player} win!")