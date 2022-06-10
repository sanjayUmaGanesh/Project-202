import socket
import pyttsx3
from tkinter import *
from threading import Thread


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip_address = "127.0.0.1"
port = 8000

client.connect((ip_address,port))
vA = pyttsx3.init()
voices = vA.getProperty('voices') 
vA.setProperty('voice', voices[1].id)
vA.setProperty('rate', 200)
vA.say("Connection established with the server")
print("Connection established\n\n")
vA.runAndWait()

class GUI:
    def __init__(self):
        self.window = Tk()
        self.window.withdraw()

        self.loginWin = Toplevel()
        self.loginWin.title = "LoGiN0"

        self.loginWin.resizable(width = False, height = False)
        self.loginWin.configure(width= 400, height = 300)

        self.pls = Label(self.loginWin,
        text = "Please login to continue...",
        justify = CENTER,
        font ="Helvetica 14 bold" )

        self.pls.place(
        relheight=0.14,
        relx = 0.2,
        rely = 0.07)

        self.labelName = Label(self.loginWin,
        text = "Name: ",
        font = "Helvetica 12")

        self.labelName.place(
        relheight = 0.2,
        relx = 0.1,
        rely = 0.2)
        
        self.entryName = Entry(self.loginWin,font = "Helvetica 12")
        self.entryName.place(
        relwidth = 0.4,
        relheight = 0.09,
        relx = 0.35,
        rely = 0.26)

        self.entryName.focus()

        self.go = Button(
            self.loginWin, 
            text = "Continue",
            font = "Helvetica 12 bold",
            command=lambda:self.proceed(self.entryName.get())
            )
        self.go.place(
            relx = 0.4,
            rely = 0.44)
        
        self.window.mainloop()

    def proceed(self,name):
        self.loginWin.destroy()
        self.name = name
        rcv = Thread(target = self.recieve)
        rcv.start()

    def recieve(self):
        while True:
            try:
                message = client.recv(2048).decode('utf-8')
                if message == "NICKNAME":
                    client.send(self.name.encode('utf-8'))
                else:
                    pass
                
            except:
                print("An error occured")
                client.close()
                break


g = GUI()


# def write():
#     while True:
#         message = '{}'.format(input(""))
#         client.send(message.encode('utf-8'))







# recieve_thread = Thread(target=recieve)
# recieve_thread.start()
# write_thread = Thread(target=write)
# write_thread.start()