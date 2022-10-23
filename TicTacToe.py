import time
from tkinter import *
from turtle import back

from matplotlib.pyplot import margins
from sklearn.preprocessing import scale

root = Tk()
# root.overrideredirect(True)
root.geometry("532x635")
root.title("Tic Tac Toe")
root.config(bg="black")
root.iconphoto(False,PhotoImage(file='./Images/icon.ico',))

player = "You"
buttons = [[0,0,0],[0,0,0],[0,0,0]]
btns = [[],[],[]]
count = 0
gameWin = 0

head = Frame(root,borderwidth=10,background="#404040")
head.grid(row=0,column=0,sticky="nsew")
game = Frame(root,borderwidth=20,background="#202020")
game.grid(row=1,column=0,sticky="nsew")

label = Label(head,text="{}".format(player),padx=20,pady=10,width=10,background="black",foreground="lime",font=("Consolas",15,"bold"))
label.pack()
    

def allsame(a,b,c):
    return a == b and b == c and a != 0

def checkGame(buttons):
    gameWin = 0

    for i in range(3):
        if allsame(buttons[i][0],buttons[i][1],buttons[i][2]):
            gameWin=buttons[i][0]
            for j in range(3):
                if gameWin == 1:
                    btns[i][j].button.config(disabledforeground="green")
                else:
                    btns[i][j].button.config(disabledforeground="red")
                    
    for i in range(3):
        if allsame(buttons[0][i],buttons[1][i],buttons[2][i]):
            gameWin=buttons[0][i]
            for j in range(3):
                if gameWin == 1:
                    btns[j][i].button.config(disabledforeground="green")
                else:
                    btns[j][i].button.config(disabledforeground="red")

    if allsame(buttons[0][0],buttons[1][1],buttons[2][2]):
        gameWin=buttons[0][0]
        for i in range(3):
            if gameWin == 1:
                btns[i][i].button.config(disabledforeground="green")
            else:
                btns[i][i].button.config(disabledforeground="red")

    if allsame(buttons[2][0],buttons[1][1],buttons[0][2]):
        gameWin=buttons[2][0]
        for i in range(3):
            if gameWin == 1:
                btns[i][2-i].button.config(disabledforeground="green")
            else:
                btns[i][2-i].button.config(disabledforeground="red")
    
    return gameWin

def checkDraw(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return False
    return True

def chkwin(buttons):
    win = 0

    for i in range(3):
        if allsame(buttons[i][0],buttons[i][1],buttons[i][2]):
            win=buttons[i][0]
                    
    for i in range(3):
        if allsame(buttons[0][i],buttons[1][i],buttons[2][i]):
            win=buttons[0][i]

    if allsame(buttons[0][0],buttons[1][1],buttons[2][2]):
        win=buttons[0][0]

    if allsame(buttons[2][0],buttons[1][1],buttons[0][2]):
        win=buttons[2][0]
    
    return win

def advSearch(state):
    bestScore = -1000
    bestMove = (0,0)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                state[i][j] = 2
                score = minimax(state, False)
                state[i][j] = 0
                if score>bestScore:
                    bestScore = score
                    bestMove = (i,j)
    return bestMove

def minimax(state,isMaximizing):
    status = chkwin(state)
    if status == 2:
        return 1
    elif status == 1:
        return -1
    elif checkDraw(state):
        return 0
    
    if isMaximizing:
        bestscore = -1000
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    state[i][j] = 2
                    score = minimax(state,False)
                    state[i][j] = 0
                    if score>bestscore:
                        bestscore=score
        return bestscore
    else:
        bestscore = 1000
        for i in range(3):
            for j in range(3):
                if state[i][j] == 0:
                    state[i][j] = 1
                    score = minimax(state,True)
                    state[i][j] = 0
                    if score<bestscore:
                        bestscore=score
        return bestscore
    

class GameButton:
    def __init__(self, i, j):
        self.button = Button(game,text="",width=7,height=3,font=("Consolas",30,"bold"),command=self.onpressed)
        self.button.config(background="#404040",activebackground="#404040")
        self.i = i
        self.j = j
    
    def onpressed(self):
        global player
        global label
        global count
        global gameWin
        global buttons
        global action
        global btns

        if player == 'You':
            self.button.config(text="X",state=DISABLED,disabledforeground="#aaaaaa"); 
            buttons[self.i][self.j] = 1
        else:
            self.button.config(text="O",state=DISABLED); 
            buttons[self.i][self.j] = 2

        if player == "You":
            player = "Bot"
        else:
            player = "You" 
            
        label.config(text="{}".format(player))

        gameWin = checkGame(buttons)
        count+=1
        if gameWin != 0:
            label.config(text="{} Win{}".format("You" if gameWin==1 else "Bot","s" if gameWin==2 else ""))
            for i in range(3):
                for j in range(3):
                    btns[i][j].button.config(state=DISABLED)
        elif checkDraw(buttons):
            label.config(text="Draw")
            return

        if player == 'Bot':
            action = advSearch(buttons)
            btns[action[0]][action[1]].onpressed()


for i in range(3):
    for j in range(3):
        button = GameButton(i,j)
        btns[i].append(button)
        button.button.grid(row=i,column=j)

root.resizable(False,False)
root.mainloop()