import os
import random
import time

def tic_tac_toe():
    end = False
    global board
    game= True
    global chose
    while game == True:
        start()
        board = [1,2,3,4,5,6,7,8,9]
        print('Press P for play')
        print('Press L for Leaderboard')
        print('Quit = Anithing else')
        WhatToDo = input()
        if WhatToDo == "P" or WhatToDo == 'p' :
            os.system('clear')
            while True:
                chose = input("Do you want to play against AI or Player? (1/2)\n")
                if chose == '1' or chose == '2':
                    break
            while True:
                draw()
                #end=check_board()
                player_1()
                print()
                end=check_board()
                if end == True:
                    again = input('again? (y/n)\n')
                    if again == 'y' or again == 'Y':
                        break
                    else:
                        os.system('clear')
                        with open('leader_board.txt','r+') as L_Board:
                            print(L_Board.read())
                        game = False
                        break
                if chose == "1":
                    AI()
                    end=check_board()
                else:
                    player_2()
                    print()
                    end=check_board()
                if end == True:
                    again = input('again? (y/n)\n')
                    if again == 'y' or again == 'Y':
                        break
                    else:
                        os.system('clear')
                        with open('leader_board.txt','r+') as L_Board:
                            print(L_Board.read())
                        game = False
                        break
        elif WhatToDo == 'L'or WhatToDo == 'l':
            with open('leader_board.txt','r+') as L_Board:
                os.system('clear')
                print(L_Board.read())
                print()
                print('Press P for play')
                print('Quit = Anithing else')
                back = input()
                if back == 'P' or back == 'p':
                    continue
                else:
                    break
        else:
            game = False
            break
               

def draw():
    os.system('clear')
    print( board[0], "|", board[1], "|", board[2])
    print("---------")
    print( board[3], "|", board[4], "|", board[5])
    print("---------")
    print( board[6], "|", board[7], "|", board[8])
    print()

    return board


def chose_number():
    while True:
        a = input()
        try:
            a = int(a)
            a -= 1
            if a in range(0, 9):
                return a
            else:
                print("Do You like to stretch the limits?")
                continue
        except ValueError:
            print("That is not a number, FOOL")
            continue


def player_1():
    global board
    global n
    while True:
        print("Player 1 with X")
        n = chose_number()
        if board[n] == "X" or board[n] == "O":
            print("Defenetly Not OK")
            continue
        else: 
            board[n] = "X"
            draw()
            break
            return n


def AI():
    global board
    beef = ["You shall not pass", "Just give up",
            "THIS is the best I can do. This is what I've been waiting for. All of you against all of me!",
            "Hasta la vista, baby",
            "Humph. Hope, it is the quintessential human delusion, simultaneously the source of your greatest strength, and your greatest weakness.", 
            "Hmm, Mr. Anderson. You disappoint me.",
            "You're not a scientist! You're not a doctor! YOU'RE NOT EVEN A FULL-TIME EMPLOYEE!", 
            "No one User wrote me! I'm worth millions of their man-years!","August 29th: Skynet Becomes Self-aware"]
    while True:
        n =random.randrange(0,9)
        if board[n] == "X" or board[n] == "O":
            continue
        else: 
            board[n] = "O"
            draw()
            print(beef[n])
            time.sleep(2)
            break


def AI_2():
    global board
    while True:
        try:
            if board[n+1] == 'X' or board[n+1] == 'O':
                pass
            else:
                board[n+1] = 'O'
                break

            if board[n+2] == 'X' or board[n+2] == 'O':
                pass
            else:
                board[n+2] = 'O'
                break

            if board[n+3] == 'X' or board[n+3] == 'O':
                pass
            else:
                board[n+3] = 'O'

            if board[n+4] == 'X' or board[n+4] == 'O':
                pass
            else:
                board[n+4] = 'O'
                break

            if board[n+5] == 'X' or board[n+5] == 'O':
                pass
            else:
                board[n+5] = 'O'
                break

            if board[n+6] == 'X' or board[n+6] == 'O':
                pass
            else:
                board[n+6] = 'O'
                break

            if board[n+7] == 'X' or board[n+7] == 'O':
                pass
            else:
                board[n+7] = 'O'
                break

            if board[n+8] == 'X' or board[n+8] == 'O':
                pass
            else:
                board[n+8] = 'O'
                break
        except IndexError:
            if board[n-1] == 'X' or board[n-1] == 'O':
                pass
            else:
                board[n-1] = 'O'
                break

            if board[n-2] == 'X' or board[n-2] == 'O':
                pass
            else:
                board[n-2] = 'O'
                break

            if board[n-3] == 'X' or board[n-3] == 'O':
                pass
            else:
                board[n-3] = 'O'
                break

            if board[n-4] == 'X' or board[n-4] == 'O':
                pass
            else:
                board[n-4] = 'O'
                break

            if board[n-5] == 'X' or board[n-5] == 'O':
                pass
            else:
                board[n-5] = 'O'
                break

            if board[n-6] == 'X' or board[n-6] == 'O':
                pass
            else:
                board[n-6] = 'O'
                break

            if board[n-7] == 'X' or board[n-7] == 'O':
                pass
            else:
                board[n-7] = 'O'
                break

            if board[n-8] == 'X' or board[n-8] == 'O':
                pass
            else:
                board[n-8] = 'O'
                break


def player_2():
    global board
    while True:
        print("Player 2 with O")
        n = chose_number()
        if board[n] == "X" or board[n] == "O":
            print("Defenetly Not OK")
            continue
        else: 
            board[n] = "O"
            draw()
            break


def check_board():
    win_combination = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    count = 0
    for a in win_combination:
        if board[a[0]] == board[a[1]] == board[a[2]] == "X":
            print("X wins this game!")
            with open('leader_board.txt', 'a+') as L_Board:
                L_Board.write(input('What is your name?\n')+' won with X '+time.strftime("%Y-%m-%d-%H:%M:%S")+'\n')
            print("can you do that again?")
            return True
        if board[a[0]] == board[a[1]] == board[a[2]] == "O":
            print("O wins this game!")
            if chose == '2':
                with open('leader_board.txt', 'a+') as L_Board:
                    L_Board.write(input('What is your name?\n')+' won with O '+time.strftime("%Y-%m-%d-%H:%M:%S")+'\n')
            elif chose == '1':
                with open('leader_board.txt', 'a+') as L_Board:
                    L_Board.write('AI'+' won with O '+time.strftime("%Y-%m-%d-%H:%M:%S")+'\n')
            print("can you do that again?")

            return True
    for a in range(0,9):
        if board[a] == "X" or board[a] == "O":
            count+= 1
        if count == 9:
            print("This game is a tie")
            print("We have to solve this problem")
            return True


def start():
    os.system('clear')
    print()
    print()
    print("                                                              /x//o//x//o//x///")
    print("                                                              //x//o//x//o//x//")
    print("                                                              ///x//o//x//o//x/")
    print("////////////                //////////////                    ////x//o//x//o//x")
    print("    ///     ///     //////        ///       //////       ///////     /ox/  ///    ///       //////     /////////")
    print("    ///     ///   ///             ///      ///  ///    ///           /ox/  ///    ///    ///     ///   ///     ///")
    print("    ///     ///  ///              ///     ///    ///  ///            /ox/  //////////   ///       ///  ///    ///")
    print("    ///     ///  ///              ///    //////////// ///            /ox/  ///    ///   ///       ///  /////////")
    print("    ///     ///  ///              ///   ///        /// ///           /ox/  ///    ///    ///     ///   ///     ///")
    print("    ///     ///   ////////        ///  ///          //// ///////     /ox/  ///    ///      //////      ///      ///")
    print()
    print()
       

tic_tac_toe()