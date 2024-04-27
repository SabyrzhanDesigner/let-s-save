############## меню пиццы
class Pizza:

    def __init__(self,pep, bar, dar, exit):
        self.pep = pep
        self.bar = bar
        self.dar = dar
        self.exit = exit

class Cook(Pizza):
    ch_pep = '(пряные колбаски с легкой перчинкой,сыр моцарелла со сливочным вкусом и нежный томатный соус.)'
    ch_bar = '(пицца с охотничьими колбасками, ветчиной, грибами, маринованными огурцами)'
    ch_dar = '(хрустящее тесто, красный соус, маслины, красная рыба, брокколи, креветки, сыр моцарелла.)'


    def __int__(self):
        self.ch_pep = ('Пряные колбаски с легкой перчинкой,сыр моцарелла со сливочным вкусом и нежный томатный соус.')

        self.bar = ('пицца с охотничьими колбасками, ветчиной, грибами, маринованными огурцами')

        self.dar = ('Хрустящее тесто, красный соус, маслины, красная рыба, брокколи, креветки, сыр моцарелла.')
class Menu(Cook, Pizza):

    def menu(self):
        print('*' * 4, 'Меню пиццы:', '*' * 4)

        print(f'{self.pep} Пепперони  - 2500 тг \n {self.ch_pep}')
        print(f' \n{self.bar} Барбекю - 3500 тг \n {self.ch_bar}')
        print(f' \n{self.dar} Дары моря - 4000 тг \n {self.ch_dar}')
        print(f'\n  {self.exit} Отмена заказа')
        print('*' * 22)


class Payment(Menu):
    client = 'Клиент'
    cost = int()



    def __int__(self, client, cost):
        self.client = client
        self.cost = cost




    def pizza_choice(self):
        self.client = int(input('Ваш выбор: '))
        print('*' * 22)

        if self.client == 1:
            print(f'Ваш выбор:{self.pep} ')
            print('Ваш заказ принят!')
            print('*' * 22)

            print("Выберите способ оплаты? ")
            print('[1] Наличными')
            print('[2] Переводом')
            print('[3] Картой')
            print('*' * 22)

            self.client = int(input('Выбор оплаты: '))

            if self.client == int(2):
                print('Номер для перевода оплаты заказа: +7(775)990-06-91')
                print("Ваша оплата принята! Ожидайте заказа 15-20 минут")
                print('*' * 22)

            elif self.client == int(3):
                print('Приложите Вашу карту к терминалу!')
                print("Ваша оплата принята! Ожидайте заказа 15-20 минут")
            elif self.client == int(1):
                self.cost = (int(input('Ваша оплата: ')))
                print('*' * 22)

                if self.cost == int(2500):
                    print("Ваша оплата принята! Ожидайте заказа 15-20 минут")
                    print('*' * 22)

                elif self.cost > int(2500):
                    print("Ваша оплата принята! Ожидайте заказа 15-20 минут")
                    print("Ваша сдача:", self.cost - int(2500), "тг")
                    print('*' * 22)

                else:
                    print("Извините, у вас не хватает денег!")
                    print('*' * 22)

        if self.client == 2:
            print(f'Ваш выбор:{self.bar} ')
            print('Ваш заказ принят!')
            print('*' * 22)

            print("Выберите способ оплаты? ")
            print('[1] Наличными')
            print('[2] Переводом')
            print('[3] Картой')
            print('*' * 22)

            self.client = int(input('Выбор оплаты: '))

            if self.client == int(2):
                print('Номер для перевода оплаты заказа: +7(775)990-06-91')
                print("Ваша оплата принята! Ожидайте заказа 15-20 минут")
                print('*' * 22)

            elif self.client == int(3):
                print('Приложите Вашу карту к терминалу!')
                print("Ваша оплата принята! Ожидайте заказа 15-20 минут")
            elif self.client == int(1):
                self.cost = (int(input('Ваша оплата: ')))
                print('*' * 22)

                if self.cost == int(3500):
                    print("Ваша оплата принята! Ожидайте заказа 15-20 минут")
                    print('*' * 22)

                elif self.cost > int(3500):
                    print("Ваша оплата принята! Ожидайте заказа 15-20 минут")
                    print("Ваша сдача:", self.cost - int(3500), "тг")
                    print('*' * 22)

                else:
                    print("Извините, у вас не хватает денег!")
                    print('*' * 22)

        if self.client == 3:
            print(f'Ваш выбор:{self.dar} ')
            print('Ваш заказ принят!')
            print('*' * 22)

            print("Выберите способ оплаты? ")
            print('[1] Наличными')
            print('[2] Переводом')
            print('[3] Картой')
            print('*' * 22)

            self.client = int(input('Выбор оплаты: '))

            if self.client == int(2):
                print('Номер для перевода оплаты заказа: +7(775)990-06-91')
                print("Ваша оплата принята! Ожидайте заказа 15-20 минут")
                print('*' * 22)

            elif self.client == int(3):
                print('Приложите Вашу карту к терминалу!')
                print("Ваша оплата принята! Ожидайте заказа 15-20 минут")
            elif self.client == int(1):
                self.cost = (int(input('Ваша оплата: ')))
                print('*' * 22)

                if self.cost == int(4000):
                    print("Ваша оплата принята! Ожидайте заказа 15-20 минут")
                    print('*' * 22)

                elif self.cost > int(4000):
                    print("Ваша оплата принята! Ожидайте заказа 15-20 минут")
                    print("Ваша сдача:", self.cost - int(4000), "тг")
                    print('*' * 22)

                else:
                    print("Извините, у вас не хватает денег!")
                    print('*' * 22)

            else:
                print("Некорректный ввод!")


c1 = Menu("1", "2", "3", "0", )
c2 = Payment("Пепперони", "Барбекю", "Дары моря", "Выход")
c3 = Cook("Пепперони", "Барбекю", "Дары моря", "Выход")
c1.menu()
c2.pizza_choice()
print('Ваш заказ готов! Приятного аппетита!')


####### Камень, ножницы, бумага

import random

print('-' * 5, 'Камень, Ножницы, Бумага', '-' * 5)
print('-' * 8, 'Добро пожаловать!', '-' * 8)

possible_actions = ["камень", "бумага", "ножницы"]
gamer = 'Игрок'
print('Привет, игрок! Вы играете с ботом!')

name = input('Ваше имя? ').upper()
if name == "":
    name = gamer

player_wins = 0
computer_wins = 0

wants_to_play = True
turns = 0

while wants_to_play:
    computer_action = random.choice(possible_actions)
    player_action = input(f'{name}, "камень",  "ножницы", "бумага или "выход"? ').lower()
    while  (player_action != 'камень' and player_action != 'ножницы' and
           player_action != 'бумага' and player_action != 'выход'):
            print(f'"{player_action}" - не корректное действие')
            player_action = input(f'{name}, "камень",  "ножницы", "бумага или "выход"? ').lower()

    if player_action == 'выход':
        wants_to_play = False
        print('До свидания!')

    else:
        turns += 1
        print(f'{name} выбрал \"{player_action}\", бот выбрал \"{computer_action}\"')

        if player_action == computer_action:
            print('Ничья!')
        elif ((player_action == 'камень' and computer_action == 'ножницы') or (player_action == 'ножницы'
              and computer_action == 'бумага') or (player_action == 'бумага' and computer_action == 'камень')):
            print(f'{name} выиграл!')
            player_wins += 1
        else:
            print('Бот выиграл!')
            computer_wins += 1

        print(f' Раунд: {turns}, {name}: {player_wins}, Бот: {computer_wins}')


        if turns == 3:
            player_answer = input(f'{name}, Поиграем еще раз? ')

            if player_answer == 'Да'.lower():
                player_action = input(f'{name}, камень, ножницы, бумага или выход? ').lower()
            elif player_answer == 'Нет'.lower():
                wants_to_play = False
                print(f'Хорошо! Я буду тебя ждать, {name}')

            elif player_answer != 'Да'.lower() and player_answer != 'Нет'.lower():
                print("Некорректный ответ!")
                print(f' Раунд: {turns}, {name}: {player_wins}, Бот: {computer_wins}')

