import random

def ex1(word):
    text = 'Мистер и миссис Дурсль проживали в доме номер четыре по Тисовой улице и всегда с гордостью заявляли, что они, слава богу, абсолютно нормальные люди. Уж от кого-кого, а от них никак нельзя было ожидать, чтобы они попали в какую-нибудь странную или загадочную ситуацию. Мистер и миссис Дурсль весьма неодобрительно относились к любым странностям, загадкам и прочей ерунде.'
    text = list(filter(lambda txt: word not in txt, text.split()))
    return ' '.join(text)

def camdyGame(mode):
    candyCount = 100
    candyMax = 28
    player = random.randint(1,2)
    if mode == 1:
        print('Режим игрок против игрока')
        playerVsPlayer(candyCount,candyMax,player)
    elif mode == 2:
        print('Режим игрок против бота')
        playerVsBot(candyCount,candyMax,player)
    else:
        print('Не правильный режим или дополнительный функции еще не реализованы')


def playerVsPlayer(candy,candyMax,player):
    candyCount = candy
    while candyCount > 0:
        print('Ходит игрок ', player)
        playerCount = int(input('Введите число: '))
        if (playerCount <= candyMax) and (playerCount <= candyCount):
            candyCount = candyCount - playerCount
            if candyCount == 0:
                print('Победил игрок', player)
            if player == 1:
                player = 2
            else:
                player = 1
        else:
            print('некорректный ход')
        print('Candy count', candyCount)

def playerVsBot(candy,candyMax,player):
    candyCount = candy
    while candyCount > 0:
        botCandysMax = candyMax
        if player == 1:
            print('Ходит игрок ', player)
            playerCount = int(input('Введите число: '))
        else:
            print('Ход бота: ')
            if botCandysMax > candyCount:
                botCandysMax = candyCount
                if candyCount < botCandysMax:
                    playerCount = candyCount
                else:
                    playerCount = random.randint(1,botCandysMax)
                print('Бот выбрал', playerCount)
            else: 
                playerCount = random.randint(1,botCandysMax)
        if (playerCount <= candyMax) and (playerCount <= candyCount):
            candyCount = candyCount - playerCount
            if candyCount == 0:
                print('Победил игрок', player)
            if player == 1:
                player = 2
            else:
                player = 1
        else:
            print('некорректный ход')
        print('Candy count', candyCount)


print('1. Напишите программу, удаляющую из текста все слова, содержащие " ".')
print(ex1('Мистер'))
print('2. Создайте программу для игры с конфетами человек против человека.')
print('Выберите режим игры:\n 1. Игра с человеком\n 2. Игра с ботом\n 3. Игра с интелектом')
print(camdyGame(1))

def fileWrite():
    path = 'coding.txt'
    data = open(path, 'a')
    open(path, 'w').close()
    text = input('Введите текст: ')
    data.write(str(text))
    data.close()


print(fileWrite())