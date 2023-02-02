import random
print('"Это игра "Крестики-нолики". Играют два игрока. Первый ход определяет жребий. Первыми ставят "X"')
play = int(input('Играем?(если ДА- нажми 1, если НЕТ - 0):  '))
pole = list(range(1,10))
play_simbol = [ 'x', '0']
def image_pole(pole):
       print ("-------------")
       for i in range(3):
           print ("|", str(pole[0+i*3]), "|", str(pole[1+i*3]), "|", str(pole[2+i*3]), "|")
           print ("-------------")
if play == 1:

  
   
   image_pole(pole)
   number_human = [1, 2]
   random.shuffle(number_human)
   play_simbol = [ 'x', 0]
   print(f'Жеребьевка закончена. Сейчас ход игрока № {number_human[0]}')
   player_hod = int(input('Введи номер позиции:  '))
   while 0 < player_hod > 10:
       print(f'Ход игрока № {number_human[0]}')
       player_hod = int(input('Введи номер позиции:  '))
       if str(pole[player_hod -1])  not in 'x0':
          pole[player_hod - 1] = play_simbol[0]
          image_pole(pole)
          temp = number_human[0]
          number_human[0] = number_human[1]
          number_human[1] = temp
          temp = play_simbol[0]
          play_simbol[0] = play_simbol[1]
          play_simbol[1] = temp
       else:
            print('Эта клетка занята')
       
   print("*" * 10, " Игра Крестики-нолики для двух игроков ", "*" * 10)

board = list(range(1,10))

def draw_board(board):
   print("-" * 13)
   for i in range(3):
      print("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
      print("-" * 13)

def take_input(player_token):
   valid = False
   while not valid:
      player_answer = input("Куда поставим " + player_token+"? ")
      try:
         player_answer = int(player_answer)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if player_answer >= 1 and player_answer <= 9:
         if(str(board[player_answer-1]) not in "XO"):
            board[player_answer-1] = player_token
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(board):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if board[each[0]] == board[each[1]] == board[each[2]]:
          return board[each[0]]
   return False

def main(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(board)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    draw_board(board)
main(board)

input("Нажмите Enter для выхода!")