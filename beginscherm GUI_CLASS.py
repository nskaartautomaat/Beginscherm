from tkinter import *
from PIL import Image, ImageTk


class Beginscherm:

    def __init__(self,master):
        window.configure(bg="#fdcf19")
        window.geometry("1366x768")

        global MainFrame
        MainFrame = Frame(master,bg="#fdcf19",height=718)
        MainFrame.pack(side=TOP,fill=X)

        global BotFrame
        BotFrame =Frame(master,bg="#01236A",height=50)
        BotFrame.pack(side=BOTTOM,fill=X)

        self.l1 = Label(MainFrame,text="Welkom bij NS",fg="#01236A",bg="#fdcf19",font=("arial", 33))
        self.l1.place(relx=0.5, rely=0.5,y=-250, anchor=CENTER)

        self.l2= Label(MainFrame,image=photo1,bg="#fdcf19")
        self.l2.place(relx=0.5, rely=0.5,y=-100, anchor=CENTER)

        self.l3= Label (BotFrame,image=photo2,bg="#01236A")
        self.l3.place(relx=0.5, rely=0.5,x=-180,anchor=E)


        self.b1= Button(MainFrame,text="Kopen \nlos kaartje",fg="white",bg="#01236A",width=19,height=3, font=("arial",15))
        self.b1.place(relx=0.5, rely=0.5,y=109,x=-350, anchor=CENTER)

        self.b2= Button(MainFrame,text="Kopen \nOV-chipkaart",fg="white",bg="#01236A",width=19,height=3, font=("arial",15))
        self.b2.place(relx=0.5, rely=0.5,y=109,x=-120, anchor=CENTER)

        self.b3= Button(MainFrame,text="Ik wil naar \nhet buitenland",fg="white",bg="#01236A",width=19,height=3, font=("arial",15))
        self.b3.place(relx=0.5, rely=0.5,y=109,x=110, anchor=CENTER)

        self.b4= Button(MainFrame,text="Actuele \nreisinformatie",fg="white",bg="#01236A",command=self.bpress,width=19,height=3, font=("arial",15))
        self.b4.place(relx=0.5, rely=0.5,y=109,x=340, anchor=CENTER)
    def bpress(self):
        MainFrame.destroy()
        BotFrame.destroy()
        Test(window)

class Test:

    def __init__(self,master):
        frame = Frame(master)
        frame.pack()

        self.printButton = Button(frame, text="test msg",command=self.printMassage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button (frame, text="Quit",command=frame.quit)
        self.quitButton.pack(side=LEFT)

    def printMassage(self):
        print("dit is een bericht")


try:
    window= Tk()

    photo1 = ImageTk.PhotoImage(Image.open ("ovkaart.jpg"))
    photo2 = ImageTk.PhotoImage(Image.open ("taalenopties.jpg"))

    beginscherm = Beginscherm(window)


    window.mainloop()
except SyntaxError as error_info:
    print("er gaat wat fout",error_info)

