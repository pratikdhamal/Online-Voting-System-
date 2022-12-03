import tkinter as tk
import socket
from tkinter import *
from PIL import ImageTk,Image

def voteCast(root,frame1,vote,client_socket):

    for widget in frame1.winfo_children():
        widget.destroy()

    client_socket.send(vote.encode()) #4

    message = client_socket.recv(1024) #Success message
    print(message.decode()) #5
    message = message.decode()
    if(message=="Successful"):
        Label(frame1, text="Vote Casted Successfully", font=('Arial Rounded MT Bold', 16),bg=('#32CD32')).grid(row = 1, column = 1)
    else:
        Label(frame1, text="Vote Cast Failed... \nTry again", font=('Arial Rounded MT Bold', 16),bg=('#EE4000')).grid(row = 1, column = 1)

    client_socket.close()



def votingPg(root,frame1,client_socket):

    root.title("Cast Vote")
    for widget in frame1.winfo_children():
        widget.destroy()

    Label(frame1, text="Cast Vote", font=('Arial Rounded MT Bold', 25,'bold')).grid(row = 0, column = 1, rowspan=1)
    Label(frame1, text="").grid(row = 1,column = 0)

    vote = StringVar(frame1,"-1")

    Radiobutton(frame1, text = "\nCOMP Department\n", variable = vote, value = "cse", indicator = 0, height = 4, width=15,font=('Oswald', 10, 'bold'), command = lambda: voteCast(root,frame1,"cse",client_socket)).grid(row = 2,column = 1)
    cseLogo = ImageTk.PhotoImage((Image.open("images/cse.png")).resize((54,42),Image.ANTIALIAS))
    cseImg = Label(frame1, image=cseLogo).grid(row = 2,column = 0)

    Radiobutton(frame1, text = "\nMECH Department\n", variable = vote, value = "mech", indicator = 0, height = 4, width=15,font=('Oswald', 10, 'bold'), command = lambda: voteCast(root,frame1,"mech",client_socket)).grid(row = 3,column = 1)
    mechLogo = ImageTk.PhotoImage((Image.open("images/mech.png")).resize((54,42),Image.ANTIALIAS))
    mechImg = Label(frame1, image=mechLogo).grid(row = 3,column = 0)

    Radiobutton(frame1, text = "\nINSTRU Department\n", variable = vote, value = "instru", indicator = 0, height = 4,font=('Oswald', 10, 'bold'), width=15, command = lambda: voteCast(root,frame1,"instru",client_socket) ).grid(row = 4,column = 1)
    instruLogo = ImageTk.PhotoImage((Image.open("images/instru.png")).resize((54,42),Image.ANTIALIAS))
    instruImg = Label(frame1, image=instruLogo).grid(row = 4,column = 0)

    Radiobutton(frame1, text = "\nCHEM Department\n", variable = vote, value = "chem", indicator = 0, height = 4, width=15,font=('Oswald', 10, 'bold'), command = lambda: voteCast(root,frame1,"chem",client_socket)).grid(row = 5,column = 1)
    chemLogo = ImageTk.PhotoImage((Image.open("images/chem.png")).resize((54,42),Image.ANTIALIAS))
    chemImg = Label(frame1, image=chemLogo).grid(row = 5,column = 0)

    Radiobutton(frame1, text = "\nCIVIL Department   \n  ", variable = vote, value = "civil", indicator = 0, height = 4,font=('Oswald', 10, 'bold'), width=15, command = lambda: voteCast(root,frame1,"civil",client_socket)).grid(row = 6,column = 1)
    civilLogo = ImageTk.PhotoImage((Image.open("images/civil.png")).resize((54,42),Image.ANTIALIAS))
    civilImg = Label(frame1, image=civilLogo).grid(row = 6,column = 0)

    frame1.pack()
    root.mainloop()


# if __name__ == "__main__":
#         root = Tk()
#         root.geometry('500x500')
#         frame1 = Frame(root)
#         client_socket='Fail'
#         votingPg(root,frame1,client_socket)
