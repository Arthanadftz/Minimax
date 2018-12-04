from tic_tac_toe import *


def play(my_board):
  player = input("Chose your mark 'X' or 'O': ")
  player = player.upper()
  print("Your choise is: '%s'" %(player))
  while not game_is_over(my_board):
    if player == 'X':
      move = int(input("Enter number from: %s" %(available_moves(my_board))))
      select_space(my_board, move, player)
      print_board(my_board)
      if not game_is_over(my_board):
        select_space(my_board, minimax(my_board, False)[1], 'O')
        print_board(my_board)  
    elif player == 'O':
      move = int(input("Enter number from: %s" %(available_moves(my_board))))
      select_space(my_board, move, "O")
      print_board(my_board)
      if not game_is_over(my_board):
        select_space(my_board, minimax(my_board, True)[1], 'X')
        print_board(my_board)
    else:
      print('Aww.. You have entered invalid input. Try again...')
      play(my_board) 
  if game_is_over(my_board):
    print('Game Over!')
  if has_won(my_board, player):
    print('%s haw won! Congratz!' %(player))
  elif not available_moves(my_board):
    print("It's a tie!")
  else:
    print('Unfortunately you lose:(')


def ai_play(my_board):
  while not game_is_over(my_board):
    select_space(my_board, minimax(my_board, True)[1], "X")
    print_board(my_board)
    if not game_is_over(my_board):
      select_space(my_board, minimax(my_board, False)[1], "O")
      print_board(my_board)
  

def menu():
  print("Let's play Tic-Tac-Toe!?")
  my_board = [
  ["1", "2", "3"],
  ["4", "5", "6"],
  ["7", "8", "9"]
  ]

  print_board(my_board)

  print("Do you want to play vs AI or just watch on it's perfomance?\n [1] - Play vs AI.\n [2] - Watch the AI battle.\n [3] - Exit.")
  response = int(input('Chose from the list: '))

  if response == 1:
    play(my_board)
    menu()
  elif response == 2:
    ai_play(my_board)
    menu()
  elif response == 3:
    print("Cya!")
    return
  else:
    print('Your choice is invalid. Try again.')
    menu()

menu() 