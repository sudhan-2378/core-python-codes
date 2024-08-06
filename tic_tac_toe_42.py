block = ["","","","","","","","",""]
score_a = 0
score_b = 0
x,o = "",""
print("welcome to tic-tac-toe")
a = input("enter the first player's name : ")
b = input("enter the second player's name : ")
def board(val):
    print("\n")
    print("\t       |         |")
    print("\t ",val[0],"   |  ",val[1],"    |  ",val[2])
    print("\t_______|_________|________")
    print("\t       |         |")
    print("\t ",val[3],"   |  ",val[4],"    |  ",val[5])
    print("\t_______|_________|________")
    print("\t       |         |")
    print("\t ",val[6],"   |  ",val[7],"    |  ",val[8])
    print("\n")
    
board(block)
def scorecard(a,b,c,d):
    print("=======================")
    print("+      SCORECARD      +")
    print("=======================")
    print(f"     {a}   --   {c}     ")
    print(f"     {b}   --   {d}     ")
    print("=======================")

scorecard(a,b,score_a,score_b)
def solution_x(block,x):
    if [block[0],block[1],block[2]] == ["x","x","x"]:
        return True
    elif [block[3],block[4],block[5]] == ["x","x","x"]:
        return True
    elif [block[6],block[7],block[8]] == ["x","x","x"]:
        return True
    elif [block[0],block[3],block[6]] == ["x","x","x"]:
        return True
    elif [block[1],block[4],block[7]] == ["x","x","x"]:
        return True
    elif [block[2],block[5],block[8]] == ["x","x","x"]:
        return True
    elif [block[0],block[4],block[8]] == ["x","x","x"]:
        return True
    elif [block[2],block[4],block[6]] == ["x","x","x"]:
        return True

def solution_o(block,o):
    if [block[0],block[1],block[2]] == ["o","o","o"]:
        return True
    elif [block[3],block[4],block[5]] == ["o","o","o"]:
        return True
    elif [block[6],block[7],block[8]] == ["o","o","o"]:
        return True
    elif [block[0],block[3],block[6]] == ["o","o","o"]:
        return True
    elif [block[1],block[4],block[7]] == ["o","o","o"]:
        return True
    elif [block[2],block[5],block[8]] == ["o","o","o"]:
        return True
    elif [block[0],block[4],block[8]] == ["o","o","o"]:
        return True
    elif [block[2],block[4],block[6]] == ["o","o","o"]:
        return True

def gameplay(block,a,b,score_a,score_b):
    score_a = 0
    score_b = 0
    print(f"player {a} chooses first : ")
    print("1.play\n2.quit")
    option = int(input("enter your option(1/2) : "))
    if option == 1:
        player_a = a
        a = "x"
        player_b = b
        b = "o"
        board(block)
        for i in range(5):
            choice_x = int(input("enter your block's position : "))
            if len(block[choice_x - 1]) == 1:
                print("this block is already occupied.try again!!")
                choice_x = int(input("enter your block's position : "))
                if len(block[choice_x - 1]) == 1:
                    print("your chance is over!!")
                else:
                    block[choice_x - 1] = "x"
            else:
                block[choice_x - 1] = "x"
            solution_x(block,x)
            if solution_x(block,x) == True:
                print("player x has won the game")
                score_a += 1
                scorecard(player_a,player_b,score_a,score_b)
                break
            board(block)
            if i == 4:
                break
            choice_o = int(input("enter your block's position : "))
            if len(block[choice_o - 1]) == 1:
                print("this block is already occupied.try again!!")
                choice_o = int(input("enter your block's position : "))
                if len(block[choice_o - 1]) == 1:
                    print("your chance is over!!")
                else:
                    block[choice_o - 1] = "o"
            else:
                block[choice_o - 1] = "o"
            solution_o(block,o)
            if solution_o(block,o) == True:
                print("player o has won the game")
                score_b += 1
                scorecard(player_a,player_b,score_a,score_b)
                break
            board(block)
        else:
            print("It's a draw!")
            scorecard(player_a,player_b,score_a,score_b)
        print("the game has finished...")
    if option == 2:
        scorecard(player_a,player_b,score_a,score_b)

gameplay(block,a,b,score_a,score_b)
