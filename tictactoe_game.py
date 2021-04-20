import os
def DrawBoard():
    os.system('cls')
    print("\t\t    View\t\t\tRepresentation")
    print("\t\t %c | %c | %c " %(board[7],board[8],board[9]),"\t\t\t 7 | 8 | 9")    
    print("\t\t------------\t\t\t------------")    
    print("\t\t %c | %c | %c " %(board[4],board[5],board[6]),"\t\t\t 4 | 5 | 6")    
    print("\t\t------------\t\t\t------------")   
    print("\t\t %c | %c | %c " %(board[1],board[2],board[3]),"\t\t\t 1 | 2 | 3")
    print()

def procide():
    print("\t\tTo procide press 'Y'")
    print("\t\t",end="")
    entry=input().upper()
    while entry!='Y':
        print("\t\tInvalid input !! Please provide a valid input")
        print("\t\t",end="")
        entry=input().upper()
    os.system('cls')

def CheckWin():   
    #Horizontal winning condition    
    if(board[1] == board[2] and board[2] == board[3] and board[1] != ' '):    
        return "win"    
    elif(board[4] == board[5] and board[5] == board[6] and board[4] != ' '):    
        return "win"   
    elif(board[7] == board[8] and board[8] == board[9] and board[7] != ' '):    
        return "win"  
    #Vertical Winning Condition    
    elif(board[1] == board[4] and board[4] == board[7] and board[1] != ' '):    
        return "win"    
    elif(board[2] == board[5] and board[5] == board[8] and board[2] != ' '):    
        return "win"   
    elif(board[3] == board[6] and board[6] == board[9] and board[3] != ' '):    
        return "win"   
    #Diagonal Winning Condition    
    elif(board[1] == board[5] and board[5] == board[9] and board[5] != ' '):    
        return "win"  
    elif(board[3] == board[5] and board[5] == board[7] and board[5] != ' '):    
        return "win" 
    #Tie or Draw   
    elif(board[1]!=' ' and board[2]!=' ' and board[3]!=' ' and board[4]!=' ' and board[5]!=' ' and board[6]!=' ' and board[7]!=' ' and board[8]!=' ' and board[9]!=' '):    
        return "draw"    
    else:            
        return "running"


if __name__=='__main__':
    t=True
    sign=["X","O"]
    choice=["Y","N"]
    while t:
        board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        os.system('cls')
        print ("\t\tWelcome to tic tac toe game.")
        print("\t\tPlayer 1 select from 'X' &'O'")
        print("\t\t",end="")
        p1=input().upper()
        while p1 not in sign:
            print("\t\tInvalid input !! Please provide a valid input")
            print("\t\t",end="")
            p1=input().upper()
        p2='O' if p1=='X' else 'X'
        os.system('cls')
        print("\t\tPlayer 1 sign ",p1)
        print("\t\tPlayer 2 sign ",p2)
        procide()
        print("\t\tLets start the game")
        print("\t\tThe position of the board is identified as following")
        print("\t\t 7 | 8 | 9\n\t\t------------\n\t\t 4 | 5 | 6 \n\t\t------------\n\t\t 1 | 2 | 3 ")
        procide()
        ##############flags################
        win=0
        turn=1
        while turn<=9:
            if turn%2==1:
                p=1
                mark=p1
            else:
                p=2
                mark=p2
            DrawBoard()
            print("\t\tNow the turn is for Player %d "%p)
            print("\t\tChose your position ",end="")
            i=int(input())
            while board[i]!=" ":
                print("\t\tThe place is already occupied.")
                print("\t\tEnter another number: ",end="")
                i=int(input())
            board[i]=mark
            decision=CheckWin()
            if decision=="running":
                turn+=1
            elif decision=="win":
                DrawBoard()
                print("\t\tPlayer %d won." %p)
                break
            elif decision=="draw":
                print("\t\tThe game is draw")
        print("\t\tPress 'Y' for a new game or any key to exit",end="\n\t\t")
        res=input().upper()
        if res=='Y':
            t=True
        else:
            t=False
    os.system('cls')
    print("\t\tThank you for using our game!!!")
    print("\t\tGame is made by Amlan Dutta")
    input()
