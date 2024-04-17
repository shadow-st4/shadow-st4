from tkinter import *
from tkinter.messagebox import showinfo

root = Tk()

def reset_game():
    global btn, point_p1, point_p2, button, point, round_player, selection, point_player
    point_p1.config(text=point[0])
    point_p2.config(text=point[1])
    selection = ['','','',
                 '','','',
                 '','','']
    for i in range(9):
        button[i].config(text=selection[i])
        
def rull():
    global btn, point_p1, point_p2, button, point, round_player, selection, point_player
    #player one
    if selection[0] == 'o' and selection[1] == 'o' and selection[2] == 'o':
        showinfo('game the end','player one is win!')
        point[0] += 1
        btn.after(100, reset_game)
    elif selection[3] == 'o' and selection[4] == 'o' and selection[5] == 'o':
        showinfo('game the end','player one is win!')
        point[0] += 1
        btn.after(100, reset_game)
    elif selection[6] == 'o' and selection[7] == 'o' and selection[8] == 'o':
        showinfo('game the end','player one is win!')
        point[0] += 1
        btn.after(100, reset_game)
    elif selection[0] == 'o' and selection[3] == 'o' and selection[6] == 'o':
        showinfo('game the end','player one is win!')
        point[0] += 1
        btn.after(100, reset_game)
    elif selection[1] == 'o' and selection[4] == 'o' and selection[7] == 'o':
        showinfo('game the end','player one is win!')
        point[0] += 1
        btn.after(100, reset_game)
    elif selection[2] == 'o' and selection[5] == 'o' and selection[8] == 'o':
        showinfo('game the end','player one is win!')
        point[0] += 1
        btn.after(100, reset_game)
    elif selection[0] == 'o' and selection[4] == 'o' and selection[8] == 'o':
        showinfo('game the end','player one is win!')
        point[0] += 1
        btn.after(100, reset_game)
    elif selection[2] == 'o' and selection[4] == 'o' and selection[6] == 'o':
        showinfo('game the end','player one is win!')
        point[0] += 1
        btn.after(100, reset_game)

    #player two
    if selection[0] == 'x' and selection[1] == 'x' and selection[2] == 'x':
        showinfo('game the end','player two is win!')
        point[1] += 1
        btn.after(100, reset_game)
    elif selection[3] == 'x' and selection[4] == 'x' and selection[5] == 'x':
        showinfo('game the end','player two is win!')
        point[1] += 1
        btn.after(100, reset_game)
    elif selection[6] == 'x' and selection[7] == 'x' and selection[8] == 'x':
        showinfo('game the end','player two is win!')
        point[1] += 1
        btn.after(100, reset_game)
    elif selection[0] == 'x' and selection[3] == 'x' and selection[6] == 'x':
        showinfo('game the end','player two is win!')
        point[1] += 1
        btn.after(100, reset_game)
    elif selection[1] == 'x' and selection[4] == 'x' and selection[7] == 'x':
        showinfo('game the end','player two is win!')
        point[1] += 1
        btn.after(100, reset_game)
    elif selection[2] == 'x' and selection[5] == 'x' and selection[8] == 'x':
        showinfo('game the end','player two is win!')
        point[1] += 1
        btn.after(100, reset_game)
    elif selection[0] == 'x' and selection[4] == 'x' and selection[8] == 'x':
        showinfo('game the end','player two is win!')
        point[1] += 1
        btn.after(100, reset_game)
    elif selection[2] == 'x' and selection[4] == 'x' and selection[6] == 'x':
        showinfo('game the end','player two is win!')
        point[1] += 1
        btn.after(100, reset_game)

def select(x):
    global btn, point_p1, point_p2, button, point, round_player, selection, point_player
    #config's player
    if selection[x] == '':
        if round_player == 'player one':
            button[x].config(text='o', fg='green')
            selection[x] = 'o'
            round_player = 'player two'
            rull()
        elif round_player == 'player two':
            button[x].config(text='x', fg='purple')
            selection[x] = 'x'
            round_player = 'player one'
            rull()

def point_players():
    global btn, point_p1, point_p2, button, point, round_player, selection, point_player
    point_case = Frame(root)
    point_case.grid(row=0, column=0)
    point_p1 = Label(point_case, font=Font, fg='green', text=point[0])
    point_p1.grid(row=0, column=0)
    point_p2 = Label(point_case, font=Font, fg='purple', text=point[1])
    point_p2.grid(row=0, column=1)

def create_board():
    global btn, point_p1, point_p2, button, point, round_player, selection, point_player
    board = Frame(root)
    board.grid(row=1, column=0)
    button = []
    col = 0
    rw = 0
    width_btn = 8
    height_btn = 4
    for i in range(9):
        btn = Button(board, text='', font=Font, width=width_btn, height=height_btn, bg='white', fg='black', command=lambda x=i : select(x))
        btn.grid(row=rw, column=col)
        button.append(btn)
        col += 1
        if col %3 == 0:
            rw += 1
            col = 0

#option's
point = [0,0]
Font = ('', 18, '')
round_player = 'player one'
selection = ['','','',
             '','','',
             '','','']

#start game
create_board()
point_players()

root.mainloop()
