#Using the X-Ray Board_B
#Prints the current layout of the board
def draw_board(board_L = [[12, 12, 12], [12, 12, 12], [12, 12, 12]], board_B = [[12, 12, 12], [12, 12, 12], [12, 12, 12]], is_player: bool = True):
    for x in range(len(board_L)):
        for w in range(len(board_L[x])):
            while board_L[x][w] > 12:
                board_L[x][w] -= 12
            while board_L[x][w] <= 0:
                board_L[x][w] += 12
            while board_B[x][w] > 12:
                board_B[x][w] -= 12
            while board_B[x][w] <= 0:
                board_B[x][w] += 12
    if is_player:
        for i in range(len(board_L)):
            print("{0:<2} {1:<2} {2:<2} | {3:<2} {4:<2} {5:<2}".format(board_L[i][0], board_L[i][1], board_L[i][2], board_B[i][0], board_B[i][1], board_B[i][2]))
        print()

def make_move(move: str, board_L = [[12, 12, 12], [12, 12, 12], [12, 12, 12]], board_B = [[12, 12, 12], [12, 12, 12], [12, 12, 12]]):
    if move == "A" or move == "a":
        for i in range(len(board_L)):
            for x in range(len(board_L[i])):
                board_L[i][x] += 1
        board_B[0][0] -= 1
        board_B[0][2] -= 1
        board_B[2][0] -= 1
        board_B[2][2] -= 1
        return board_L, board_B
    elif move == "BX" or move == "b":
        for i in range(len(board_L)):
            for x in range(len(board_L[i])):
                if not(i == 0 and x == 0):#Maybe fix this logic. Should be excluding only the first column of the first row
                    board_L[i][x] += 1
        board_B[0][2] -= 1
        board_B[2][0] -= 1
        board_B[2][2] -= 1
        return board_L, board_B
    elif move == "BO" or move == "c":
        board_L[0][0] += 1
        board_B[0][0] -= 1
        board_B[0][1] -= 1
        board_B[1][0] -= 1
        board_B[1][1] -= 1
        return board_L, board_B
    elif move == "CX" or move == "d":
        for i in range(len(board_L)):
            for x in range(len(board_L[i])):
                if not(i == 0 and x == 2):#Maybe fix this logic. Should be excluding only the first column of the first row
                    board_L[i][x] += 1
        board_B[0][0] -= 1
        board_B[2][0] -= 1
        board_B[2][2] -= 1
        return board_L, board_B
    elif move == "CO" or move == "e":
        board_L[0][2] += 1
        board_B[0][1] -= 1
        board_B[0][2] -= 1
        board_B[1][1] -= 1
        board_B[1][2] -= 1
        return board_L, board_B
    elif move == "DX" or move == "f":
        for i in range(len(board_L)):
            for x in range(len(board_L[i])):
                if not(i == 2 and x == 0):#Maybe fix this logic. Should be excluding only the first column of the first row
                    board_L[i][x] += 1
        board_B[0][0] -= 1
        board_B[0][2] -= 1
        board_B[2][2] -= 1
        return board_L, board_B
    elif move == "DO" or move == "g":
        board_L[2][0] += 1
        board_B[1][0] -= 1
        board_B[1][1] -= 1
        board_B[2][0] -= 1
        board_B[2][1] -= 1
        return board_L, board_B
    elif move == "EX" or move == "h":
        for i in range(len(board_L)):
            for x in range(len(board_L[i])):
                if not(i == 2 and x == 2):#Maybe fix this logic. Should be excluding only the first column of the first row
                    board_L[i][x] += 1
        board_B[0][0] -= 1
        board_B[0][2] -= 1
        board_B[2][0] -= 1
        return board_L, board_B
    elif move == "EO" or move == "i":
        board_L[2][2] += 1
        board_B[1][1] -= 1
        board_B[1][2] -= 1
        board_B[2][1] -= 1
        board_B[2][2] -= 1
        return board_L, board_B
    elif move == "FX" or move == "j":
        board_L[0][0] += 1
        board_L[0][1] += 1
        board_L[0][2] += 1
        board_L[1][0] += 1
        board_L[1][1] += 1
        board_L[1][2] += 1
        board_B[0][0] -= 1
        board_B[0][2] -= 1
        return board_L, board_B
    elif move == "FO" or move == "k":
        board_L[2][0] += 1
        board_L[2][2] += 1
        board_B[1][0] -= 1
        board_B[1][1] -= 1
        board_B[1][2] -= 1
        board_B[2][0] -= 1
        board_B[2][1] -= 1
        board_B[2][2] -= 1
        return board_L, board_B
    elif move == "GX" or move == "l":
        board_L[0][1] += 1
        board_L[0][2] += 1
        board_L[1][1] += 1
        board_L[1][2] += 1
        board_L[2][1] += 1
        board_L[2][2] += 1
        board_B[0][2] -= 1
        board_B[2][2] -= 1
        return board_L, board_B
    elif move == "GO" or move == "m":
        board_L[0][0] += 1
        board_L[2][0] += 1
        board_B[0][0] -= 1
        board_B[0][1] -= 1
        board_B[1][0] -= 1
        board_B[1][1] -= 1
        board_B[2][0] -= 1
        board_B[2][1] -= 1
        return board_L, board_B




    elif move == "A'" or move == "n":
        for i in range(len(board_B)):
            for x in range(len(board_B[i])):
                board_B[i][x] -= 1
        board_L[0][0] += 1
        board_L[0][2] += 1
        board_L[2][0] += 1
        board_L[2][2] += 1
        return board_L, board_B
    elif move == "BX'" or move == "o":
        for i in range(len(board_B)):
            for x in range(len(board_B[i])):
                if not(i == 0 and x == 0):#Maybe fix this logic. Should be excluding only the first column of the first row
                    board_B[i][x] -= 1
        board_L[0][2] += 1
        board_L[2][0] += 1
        board_L[2][2] += 1
        return board_L, board_B
    elif move == "BO'" or move == "p":
        board_B[0][0] -= 1
        board_L[0][0] += 1
        board_L[0][1] += 1
        board_L[1][0] += 1
        board_L[1][1] += 1
        return board_L, board_B
    elif move == "CX'" or move == "q":
        for i in range(len(board_B)):
            for x in range(len(board_B[i])):
                if not(i == 0 and x == 2):#Maybe fix this logic. Should be excluding only the first column of the first row
                    board_B[i][x] -= 1
        board_L[0][0] += 1
        board_L[2][0] += 1
        board_L[2][2] += 1
        return board_L, board_B
    elif move == "CO'" or move == "r":
        board_B[0][2] -= 1
        board_L[0][1] += 1
        board_L[0][2] += 1
        board_L[1][1] += 1
        board_L[1][2] += 1
        return board_L, board_B
    elif move == "DX'" or move == "s":
        for i in range(len(board_B)):
            for x in range(len(board_B[i])):
                if not(i == 2 and x == 0):#Maybe fix this logic. Should be excluding only the first column of the first row
                    board_B[i][x] -= 1
        board_L[0][0] += 1
        board_L[0][2] += 1
        board_L[2][2] += 1
        return board_L, board_B
    elif move == "DO'" or move == "t":
        board_B[2][0] -= 1
        board_L[1][0] += 1
        board_L[1][1] += 1
        board_L[2][0] += 1
        board_L[2][1] += 1
        return board_L, board_B
    elif move == "EX'" or move == "u":
        for i in range(len(board_B)):
            for x in range(len(board_B[i])):
                if not(i == 2 and x == 2):#Maybe fix this logic. Should be excluding only the first column of the first row
                    board_B[i][x] -= 1
        board_L[0][0] += 1
        board_L[0][2] += 1
        board_L[2][0] += 1
        return board_L, board_B
    elif move == "EO'" or move == "v":
        board_B[2][2] -= 1
        board_L[1][1] += 1
        board_L[1][2] += 1
        board_L[2][1] += 1
        board_L[2][2] += 1
        return board_L, board_B
    elif move == "FX'" or move == "w":
        board_B[0][0] -= 1
        board_B[0][1] -= 1
        board_B[0][2] -= 1
        board_B[1][0] -= 1
        board_B[1][1] -= 1
        board_B[1][2] -= 1
        board_L[0][0] += 1
        board_L[0][2] += 1
        return board_L, board_B
    elif move == "FO'" or move == "x":
        board_B[2][0] -= 1
        board_B[2][2] -= 1
        board_L[1][0] += 1
        board_L[1][1] += 1
        board_L[1][2] += 1
        board_L[2][0] += 1
        board_L[2][1] += 1
        board_L[2][2] += 1
        return board_L, board_B
    elif move == "GX'" or move == "y":
        board_B[0][1] -= 1
        board_B[0][2] -= 1
        board_B[1][1] -= 1
        board_B[1][2] -= 1
        board_B[2][1] -= 1
        board_B[2][2] -= 1
        board_L[0][2] += 1
        board_L[2][2] += 1
        return board_L, board_B
    elif move == "GO'" or move == "z":
        board_B[0][0] -= 1
        board_B[2][0] -= 1
        board_L[0][0] += 1
        board_L[0][1] += 1
        board_L[1][0] += 1
        board_L[1][1] += 1
        board_L[2][0] += 1
        board_L[2][1] += 1
        return board_L, board_B











    
    elif move == "-A" or move == "-a":
        for i in range(len(board_L)):
            for x in range(len(board_L[i])):
                board_L[i][x] -= 1
        board_B[0][0] += 1
        board_B[0][2] += 1
        board_B[2][0] += 1
        board_B[2][2] += 1
        return board_L, board_B
    elif move == "-BX" or move == "-b":
        for i in range(len(board_L)):
            for x in range(len(board_L[i])):
                if not(i == 0 and x == 0):#Maybe fix this logic. Should be excluding only the first column of the first row
                    board_L[i][x] -= 1
        board_B[0][2] += 1
        board_B[2][0] += 1
        board_B[2][2] += 1
        return board_L, board_B
    elif move == "-BO" or move == "-c":
        board_L[0][0] -= 1
        board_B[0][0] += 1
        board_B[0][1] += 1
        board_B[1][0] += 1
        board_B[1][1] += 1
        return board_L, board_B
    elif move == "-CX" or move == "-d":
        for i in range(len(board_L)):
            for x in range(len(board_L[i])):
                if not(i == 0 and x == 2):#Maybe fix this logic. Should be excluding only the first column of the first row
                    board_L[i][x] -= 1
        board_B[0][0] += 1
        board_B[2][0] += 1
        board_B[2][2] += 1
        return board_L, board_B
    elif move == "-CO" or move == "-e":
        board_L[0][2] -= 1
        board_B[0][1] += 1
        board_B[0][2] += 1
        board_B[1][1] += 1
        board_B[1][2] += 1
        return board_L, board_B
    elif move == "-DX" or move == "-f":
        for i in range(len(board_L)):
            for x in range(len(board_L[i])):
                if not(i == 2 and x == 0):#Maybe fix this logic. Should be excluding only the first column of the first row
                    board_L[i][x] -= 1
        board_B[0][0] += 1
        board_B[0][2] += 1
        board_B[2][2] += 1
        return board_L, board_B
    elif move == "-DO" or move == "-g":
        board_L[2][0] -= 1
        board_B[1][0] += 1
        board_B[1][1] += 1
        board_B[2][0] += 1
        board_B[2][1] += 1
        return board_L, board_B
    elif move == "-EX" or move == "-h":
        for i in range(len(board_L)):
            for x in range(len(board_L[i])):
                if not(i == 2 and x == 2):#Maybe fix this logic. Should be excluding only the first column of the first row
                    board_L[i][x] -= 1
        board_B[0][0] += 1
        board_B[0][2] += 1
        board_B[2][0] += 1
        return board_L, board_B
    elif move == "-EO" or move == "-i":
        board_L[2][2] -= 1
        board_B[1][1] += 1
        board_B[1][2] += 1
        board_B[2][1] += 1
        board_B[2][2] += 1
        return board_L, board_B
    elif move == "-FX" or move == "-j":
        board_L[0][0] -= 1
        board_L[0][1] -= 1
        board_L[0][2] -= 1
        board_L[1][0] -= 1
        board_L[1][1] -= 1
        board_L[1][2] -= 1
        board_B[0][0] += 1
        board_B[0][2] += 1
        return board_L, board_B
    elif move == "-FO" or move == "-k":
        board_L[2][0] -= 1
        board_L[2][2] -= 1
        board_B[1][0] += 1
        board_B[1][1] += 1
        board_B[1][2] += 1
        board_B[2][0] += 1
        board_B[2][1] += 1
        board_B[2][2] += 1
        return board_L, board_B
    elif move == "-GX" or move == "-l":
        board_L[0][1] -= 1
        board_L[0][2] -= 1
        board_L[1][1] -= 1
        board_L[1][2] -= 1
        board_L[2][1] -= 1
        board_L[2][2] -= 1
        board_B[0][2] += 1
        board_B[2][2] += 1
        return board_L, board_B
    elif move == "-GO" or move == "-m":
        board_L[0][0] -= 1
        board_L[2][0] -= 1
        board_B[0][0] += 1
        board_B[0][1] += 1
        board_B[1][0] += 1
        board_B[1][1] += 1
        board_B[2][0] += 1
        board_B[2][1] += 1
        return board_L, board_B




    elif move == "-A'" or move == "-n":
        for i in range(len(board_B)):
            for x in range(len(board_B[i])):
                board_B[i][x] += 1
        board_L[0][0] -= 1
        board_L[0][2] -= 1
        board_L[2][0] -= 1
        board_L[2][2] -= 1
        return board_L, board_B
    elif move == "-BX'" or move == "-o":
        for i in range(len(board_B)):
            for x in range(len(board_B[i])):
                if not(i == 0 and x == 0):#Maybe fix this logic. Should be excluding only the first column of the first row
                    board_B[i][x] += 1
        board_L[0][2] -= 1
        board_L[2][0] -= 1
        board_L[2][2] -= 1
        return board_L, board_B
    elif move == "-BO'" or move == "-p":
        board_B[0][0] += 1
        board_L[0][0] -= 1
        board_L[0][1] -= 1
        board_L[1][0] -= 1
        board_L[1][1] -= 1
        return board_L, board_B
    elif move == "-CX'" or move == "-q":
        for i in range(len(board_B)):
            for x in range(len(board_B[i])):
                if not(i == 0 and x == 2):#Maybe fix this logic. Should be excluding only the first column of the first row
                    board_B[i][x] += 1
        board_L[0][0] -= 1
        board_L[2][0] -= 1
        board_L[2][2] -= 1
        return board_L, board_B
    elif move == "-CO'" or move == "-r":
        board_B[0][2] += 1
        board_L[0][1] -= 1
        board_L[0][2] -= 1
        board_L[1][1] -= 1
        board_L[1][2] -= 1
        return board_L, board_B
    elif move == "-DX'" or move == "-s":
        for i in range(len(board_B)):
            for x in range(len(board_B[i])):
                if not(i == 2 and x == 0):#Maybe fix this logic. Should be excluding only the first column of the first row
                    board_B[i][x] += 1
        board_L[0][0] -= 1
        board_L[0][2] -= 1
        board_L[2][2] -= 1
        return board_L, board_B
    elif move == "-DO'" or move == "-t":
        board_B[2][0] += 1
        board_L[1][0] -= 1
        board_L[1][1] -= 1
        board_L[2][0] -= 1
        board_L[2][1] -= 1
        return board_L, board_B
    elif move == "-EX'" or move == "-u":
        for i in range(len(board_B)):
            for x in range(len(board_B[i])):
                if not(i == 2 and x == 2):#Maybe fix this logic. Should be excluding only the first column of the first row
                    board_B[i][x] += 1
        board_L[0][0] -= 1
        board_L[0][2] -= 1
        board_L[2][0] -= 1
        return board_L, board_B
    elif move == "-EO'" or move == "-v":
        board_B[2][2] += 1
        board_L[1][1] -= 1
        board_L[1][2] -= 1
        board_L[2][1] -= 1
        board_L[2][2] -= 1
        return board_L, board_B
    elif move == "-FX'" or move == "-w":
        board_B[0][0] += 1
        board_B[0][1] += 1
        board_B[0][2] += 1
        board_B[1][0] += 1
        board_B[1][1] += 1
        board_B[1][2] += 1
        board_L[0][0] -= 1
        board_L[0][2] -= 1
        return board_L, board_B
    elif move == "-FO'" or move == "-x":
        board_B[2][0] += 1
        board_B[2][2] += 1
        board_L[1][0] -= 1
        board_L[1][1] -= 1
        board_L[1][2] -= 1
        board_L[2][0] -= 1
        board_L[2][1] -= 1
        board_L[2][2] -= 1
        return board_L, board_B
    elif move == "-GX'" or move == "-y":
        board_B[0][1] += 1
        board_B[0][2] += 1
        board_B[1][1] += 1
        board_B[1][2] += 1
        board_B[2][1] += 1
        board_B[2][2] += 1
        board_L[0][2] -= 1
        board_L[2][2] -= 1
        return board_L, board_B
    elif move == "-GO'" or move == "-z":
        board_B[0][0] += 1
        board_B[2][0] += 1
        board_L[0][0] -= 1
        board_L[0][1] -= 1
        board_L[1][0] -= 1
        board_L[1][1] -= 1
        board_L[2][0] -= 1
        board_L[2][1] -= 1
        return board_L, board_B
    else:
        return board_L, board_B

def is_puzzle_solved(board_L = [[12, 12, 12], [12, 12, 12], [12, 12, 12]], board_B = [[12, 12, 12], [12, 12, 12], [12, 12, 12]]):
    for i in range(len(board_L)):
        for x in range(len(board_L[i])):
            if board_L[i][x] != 12:
                return False
    for w in range(len(board_B)):
        for y in range(len(board_B[w])):
            if board_B[w][y] != 12:
                return False
    return True


'''
def recur_for(possible_letters: str, depth: int, indices, possible_solutions):
    if not(depth == 1):
        for i in range(len(possible_letters)):
            recur_for(possible_letters, depth - 1, indices + [i], possible_solutions)
    else:
        possible_solution = ""
        for p in indices:
            possible_solution += possible_letters[p]
        possible_solutions.append(possible_solution)

def brute_force(possible_letters: str, possible_length: int):
    possible_solutions = []
    if possible_length == 1:
        for i in range(len(possible_letters)):
            possible_solutions.append(possible_letters[i])
    else:
        for x in range(len(possible_letters)):
            recur_for(possible_letters, possible_length, [x], possible_solutions)
    return possible_solutions

def solver(board_L = [[12, 12, 12], [12, 12, 12], [12, 12, 12]], board_B = [[12, 12, 12], [12, 12, 12], [12, 12, 12]]):
    possible_letters = "abcdefghijklmnopqrstuvwxyz"
    possible_length = 1
    board_L_copy = board_L
    board_B_copy = board_B
    while True:
        move_list = brute_force(possible_letters, possible_length)
        for i in range(len(move_list)):
            for x in range(len(move_list[i])):
                board_L, board_B = make_move(move_list[i][x], board_L, board_B)
                draw_board(board_L, board_B, False)
            if is_puzzle_solved(board_L, board_B):
                print("Congrats, it has been solved. Here is the solution: {}".format(move_list[i]))
                return None
            else:#Resetting the board to the original state
                board_L = board_L_copy
                board_B = board_B_copy
        possible_length += 1
        print(possible_length)
'''
'''
def recur_for(possible_letters: str, depth: int, indices):
    if not(depth == 1):
        for i in range(len(possible_letters)):
            recur_for(possible_letters, depth - 1, indices + [i])
    else:
        f = open("Permutations.txt", "a")
        possible_solution = ""
        for p in indices:
            possible_solution += possible_letters[p]
        possible_solution += "\n"
        f.write(possible_solution)
        f.close()
        
def brute_force(possible_letters: str, possible_length: int):
    if possible_length == 1:
        f = open("Permutations.txt", "a")
        for i in range(len(possible_letters)):
            f.write(possible_letters[i] + "\n")
        f.close()
    else:
        for x in range(len(possible_letters)):
            recur_for(possible_letters, possible_length, [x])

def brute_force_solver(board_L = [[12, 12, 12], [12, 12, 12], [12, 12, 12]], board_B = [[12, 12, 12], [12, 12, 12], [12, 12, 12]], possible_length = 1):
    possible_letters = "abcdefghijklmnopqrstuvwxyz"
    board_L_copy = board_L
    board_B_copy = board_B
    while True:
        brute_force(possible_letters, possible_length)
        f = open("Permutations.txt", "w")
        f.write("")
        f.close()
        f = open("Permutations.txt")
        for move in f:
            board_L, board_B = make_move(move, board_L, board_B)
            draw_board(board_L, board_B, False)
            if is_puzzle_solved(board_L, board_B):
                print("Congrats, it has been solved. Here is the solution: {}".format(move))
                return None
            else:#Resetting the board to the original state
                board_L = board_L_copy
                board_B = board_B_copy
        f.close()
        possible_length += 1
        print(possible_length)
'''


def solver(board_L = [[12, 12, 12], [12, 12, 12], [12, 12, 12]], board_B = [[12, 12, 12], [12, 12, 12], [12, 12, 12]]):
    step = 1
    move_list = []
    while True:#Maybe make the elifs into ifs
        if step == 1:
            print("Step is: {}".format(step))
            while board_L[0][1] != board_L[0][0]:
                make_move("CO'", board_L, board_B)
                draw_board(board_L, board_B)
                move_list.append("CO'")
            step += 1
        elif step == 2:
            print("Step is: {}".format(step))
            while board_L[1][0] != board_L[0][0]:#also != board[0][1]
                make_move("DO'", board_L, board_B)
                draw_board(board_L, board_B)
                move_list.append("DO'")
            step += 1
        elif step == 3:
            print("Step is: {}".format(step))
            while board_L[1][1] != board_L[0][0]:# also != ^^^^
                make_move("EO'", board_L, board_B)
                draw_board(board_L, board_B)
                move_list.append("EO'")
            step += 1
        elif step == 4:
            print("Step is: {}".format(step))
            while board_L[0][2] != board_L[1][2]:
                make_move("CO", board_L, board_B)
                draw_board(board_L, board_B)
                move_list.append("CO")
            step += 1
        elif step == 5:
            print("Step is: {}".format(step))
            while board_L[0][0] != board_L[0][2]:#also != ^^^^
                make_move("BO'", board_L, board_B)
                draw_board(board_L, board_B)
                move_list.append("BO'")
            step += 1
        elif step == 6:
            print("Step is: {}".format(step))
            while board_L[0][0] != board_L[2][1]:#also != ^^^^
                make_move("FX", board_L, board_B)
                draw_board(board_L, board_B)
                move_list.append("FX")
            step += 1
        elif step == 7:
            print("Step is: {}".format(step))
            while board_L[2][0] != board_L[0][0]:
                make_move("DO", board_L, board_B)
                draw_board(board_L, board_B)
                move_list.append("DO")
            step += 1
        elif step == 8:
            print("Step is: {}".format(step))
            while board_L[2][2] != board_L[0][0]:
                make_move("EO", board_L, board_B)
                draw_board(board_L, board_B)
                move_list.append("EO")
            step += 1
        elif step == 9:
            print("Step is: {}".format(step))
            while board_L[0][0] != 12:
                make_move("A", board_L, board_B)
                draw_board(board_L, board_B)
                move_list.append("A")
            step += 1
        elif step == 10:#SIDE L COMPLETED. Might be very wrong below, as I didn't want to re-do the draw_board and make_move functions to account for non-xray board_B
            print("Step is: {}".format(step))
            if board_B[0][1] != 12:
                x = 12 - board_B[0][1]
                for i in range(x):
                    make_move("-CO", board_L, board_B)
                    draw_board(board_L, board_B)
                    move_list.append("-CO")
                for i in range(x):
                    make_move("-BO", board_L, board_B)
                    draw_board(board_L, board_B)
                    move_list.append("-BO")
                for i in range(x):
                    make_move("FX'", board_L, board_B)
                    draw_board(board_L, board_B)
                    move_list.append("FX'")
            if board_B[2][1] != 12:
                x = 12 - board_B[2][1]
                for i in range(x):
                    make_move("-DO", board_L, board_B)
                    draw_board(board_L, board_B)
                    move_list.append("-DO")
                for i in range(x):
                    make_move("-EO", board_L, board_B)
                    draw_board(board_L, board_B)
                    move_list.append("-EO")
                for i in range(x):
                    make_move("FO", board_L, board_B)
                    draw_board(board_L, board_B)
                    move_list.append("FO")
            if board_B[1][0] != 12:
                x = 12 - board_B[1][0]
                for i in range(x):
                    make_move("-DO", board_L, board_B)
                    draw_board(board_L, board_B)
                    move_list.append("-DO")
                for i in range(x):
                    make_move("-BO", board_L, board_B)
                    draw_board(board_L, board_B)
                    move_list.append("-BO")
                for i in range(x):
                    make_move("GO", board_L, board_B)
                    draw_board(board_L, board_B)
                    move_list.append("GO")
            if board_B[1][2] != 12:
                x = 12 - board_B[1][2]
                for i in range(x):
                    make_move("-CO", board_L, board_B)
                    draw_board(board_L, board_B)
                    move_list.append("-CO")
                for i in range(x):
                    make_move("-EO", board_L, board_B)
                    draw_board(board_L, board_B)
                    move_list.append("-EO")
                for i in range(x):
                    make_move("GX'", board_L, board_B)
                    draw_board(board_L, board_B)
                    move_list.append("GX'")
            step += 1
        elif step == 11:
            print("Step is: {}".format(step))
            if board_B[1][1] != 12:
                x = 12 - board_B[1][1]
                for i in range(x):
                    make_move("-BO", board_L, board_B)
                    draw_board(board_L, board_B)
                    move_list.append("-BO")
                    
                    make_move("-EO", board_L, board_B)
                    draw_board(board_L, board_B)
                    move_list.append("-EO")
                    
                    make_move("DX'", board_L, board_B)
                    draw_board(board_L, board_B)
                    move_list.append("DX'")
                    
                    make_move("CX'", board_L, board_B)
                    draw_board(board_L, board_B)
                    move_list.append("CX'")
                    
                    make_move("-A'", board_L, board_B)
                    draw_board(board_L, board_B)
                    move_list.append("-A'")
            step += 1
        elif step == 12:
            print("Congrats, the puzzle has been solved! Here's the solution: {}".format(move_list))
            return move_list

def solution_interpreter(move_list):
    e = "*"
    r = " "
    x = "X"
    o = "O"
    print("The first table denotes the pegs, where '{0}' means the peg is out, and '{1}' means the peg is down.\nThe second table denotes which knobs to turn, where '{2}' means rotate that knob clockwise(into the puzzle), and where '{3}' means rotate that knob counterclockwise(out of the puzzle).".format(e, r, x, o))
    for i in move_list:
        if i == "A":
            print("| {0} | {1} |   {4} | {5}\n| {2} | {3} |   {6} | {7}".format(e, e, e, e, x, x, x, x))
            w = input()
        elif i == "-A":
            print("| {0} | {1} |   {4} | {5}\n| {2} | {3} |   {6} | {7}".format(e, e, e, e, o, o, o, o))
            w = input()
        elif i == "A'":
            print("| {0} | {1} |   {4} | {5}\n| {2} | {3} |   {6} | {7}".format(r, r, r, r, x, x, x, x))
            w = input()
        elif i == "-A'":
            print("| {0} | {1} |   {4} | {5}\n| {2} | {3} |   {6} | {7}".format(r, r, r, r, o, o, o, o))
            w = input()
            

'''
#PLAY:
            
#board_L = [[12, 12, 8], [1, 9, 8], [11, 11, 8]]
#board_B = [[12, 1, 4], [11, 7, 9], [1, 5, 4]]
#board_L = [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
#board_B = [[3, 3, 3], [3, 3, 3], [3, 3, 3]]

draw_board(board_L, board_B)
while not(is_puzzle_solved(board_L, board_B)):
    move = input("\nWhat move would you like to make?\n").upper()
    print()
    board_L, board_B = make_move(move, board_L, board_B)
    draw_board(board_L, board_B)
print("CONGRATS, you have solved the puzzle!")

'''


'''
#BRUTE FORCE SOLVER:

#if possible_length == 1 and possible_letters == "ab":
#move_list = ["a", "b"]
#
#if possible_length == 2 and possible_letters == "ab":
#move_list = ["aa", "ab", "ba", "bb"]

board_L = [[12, 12, 8], [1, 9, 8], [11, 11, 8]]
board_B = [[12, 1, 4], [11, 7, 9], [1, 5, 4]]

brute_force_solver(board_L, board_B, 6)
'''

#ALGORITHMIC SOLVER:

board_L = [[12, 12, 8], [1, 9, 8], [11, 11, 8]]
board_B = [[12, 1, 4], [11, 7, 9], [1, 5, 4]]

move_list = solver(board_L, board_B)
for i in move_list:
    w = input(i)

