
# метод для изображения игрового поля

def image_pole(pole):
       print ("-------------")
       for i in range(3):
           print ("|", str(pole[0+i*3]), "|", str(pole[1+i*3]), "|", str(pole[2+i*3]), "|")
           print ("-------------")

# метод для считывания инфо о ходе
def move_player(player_token):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
          player_answer = int(player_answer)
        except:
          print("Некорректный ввод. Вы уверены, что ввели число?")
          continue
        if player_answer >= 1 and player_answer <= 9:
           if(str(pole[player_answer-1]) not in "XO"):
              pole[player_answer-1] = player_token
              valid = True
           else:
                print("Эта клетка уже занята!")
        else:
         print("Некорректный ввод. Введите число от 1 до 9.")

# метод распознавания комбинаций выйгрыша
def vic_col(pole):
   coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for i in coord:
       if pole[i[0]] == pole[i[1]] == pole[i[2]]:
          return pole[i[0]]
   return False

print('"Это игра "Крестики-нолики". Играют два игрока. Первый ход определяет жребий. Первыми ставят "X"')
play = int(input('Играем?(если ДА- нажми 1, если НЕТ - 0):  '))
pole = list(range(1,10))
if play == 1:
    counter = 0
    win = False
    while not win:
        image_pole(pole)
        if counter % 2 == 0:
            move_player("X")
        else:
            move_player("O")
        counter += 1
        if counter > 4:
           tmp = vic_col(pole)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    image_pole(pole)
