#napravo cqla programa za igrata tic tac toe
def join(delimiter, items):
    string=""
    for i in range(0,len(items)-1):
        string += str(items[i])
        string += delimiter
    string += str(items[len(items)-1])
    return string

def board_to_string(board):
    string=""
    for i in range(0,len(board)-1):
        string+="|"+str(join("|",board[i])+"|"+"\n")
    string+="|"+str(join("|",board[len(board)-1]))+"|"
    return string

def hod(igrach, chislo, board):
    a=(chislo-1)//3
    b=chislo%3
    red=board[2-a]
    red[b-1]=str(igrach)
    return board

def proverka(board):
    red1=board[0]
    red2=board[1]
    red3=board[2]
    if red1[0]==red2[1]==red3[2]=="X" or red1[0]==red1[1]==red1[2]=="X" or red2[0]==red2[1]==red2[2]=="X" or red3[0]==red3[1]==red3[2]=="X" or red1[0]==red2[0]==red3[0]=="X" or red1[1]==red2[1]==red3[1]=="X" or red1[2]==red2[2]==red3[2]=="X" or red1[2]==red2[1]==red3[0]=="X":
        return "X"
    elif red1[0]==red2[1]==red3[2]=="O" or red1[0]==red1[1]==red1[2]=="O" or red2[0]==red2[1]==red2[2]=="O" or red3[0]==red3[1]==red3[2]=="O" or red1[0]==red2[0]==red3[0]=="O" or red1[1]==red2[1]==red3[1]=="O" or red1[2]==red2[2]==red3[2]=="O" or red1[2]==red2[1]==red3[0]=="O":
        return "O"
    elif red1[0]!="-" and red1[1]!="-" and red1[2]!="-" and red2[0]!="-" and red2[1]!="-" and red2[2]!="-" and red3[0]!="-" and red3[1]!="-" and red3[2]!="-":
        return("ravenstvo")
    else:
        return "Nowinner"
def igra(igrach,board,k):
    izbor=0
    while izbor<1 or izbor>9:
        izbor=int(input("Enter a valid player "+igrach+"'s choice:"))
        board=hod(igrach,izbor,board)
        print(board_to_string(board))
        if proverka(board)==igrach:
            print("The winner is player",igrach,"!")
            k+=1
        elif proverka(board)=="ravenstvo":
            print("There is no winner!")
            k+=1
        elif proverka(board)=="Nowinner":
            print("Keep goin")


board=[["-","-","-"],["-","-","-"],["-","-","-"]]
print(board_to_string(board))
k=0
j=1
while True:
    if j%2==1:
        izbor=0
        while izbor<1 or izbor>9:
            izbor=int(input("Enter a valid player X's choice:"))
        board=hod("X",izbor,board)
        print(board_to_string(board))
        if proverka(board)=="X":
            print("The winner is player X!")
            break
        elif proverka(board)=="ravenstvo":
            print("There is no winner!")
            break
        elif proverka(board)=="Nowinner":
            print("Keep goin'")

    if j%2==0:
        izbor=0
        while izbor<1 or izbor>9:
            izbor=int(input("Enter a valid player O's choice:"))
        board=hod("O",izbor,board)
        print(board_to_string(board))
        if proverka(board)=="O":
            print("The winner is player O!")
            break
        elif proverka(board)=="ravenstvo":
            print("There is no winner!")
            break
        elif proverka(board)=="Nowinner":
            print("Keep goin'")
    j+=1
