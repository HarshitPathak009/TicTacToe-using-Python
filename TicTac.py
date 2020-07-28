from tkinter import *
import tkinter.font as font

#global variables
move=0
choice = ["X","O"]
p = {0:[],1:[]}

acombo = {0:[0,1,2],1:[3,4,5],2:[6,7,8],3:[0,3,6],4:[1,4,7],5:[2,5,8],6:[0,4,8],7:[2,4,6]}

#methods
def click(a):
	global move
	text[a].set(choice[move%2])
	p[move%2].append(a)
	move+=1
	b[a]["state"]=DISABLED
	check()


def check():
	global p
	flg = True
	for i in range(8):
		c = acombo[i]
		flg = True
		for j in c:
			if(j not in p[0]):
				flg = False
				break
		if flg==True:
			p1text.set("Player 1: WINS")
			p2text.set("Player 2: LOST")
			for i in range(9):
				b[i]["state"] = DISABLED
			return 
	for i in range(8):
		c = acombo[i]
		flg = True
		for j in c:
			if(j not in p[1]):
				flg = False
				break
		if flg==True:
			p1text.set("Player 1: LOST")
			p2text.set("Player 2: WINS")
			for i in range(9):
				b[i]["state"] = DISABLED
			return
	if move == 9:
		p1text.set("Player 1: DRAW")
		p2text.set("Player 2: DRAW")

		
#frame creation
if __name__=="__main__": 
	r = Tk()
	r.title("TicTacToe")
	r.geometry("690x800")

	#labels
	p1text = StringVar()
	p2text = StringVar()
	p1text.set("Player 1: X")
	p2text.set("Player 2: O")
	l1 = Label(r,textvariable=p1text,font="times 22",fg="red")
	l1.grid(row=0,column=0)
	l2 = Label(r,textvariable=p2text,font="times 22",fg="green")
	l2.grid(row=0,column=2)

	
	text =[]
	b=[]
	for i in range(9):
		text.append(StringVar())


	#Buttons
	b.append(Button(r,textvariable=text[0],height=10,width=20,command=lambda:click(0),font="times 15",fg="black"))
	b[0].grid(row=1,column=0)
	b.append(Button(r,textvariable=text[1],height=10,width=20,command=lambda:click(1),font="times 15",fg="black"))
	b[1].grid(row=1,column=1)
	b.append(Button(r,textvariable=text[2],height=10,width=20,command=lambda:click(2),font="times 15",fg="black"))
	b[2].grid(row=1,column=2)
	b.append(Button(r,textvariable=text[3],height=10,width=20,command=lambda:click(3),font="times 15",fg="black"))
	b[3].grid(row=2,column=0)
	b.append(Button(r,textvariable=text[4],height=10,width=20,command=lambda:click(4),font="times 15",fg="black"))
	b[4].grid(row=2,column=1)
	b.append(Button(r,textvariable=text[5],height=10,width=20,command=lambda:click(5),font="times 15",fg="black"))
	b[5].grid(row=2,column=2)
	b.append(Button(r,textvariable=text[6],height=10,width=20,command=lambda:click(6),font="times 15",fg="black"))
	b[6].grid(row=3,column=0)
	b.append(Button(r,textvariable=text[7],height=10,width=20,command=lambda:click(7),font="times 15",fg="black"))
	b[7].grid(row=3,column=1)
	b.append(Button(r,textvariable=text[8],height=10,width=20,command=lambda:click(8),font="times 15",fg="black"))
	b[8].grid(row=3,column=2)
	r.mainloop()
	