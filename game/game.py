from tkinter import* 


import random


def nextturn(row,column) :
    global player
    
    if buts [row][column]['text']== "" and winner() is False:
       if player == players [0]:
         buts [row][column]['text']= player
         if winner () is False :
             player = players [1]
             label.config(text=(players[1]+"turn"))
         if winner () is True :
             
             label.config(text=(players[0]+"wins"))
         if winner () == "tie" :
            
             label.config(text=("tie!"))
       else:
             buts [row][column]['text']= player
             if winner () is False :
                 player = players [0]
              
                 label.config(text=(players[0]+"turn"))
             if winner () is True :
              
              label.config(text=(players[1]+"wins"))
             if winner () == "tie" :
            
              label.config(text=("tie!"))
             

    


def winner():
    for row in range (3):
        
        if buts [row][0]['text']==buts [row][1]['text'] == buts [row][2]['text'] != "":
            buts [row][0].config(bg = "green")
            buts [row][1].config(bg = "green")
            buts [row][2].config(bg = "green")
            return True
    for column in range (3):
        if buts [0][column]['text'] ==buts [1][column]['text'] == buts [2][column]['text'] != "":
            buts [0][column].config(bg = "green")
            buts [1][column].config(bg = "green")
            buts [2][column].config(bg = "green")
            return True

    if buts [0][0]['text'] ==buts [1][1]['text'] == buts [2][2]['text'] != "":
            buts [0][0].config(bg = "green")
            buts [1][1].config(bg = "green")
            buts [2][2].config(bg = "green")
            return True
    if buts [0][2]['text'] ==buts [1][1]['text'] == buts [2][0]['text'] != "":
            buts [0][2].config(bg = "green")
            buts [1][1].config(bg = "green")
            buts [2][0].config(bg = "green")
            return True
    if empty () is False :
        return "tie"
    else :
        return False
    
def empty():
    space = 9
    for row in range (3):
        for column in range (3):
            if buts [row][column]['text'] != "":
                space = space -1
    if space == 0 :
        return False
    else :
        return True
def newgame ():
    global player
    player = random.choice (players) 
    label.config(text = player + " turn")
    for row in range (3):
        for column in range (3):
            buts [row][column].config(text = "", bg = "#F0F0F0")
    
root = Tk()
root.title("tic tac toe")

players = ["x" , "o"]

player= random.choice(players)

buts = [[0,0,0],
        [0,0,0],
        [0,0,0]]
label = Label(text = player + " turn")
label.pack()
but = Button (text = "reset" , command = newgame)
but.pack()
frame = Frame(root)
frame.pack()

for row in range (3):
    for column in range (3):
        buts[row][column]=Button(frame , text = "",width =10 ,height =10, command = lambda row = row , column = column : nextturn(row,column))
        buts[row][column].grid (row=row , column= column)





root.mainloop()
