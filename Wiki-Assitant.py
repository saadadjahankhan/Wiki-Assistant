import wikipedia
import pyttsx3
import tkinter as tk
from tkinter import  *
from tkinter import messagebox
import webbrowser

engine = pyttsx3.init()
def printresult():
    re = wikipedia.summary(query.get())
    text.delete(1.0, END)
    text.insert(INSERT, re)
    engine.say(re)
    engine.runAndWait()

def abt():
	messagebox.showinfo("About","Wiki Assistant is a simple software which can scrap information about your search query from wikipedia.\nThis software was created by Saadad Jahan Khan [Mr.Venom]")

def help():
	messagebox.showinfo("Help", "Use the input box to enter your search query.\nAfter entering the query click on search button.Your result will be shown on the box.\n\nThanks for using this application.!")
def contact():
	webbrowser.open("https://facebook.com/ITXV3N0MDUD3")
###gui
root = tk.Tk()
root.title("Wiki Assistant | Version 1.0")
root.geometry("800x700")

##text define
text1 = Label(root,text="Wiki assistant",font=("tahoma",15,"underline"))
text1.pack()

##entrylabel
label1 = Label(root,text="Enter text to search:  ",font=("tahoma",10,"bold"))
label1.place(x=80,y=70)


#entrybox
query = Entry(root,width=70)
query.place(x=230,y=71)

#srchbtn
button = Button(root,text="Search",command=printresult).place(x=610,y=101)

###frame
bottom=Frame(root,bg="silver")
scrol=Scrollbar(bottom,background="black")#414e4e
scrol.pack(side=RIGHT,fill=Y)
text=Text(bottom,wrap=WORD,yscrollcommand=scrol.set,background="#6e7888",undo=True)
text.insert(INSERT,"Result Goes here!")
text.pack()
scrol.config(command=text.yview)
bottom.place(x=80,y=200)

##menubar
menubar = Menu(root,bg="grey")
root.config(menu=menubar)
menubar.config(background="grey")
menubar.add_command(label="About",command=abt)
menubar.add_command(label="Help",command=help)
menubar.add_command(label="Contact Us",command=contact)

if __name__ == '__main__':
	root.mainloop()

