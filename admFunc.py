import tkinter as tk
import dframe as df
from tkinter import *
from dframe import *
from PIL import ImageTk,Image

def resetAll(root,frame1):
    # df.count_reset()
    #df.reset_voter_list()
    #df.reset_cand_list()
    Label(frame1, text="").grid(row = 10,column = 0)
    msg = Message(frame1, text="Reset Complete", width=500)
    msg.grid(row = 11, column = 0, columnspan = 5)

def showVotes(root,frame1):

    result = df.show_result()
    root.title("Votes")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Vote Count", font=('Arial Rounded MT Bold', 25, 'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    cseLogo = ImageTk.PhotoImage((Image.open("images/cse.png")).resize((54,40),Image.ANTIALIAS))
    cseImg = Label(frame1, image=cseLogo).grid(row = 2,column = 0)

    mechLogo = ImageTk.PhotoImage((Image.open("images/mech.png")).resize((50,40),Image.ANTIALIAS))
    mechImg = Label(frame1, image=mechLogo).grid(row = 4,column = 0)

    instruLogo = ImageTk.PhotoImage((Image.open("images/instru.png")).resize((50,40),Image.ANTIALIAS))
    instruImg = Label(frame1, image=instruLogo).grid(row = 6,column = 0)

    chemLogo = ImageTk.PhotoImage((Image.open("images/chem.png")).resize((50,40),Image.ANTIALIAS))
    chemImg = Label(frame1, image=chemLogo).grid(row = 8,column = 0)

    civilLogo = ImageTk.PhotoImage((Image.open("images/civil.png")).resize((50,40),Image.ANTIALIAS))
    civilImg = Label(frame1, image=civilLogo).grid(row = 10,column = 0)


    Label(frame1, text=" COMP              :          ", font=('Oswald', 12,'bold')).grid(row = 2, column = 1)
    Label(frame1, text=result['cse'], font=('Arial Rounded MT Bold', 12)).grid(row = 2, column = 2)

    Label(frame1, text=" MECH              :          ", font=('Oswald', 12,'bold')).grid(row = 4, column = 1)
    Label(frame1, text=result['mech'], font=('Arial Rounded MT Bold', 12)).grid(row = 4, column = 2)

    Label(frame1, text=" INSTRU            :          ", font=('Oswald', 12,'bold')).grid(row = 6, column = 1)
    Label(frame1, text=result['instru'], font=('Arial Rounded MT Bold', 12)).grid(row = 6, column = 2)

    Label(frame1, text=" CHEM              :          ", font=('Oswald', 12,'bold')).grid(row = 8, column = 1)
    Label(frame1, text=result['chem'], font=('Arial Rounded MT Bold', 12)).grid(row = 8, column = 2)

    Label(frame1, text=" CIVIL             :          ", font=('Oswald', 12,'bold')).grid(row = 10, column = 1)
    Label(frame1, text=result['civil'], font=('Arial Rounded MT Bold', 12)).grid(row = 10, column = 2)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         showVotes(root,frame1)
