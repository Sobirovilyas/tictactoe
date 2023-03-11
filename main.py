import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


bot = telebot.TeleBot("6225924693:AAECgdNQdkn54zhCXaAYEJpoIOvyXZHSp0U")



# Let's start by initializing our game board
board = [[KeyboardButton("1"), KeyboardButton("2"), KeyboardButton("3")],
         [KeyboardButton("4"), KeyboardButton("5"), KeyboardButton("6")],
         [KeyboardButton("7"),KeyboardButton("8"), KeyboardButton("9")]]


game_on = True

# Initialize our current player to be X
current_player = "X"


# Function to display our game board
def display_board():
    keybaord = ReplyKeyboardMarkup(resize_keyboard=True)
    for i in range(3):
        keybaord.add(*board[i])
    return keybaord


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "hi i'm quality well bot tictactoe", reply_markup = display_board())
    bot.reply_to(message, "you select X OR O", reply_markup=display_board())
    bot.reply_to(message, "My Tic Tac Toe Game -  | - | -     1|2|3 \n  - | - | -  \    4|5|6 \n- | - | -      7|8|9 \n ", reply_markup=display_board())





# Funtion to define players
def players():
    print("Select Player - X or O")
    p1 = input("Player1: ")
    p2 = ""
    if p1 == "X":
        p2 = "O"
        print("Player2: " + p2)
    elif p1 == "O":
        p2 = "X"
        print("Player2: " + p2)
    elif p1 != "O" or p1 != "X":
        print("Sorry,invalid input. Type X or O")
        play_game()


# Define the player position
def player_position():
    global current_player
    print("Current Player: " + current_player)
    position = input("Choose position from 1 - 9: ")

    # Loop through the program untill there is a win or tie
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose position from 1 - 9: ")
        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("Position already selected, choose another position!")
    board[position] = current_player
    display_board()


# Function to play our tic tac game
def play_game():
    print("My Tic Tac Toe Game")
    display_board()
    players()

    # loop  to flip players untill there is a win
    while game_on:
        player_position()

        # Check winner
        def check_winner():
            global game_on
            # Check rows if there is a win
            if board[0].text == board[1].text == board[2].text != "-":
                game_on = False
                print("Congratulations " + board[0].text + " you WON!")
            elif board[3].text == board[4].text == board[5].text != "-":
                game_on = False
                print("Congratulations " + board[3].text + " you WON!")
            elif board[6].text == board[7].text == board[8].text != "-":
                game_on = False
                print("Congratulations " + board[6].text + " you WON!")
            # Check columns if there is a win
            elif board[0].text == board[3].text == board[6].text != "-":
                game_on = False
                print("Congratulations " + board[0].text + " you WON!")
            elif board[1].text == board[4].text == board[7].text != "-":
                game_on = False
                print("Congratulations " + board[1].text + " you WON!")
            elif board[2].text == board[5].text == board[8].text != "-":
                game_on = False
                print("Congratulations " + board[2].text + " you WON!")
            # Check diagonals if there is a win
            elif board[0].text == board[4].text == board[8].text != "-":
                game_on = False
                print("Congratulations " + board[0].text + " you WON!")
            elif board[2].text == board[4].text == board[6].text != "-":
                game_on = False
                print("Congratulations " + board[6].text + " you WON!")
            # If none of the above, then, it's a tie
            elif "-" not in board:
                game_on = False
                print("It's a Tie")
                exit()


        def flip_player():
            global current_player
            if current_player == "X":
                current_player = "O"
            else:
                current_player = "X"

        flip_player()
        check_winner()


bot.infinity_polling()

