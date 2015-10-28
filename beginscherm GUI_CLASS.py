from tkinter import *
from PIL import Image, ImageTk
import requests
import xmltodict

class Beginscherm:

    def __init__(self,master):
        window.configure(bg="#fdcf19")
        window.geometry("1366x768")

        global MainFrame
        MainFrame = Frame(master,bg="#fdcf19",height=630)
        MainFrame.pack(side=TOP,fill=X)

        global BotFrame
        BotFrame =Frame(master,bg="#01236A",height=50)
        BotFrame.pack(side=BOTTOM,fill=X)

        self.l1 = Label(MainFrame,text="Welkom bij NS",fg="#01236A",bg="#fdcf19",font=("arial", 33))
        self.l1.place(relx=0.5, rely=0.5,y=-250, anchor=CENTER)

        self.l2= Label(MainFrame,image=photo1,bg="#fdcf19")
        self.l2.place(relx=0.5, rely=0.5,y=-100, anchor=CENTER)

        self.l3= Label (BotFrame,image=photo2,bg="#01236A")
        self.l3.place(relx=0.5, rely=0.5,y=5,anchor=E)


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
        Treinen(window)


class Treinen:
    def __init__(self,master):
        global frame2
        frame2= Frame(master,bg="#fdcf19")
        frame2.pack(side=TOP,fill=X)

        self.labeltijd = Label(frame2,anchor='w',text='Tijd',fg="#003399",bg="#fdcf19", width=5).grid(row=0,column=0)
        self.LabelVertraging = Label(frame2,anchor='w',text='',fg="#003399",bg="#fdcf19", width=4).grid(row=0,column=1)
        self.labelnaar = Label(frame2,anchor='w',text='Naar', fg="#003399",bg="#fdcf19", width=25).grid(row=0,column=2)
        self.labelvertrekspoor = Label(frame2,anchor='w',text='Spoor', fg="#003399",bg="#fdcf19", width=12).grid(row=0,column=3)
        self.labelroutetekst = Label(frame2,anchor='w',text='Via', fg="#003399",bg="#fdcf19", width=60).grid(row=0,column=4)
        self.labelvervoerder = Label(frame2,anchor='w',text='Vervoerder', fg="#003399",bg="#fdcf19", width=18).grid(row=0,column=5)
        self.labelritnummer = Label(frame2,anchor='w',text='Ritnummer', fg="#003399",bg="#fdcf19", width=15).grid(row=0,column=6)
        self.labeltreinsoort = Label(frame2,anchor='w',text='Treinsoort', fg="#003399",bg="#fdcf19", width=15).grid(row=0,column=7)

        for hoeveelstetrein in range(1, aantaltreinen,2):
            self.tijd = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['VertrekTijd'][11:16]
            self.Naar = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['EindBestemming']
            self.Ritnummer = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['RitNummer']
            self.Treinsoort = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['TreinSoort']
            self.Vertrekspoor = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['VertrekSpoor']['#text']

            try:
                self.Vervoerder = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['Vervoerder']
            except KeyError:
                self.Vervoerder = ''
            try:
                self.Vertraging = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['VertrekVertragingTekst'][0:2]
            except KeyError:
                self.Vertraging = ''

            try:
                self.Via = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['RouteTekst']
            except KeyError:
                self.Via = ''

            try:
                self.Routetekst = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['RouteTekst']
            except KeyError:
                self.Routetekst = ''

            self.labeltijdAPI = Label(frame2,anchor='w',text=self.tijd,fg="white",bg="#003399", width=5).grid(row=hoeveelstetrein,column=0)
            self.labelVertraging = Label(frame2,anchor='w',text=self.Vertraging,fg="red",bg="#003399", width=4).grid(row=hoeveelstetrein,column=1)
            self.labelnaarAPI = Label(frame2,anchor='w',text=self.Naar, fg="white",bg="#003399", width=25).grid(row=hoeveelstetrein,column=2)
            self.labelvertrekspoorAPI = Label(frame2,anchor='w',text=self.Vertrekspoor, fg="white",bg="#003399", width=12).grid(row=hoeveelstetrein,column=3)
            self.labelroutetekstAPI = Label(frame2,anchor='w',text=self.Routetekst, fg="white",bg="#003399", width=60).grid(row=hoeveelstetrein,column=4)
            self.labelvervoerderAPI = Label(frame2,anchor='w',text=self.Vervoerder, fg="white",bg="#003399", width=18).grid(row=hoeveelstetrein,column=5)
            self.labelritnummerAPI = Label(frame2,anchor='w',text=self.Ritnummer, fg="white",bg="#003399", width=15).grid(row=hoeveelstetrein,column=6)
            self.labeltreinsoortAPI = Label(frame2,anchor='w',text=self.Treinsoort, fg="white",bg="#003399", width=15).grid(row=hoeveelstetrein,column=7)

        for hoeveelstetrein in range(2, aantaltreinen,2):
            self.tijd = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['VertrekTijd'][11:16]
            self.Naar = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['EindBestemming']
            self.Ritnummer = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['RitNummer']
            self.Treinsoort = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['TreinSoort']
            self.Vertrekspoor = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['VertrekSpoor']['#text']


            try:
                self.Vervoerder = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['Vervoerder']
            except KeyError:
                self.Vervoerder = ''
            try:
                self.Vertraging = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['VertrekVertragingTekst'][0:2]
            except KeyError:
                self.Vertraging = ''

            try:
                self.Via = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['RouteTekst']
            except KeyError:
                self.Via = ''

            try:
                self.Routetekst = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['RouteTekst']
            except KeyError:
                self.Routetekst = ''

            self.labeltijdAPI = Label(frame2,anchor='w',text=self.tijd,fg="white",bg="#0000ff", width=5).grid(row=hoeveelstetrein,column=0)
            self.labelVertraging = Label(frame2,anchor='w',text=self.Vertraging,fg="red",bg="#0000ff", width=4).grid(row=hoeveelstetrein,column=1)
            self.labelnaarAPI = Label(frame2,anchor='w',text=self.Naar, fg="white",bg="#0000ff", width=25).grid(row=hoeveelstetrein,column=2)
            self.labelvertrekspoorAPI = Label(frame2,anchor='w',text=self.Vertrekspoor, fg="white",bg="#0000ff", width=12).grid(row=hoeveelstetrein,column=3)
            self.labelroutetekstAPI = Label(frame2,anchor='w',text=self.Routetekst, fg="white",bg="#0000ff", width=60).grid(row=hoeveelstetrein,column=4)
            self.labelvervoerderAPI = Label(frame2,anchor='w',text=self.Vervoerder, fg="white",bg="#0000ff", width=18).grid(row=hoeveelstetrein,column=5)
            self.labelritnummerAPI = Label(frame2,anchor='w',text=self.Ritnummer, fg="white",bg="#0000ff", width=15).grid(row=hoeveelstetrein,column=6)
            self.labeltreinsoortAPI = Label(frame2,anchor='w',text=self.Treinsoort, fg="white",bg="#0000ff", width=15).grid(row=hoeveelstetrein,column=7)


            self.buttonMeerResultaten = Button(frame2,text='Meer \n treinen', fg="white",bg="#01236A",width=19,height=3, font=("arial",15), command=self.meerResult).place(y=20,x=1135)
            self.buttonTerug = Button(frame2,text='Terug', fg="white",bg="#01236A",width=19,height=3,command=self.terug,font=("arial",15)).place(y=125,x=1135)

    def meerResult(self):
        for hoeveelstetrein in range(aantaltreinen+1, aantaltreinen+5,2):
            self.tijd = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['VertrekTijd'][11:16]
            self.Naar = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['EindBestemming']
            self.Ritnummer = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['RitNummer']
            self.Treinsoort = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['TreinSoort']
            self.Vertrekspoor = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['VertrekSpoor']['#text']

            try:
                self.Vervoerder = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['Vervoerder']
            except KeyError:
                self.Vervoerder = ''
            try:
                self.Vertraging = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['VertrekVertragingTekst'][0:2]
            except KeyError:
                self.Vertraging = ''

            try:
                self.Via = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['RouteTekst']
            except KeyError:
                self.Via = ''

            try:
                self.Routetekst = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['RouteTekst']
            except KeyError:
                self.Routetekst = ''

            self.labeltijdAPI = Label(frame2,anchor='w',text=self.tijd,fg="white",bg="#003399", width=5).grid(row=hoeveelstetrein,column=0)
            self.labelVertraging = Label(frame2,anchor='w',text=self.Vertraging,fg="red",bg="#003399", width=4).grid(row=hoeveelstetrein,column=1)
            self.labelnaarAPI = Label(frame2,anchor='w',text=self.Naar, fg="white",bg="#003399", width=25).grid(row=hoeveelstetrein,column=2)
            self.labelvertrekspoorAPI = Label(frame2,anchor='w',text=self.Vertrekspoor, fg="white",bg="#003399", width=12).grid(row=hoeveelstetrein,column=3)
            self.labelroutetekstAPI = Label(frame2,anchor='w',text=self.Routetekst, fg="white",bg="#003399", width=60).grid(row=hoeveelstetrein,column=4)
            self.labelvervoerderAPI = Label(frame2,anchor='w',text=self.Vervoerder, fg="white",bg="#003399", width=18).grid(row=hoeveelstetrein,column=5)
            self.labelritnummerAPI = Label(frame2,anchor='w',text=self.Ritnummer, fg="white",bg="#003399", width=15).grid(row=hoeveelstetrein,column=6)
            self.labeltreinsoortAPI = Label(frame2,anchor='w',text=self.Treinsoort, fg="white",bg="#003399", width=15).grid(row=hoeveelstetrein,column=7)


        for hoeveelstetrein in range(aantaltreinen, aantaltreinen+5,2):
            self.tijd = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['VertrekTijd'][11:16]
            self.Naar = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['EindBestemming']
            self.Ritnummer = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['RitNummer']
            self.Treinsoort = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['TreinSoort']
            self.Vertrekspoor = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['VertrekSpoor']['#text']


            try:
                self.Vervoerder = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['Vervoerder']
            except KeyError:
                self.Vervoerder = ''
            try:
                self.Vertraging = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['VertrekVertragingTekst'][0:2]
            except KeyError:
                self.Vertraging = ''

            try:
                self.Via = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['RouteTekst']
            except KeyError:
                self.Via = ''

            try:
                self.Routetekst = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['RouteTekst']
            except KeyError:
                self.Routetekst = ''

            self.labeltijdAPI = Label(frame2,anchor='w',text=self.tijd,fg="white",bg="#0000ff", width=5).grid(row=hoeveelstetrein,column=0)
            self.labelVertraging = Label(frame2,anchor='w',text=self.Vertraging,fg="red",bg="#0000ff", width=4).grid(row=hoeveelstetrein,column=1)
            self.labelnaarAPI = Label(frame2,anchor='w',text=self.Naar, fg="white",bg="#0000ff", width=25).grid(row=hoeveelstetrein,column=2)
            self.labelvertrekspoorAPI = Label(frame2,anchor='w',text=self.Vertrekspoor, fg="white",bg="#0000ff", width=12).grid(row=hoeveelstetrein,column=3)
            self.labelroutetekstAPI = Label(frame2,anchor='w',text=self.Routetekst, fg="white",bg="#0000ff", width=60).grid(row=hoeveelstetrein,column=4)
            self.labelvervoerderAPI = Label(frame2,anchor='w',text=self.Vervoerder, fg="white",bg="#0000ff", width=18).grid(row=hoeveelstetrein,column=5)
            self.labelritnummerAPI = Label(frame2,anchor='w',text=self.Ritnummer, fg="white",bg="#0000ff", width=15).grid(row=hoeveelstetrein,column=6)
            self.labeltreinsoortAPI = Label(frame2,anchor='w',text=self.Treinsoort, fg="white",bg="#0000ff", width=15).grid(row=hoeveelstetrein,column=7)

        global aantaltreinen
        aantaltreinen +=5
    def terug(self):
        frame2.destroy()
        Beginscherm(window)


try:
    window= Tk()

    url = 'http://webservices.ns.nl/ns-api-avt?station=ut'
    user = 'dennis-strik@hotmail.com'
    passw = 'Bmz5NUzoLz3GLtbRrbwIznZUdHs_5pqL5Yv-6dMrW5V_lknjcVqStg'
    response = requests.get(url, auth=(user, passw))
    xmldi = xmltodict.parse(response.text)
    hoeveelstetrein = 1
    aantaltreinen = 16

    photo1 = ImageTk.PhotoImage(Image.open ("ovkaart.jpg"))
    photo2 = ImageTk.PhotoImage(Image.open ("taalenopties.jpg"))

    Beginscherm(window)


    window.mainloop()
except SyntaxError as error_info:
    print("er gaat wat fout",error_info)

