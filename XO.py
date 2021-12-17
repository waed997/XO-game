#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

master = Tk()
root = Toplevel(master)
master.title('XO Game')
master.geometry('280x250')
master.resizable(False, False)
master.configure(background='#15151D')
labelxo = ttk.Label(master, text="XO game", font=('Arial', 30), background='#15151D', foreground='#eeeeee')


def starting():
    if len(entryx.get()) <= 8 and len(entryo.get()) <= 8:
        root.state('normal')
        master.state('withdrawn')
        labelx.configure(text=" your turn\n {}\n       {}".format(entryx.get(), xw))
        labelo.configure(text="\n {}\n       {}".format(entryo.get(), ow))
    elif len(entryx.get()) > 8 and len(entryo.get()) > 8:
        messagebox.showinfo(title='The X and O players names are too long'
                        , message='The players names are too long, please use maximum of 8 letters as a players name')
    elif len(entryx.get()) > 8:
        messagebox.showinfo(title='The X player name is too long'
                            , message='The player name is too long, please use maximum of 8 letters')
    elif len(entryo.get()) > 8:
        messagebox.showinfo(title='The O player name is too long'
                            , message='The player name is too long, please use maximum of 8 letters')


def mm():
    global tt
    tt = 'X'
    root.state('withdrawn')
    master.state('normal')
    nr()


start_button = Button(master, text='Start', font=('Arial', 20), width=5, height=1, bg='#E3E3E3', command=starting)
newg_button = Button(root, text='New\ngame', font=('Arial', 20), width=5, height=2, bg='#E3E3E3', command=mm)
newg_button.place(x=527, y=298)
labelxp = ttk.Label(master, text='X player:', font=('Arial', 15), background='#15151D', foreground='#eeeeee')
labelop = ttk.Label(master, text='O player:', font=('Arial', 15), background='#15151D', foreground='#eeeeee')
entryx = ttk.Entry(master, width=8)
entryx.insert(0, 'X player')
entryo = ttk.Entry(master, width=8)
entryo.insert(0, 'O player')
labelxo.grid(row=0, column=0, columnspan=2, padx=50, pady=10)
start_button.grid(row=1, column=0, columnspan=2, pady=10)
labelxp.grid(row=2, column=0, pady=2)
labelop.grid(row=2, column=1)
entryx.grid(row=3, column=0, ipadx=12, ipady=3)
entryo.grid(row=3, column=1, ipadx=12, ipady=3)
steps = 0
xw = 0
ow = 0
root.geometry('640x500')
root.resizable(False, False)
root.configure(background='#15151D')
root.title('XO Game')
root.state('withdrawn')
label = ttk.Label(root, text=" ", background='black')
labelnr = ttk.Label(root, text="", background='#15151D', foreground='white')
label.place(relx=0.5, rely=0.39, anchor='center')
labelnr.place(relx=0.5, rely=0.8, anchor='center')
labelx = ttk.Label(root, text=" your turn\n {}\n       {}".format(entryx.get(), xw), font=('Arial', 20)
                   , background='#746c6c', foreground='#FF0235')
labelx.place(x=5, y=10, width=121, height=100)
labelo = ttk.Label(root, text="\n {}\n       {}".format(entryo.get(), ow), font=('Arial', 20)
                   , background='#746c6c', foreground='#0054A3')
labelo.place(x=512.5, y=10, width=121, height=100)


def nr():
    global ow, xw
    ow, xw = 0, 0
    if tt == 'O':
        labelo.configure(text=" your turn\n {}\n       {}".format(entryo.get(), ow))
        labelx.configure(text="\n {}\n       {}".format(entryx.get(), xw))
    elif tt == 'X':
        labelx.configure(text=" your turn\n {}\n       {}".format(entryx.get(), xw))
        labelo.configure(text="\n {}\n       {}".format(entryo.get(), ow))
    for i in range(3):
        for j in range(3):
            b[i][j]['state'] = NORMAL
    reset()


def en():
    for i in range(3):
        for j in range(3):
            b[i][j]['state'] = NORMAL
    reset()


def ds():
    for i in range(3):
        for j in range(3):
            b[i][j]['state'] = DISABLED
    labelnr.configure(text='press next round to continue or RESET to play again')


def reset():
    global s
    for i in range(3):
        for j in range(3):
            b[i][j].configure(text=' ')
    s = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    labelnr.configure(text='')


def checkwin(s):
    global xw
    global ow
    w = 0
    fr = ''
    sr = ''
    for p in range(2):
        for i in range(3):
            if wc[p][:] == s[i][:] or ((s[0][i] == wc[p][i]) & (s[1][i] == wc[p][i]) & (s[2][i] == wc[p][i])):
                w = 1
                if p == 0:
                    xw += 1
                    labelx.configure(text="\n {}\n       {}".format(entryx.get(), xw))
                else:
                    ow += 1
                    labelo.configure(text="\n {}\n       {}".format(entryo.get(), ow))
            fr += s[i][i]
            sr += s[i][2 - i]

    if fr == 'XXXXXX' or sr == 'XXXXXX':
        w = 1
        xw += 1
        labelx.configure(text="\n {}\n       {}".format(entryx.get(), xw))
    if fr == 'OOOOOO' or sr == 'OOOOOO':
        w = 1
        ow += 1
        labelo.configure(text="\n {}\n       {}".format(entryo.get(), ow))
    return w


def callback(r, c):
    global tt
    if s[r][c] == ' ' and tt == 'X':
        b[r][c].configure(text='X', fg='#FF0235')
        labelo.configure(text=" your turn\n {}\n       {}".format(entryo.get(), ow))
        labelx.configure(text="\n {}\n       {}".format(entryx.get(), xw))
        tt = 'O'
        s[r][c] = 'X'
    elif s[r][c] == ' ' and tt == 'O':
        b[r][c].configure(text='O', fg='#0054A3')
        labelx.configure(text=" your turn\n {}\n       {}".format(entryx.get(), xw))
        labelo.configure(text="\n {}\n       {}".format(entryo.get(), ow))
        tt = 'X'
        s[r][c] = 'O'
    if checkwin(s) == 1:
        ds()


wc = [['X', 'X', 'X'], ['O', 'O', 'O']]
s = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
b = [[0, 0, 0, ], [0, 0, 0, ], [0, 0, 0, ]]
tt = 'X'
for i in range(3):
    for j in range(3):
        b[i][j] = Button(label, text=' ', font=('Arial', 48), bg='#E3E3E3', width=3
                         , height=1, command=lambda r=i, c=j: callback(r, c))
        b[i][j].grid(row=i, column=j, padx=1, pady=1)
nextr_button = Button(root, text='next round', font=('Arial', 20), command=en, width=8, height=1, bg='#E3E3E3')
nextr_button.place(x=350, y=420)
reset_button = Button(root, text='RESET', font=('Arial', 20), command=nr, width=8, height=1, bg='#E3E3E3')
reset_button.place(x=150, y=420)

root.mainloop()
