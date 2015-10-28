from tkinter import *
from PIL import Image, ImageTk
import requests
import xmltodict
import time


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

        self.LabWelkom = Label(MainFrame,text="Welkom bij NS",fg="#01236A",bg="#fdcf19",font=("arial", 33))
        self.LabWelkom.place(relx=0.5, rely=0.5,y=-250, anchor=CENTER)

        self.LabPhoto1= Label(MainFrame,image=photo1,bg="#fdcf19")
        self.LabPhoto1.place(relx=0.5, rely=0.5,y=-100, anchor=CENTER)

        self.LabPhoto2= Label (BotFrame,image=photo2,bg="#01236A")
        self.LabPhoto2.place(relx=0.5, rely=0.5,y=5,anchor=E)


        self.ButKaartje= Button(MainFrame,text="Kopen \nlos kaartje",fg="white",bg="#01236A",width=19,height=3, font=("arial",15))
        self.ButKaartje.place(relx=0.5, rely=0.5,y=109,x=-350, anchor=CENTER)

        self.ButOV= Button(MainFrame,text="Kopen \nOV-chipkaart",fg="white",bg="#01236A",width=19,height=3, font=("arial",15))
        self.ButOV.place(relx=0.5, rely=0.5,y=109,x=-120, anchor=CENTER)

        self.ButBuitenland= Button(MainFrame,text="Ik wil naar \nhet buitenland",fg="white",bg="#01236A",width=19,height=3, font=("arial",15))
        self.ButBuitenland.place(relx=0.5, rely=0.5,y=109,x=110, anchor=CENTER)

        self.ButReisinfo= Button(MainFrame,text="Actuele \nreisinformatie",fg="white",bg="#01236A",command=self.bpress,width=19,height=3, font=("arial",15))
        self.ButReisinfo.place(relx=0.5, rely=0.5,y=109,x=340, anchor=CENTER)
    def bpress(self):
        MainFrame.destroy()
        BotFrame.destroy()
        Treinen(window)


class Treinen:

    def __init__(self,master):

        global response
        response = requests.get(url, auth=(user, passw))
        global xmldi
        xmldi = xmltodict.parse(response.text)
        global frame2
        frame2= Frame(master,bg="#fdcf19")
        frame2.pack(side=TOP,fill=X)


        tijd = time.strftime("%H:%M:%S")

        #Labels voor de koptekst
        self.labeltijd = Label(frame2, anchor='w',text='Tijd',fg="#003399",bg="#fdcf19", width=5).grid(row=0,column=0)
        self.LabelVertraging = Label(frame2, anchor='w',text='',fg="#003399",bg="#fdcf19", width=4).grid(row=0,column=1)
        self.labelnaar = Label(frame2, anchor='w',text='Naar', fg="#003399",bg="#fdcf19", width=25).grid(row=0,column=2)
        self.labelvertrekspoor = Label(frame2,anchor='w',text='Spoor', fg="#003399",bg="#fdcf19", width=12).grid(row=0,column=3)
        self.labelroutetekst = Label(frame2,anchor='w',text='Via', fg="#003399",bg="#fdcf19", width=60).grid(row=0,column=4)
        self.labelvervoerder = Label(frame2,anchor='w',text='Vervoerder', fg="#003399",bg="#fdcf19", width=18).grid(row=0,column=5)
        self.labelritnummer = Label(frame2,anchor='w',text='Ritnummer', fg="#003399",bg="#fdcf19", width=15).grid(row=0,column=6)
        self.labeltreinsoort = Label(frame2,anchor='w',text='Treinsoort', fg="#003399",bg="#fdcf19", width=15).grid(row=0,column=7)

        for hoeveelstetrein in range(0, aantaltreinen):
            if hoeveelstetrein % 2 == 0:
                kleur = "#003399"
            else:
                kleur = "#0000ff"

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
                self.Vertraging = xmldi['ActueleVertrekTijden']['VertrekkendeTrein'][hoeveelstetrein]['VertrekVertragingTekst'][0:3]
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

            rij= hoeveelstetrein+1

            self.labeltijdAPI = Label(frame2,anchor='w',text=self.tijd,fg="white",bg=kleur, width=5).grid(row=rij,column=0)
            self.labelVertraging = Label(frame2,anchor='w',text=self.Vertraging,fg="red",bg=kleur, width=4).grid(row=rij,column=1)
            self.labelnaarAPI = Label(frame2,anchor='w',text=self.Naar, fg="white",bg=kleur, width=25).grid(row=rij,column=2)
            self.labelvertrekspoorAPI = Label(frame2,anchor='w',text=self.Vertrekspoor, fg="white",bg=kleur, width=12).grid(row=rij,column=3)
            self.labelroutetekstAPI = Label(frame2,anchor='w',text=self.Routetekst, fg="white",bg=kleur, width=60).grid(row=rij,column=4)
            self.labelvervoerderAPI = Label(frame2,anchor='w',text=self.Vervoerder, fg="white",bg=kleur, width=18).grid(row=rij,column=5)
            self.labelritnummerAPI = Label(frame2,anchor='w',text=self.Ritnummer, fg="white",bg=kleur, width=15).grid(row=rij,column=6)
            self.labeltreinsoortAPI = Label(frame2,anchor='w',text=self.Treinsoort, fg="white",bg=kleur, width=15).grid(row=rij,column=7)


            self.labelCurTime = Label(text=tijd).place (relx=0.5, rely=0.5,y=-363,x=450)
            self.buttonMeerResultaten = Button(text='Meer \n treinen', state=NORMAL, fg="white",bg="#01236A",width=19,height=3, font=("arial",15), command=self.meerResult).place(relx=0.5, rely=0.5,y=-263,x=450)
            self.buttonRefresh = Button(text='Refresh', fg="white",bg="#01236A",width=19,height=3,font=("arial",15),command=self.refresh).place(relx=0.5, rely=0.5,y=-168,x=450)
            self.buttonTerug = Button(text='Terug', fg="white",bg="#01236A",width=19,height=3, command = self.terug,font=("arial",15)).place(relx=0.5, rely=0.5,y=-73,x=450)

    def meerResult(self):
        global extra_treinen
        global aantaltreinen
        for hoeveelstetrein in range(aantaltreinen, aantaltreinen+6):
            if hoeveelstetrein % 2 == 0:
                kleur = "#003399"
            else:
                kleur = "#0000ff"

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

            rij= hoeveelstetrein+1

            self.labeltijdAPI = Label(frame2,anchor='w',text=self.tijd,fg="white",bg=kleur, width=5).grid(row=rij,column=0)
            self.labelVertraging = Label(frame2,anchor='w',text=self.Vertraging,fg="red",bg=kleur, width=4).grid(row=rij,column=1)
            self.labelnaarAPI = Label(frame2,anchor='w',text=self.Naar, fg="white",bg=kleur, width=25).grid(row=rij,column=2)
            self.labelvertrekspoorAPI = Label(frame2,anchor='w',text=self.Vertrekspoor, fg="white",bg=kleur, width=12).grid(row=rij,column=3)
            self.labelroutetekstAPI = Label(frame2,anchor='w',text=self.Routetekst, fg="white",bg=kleur, width=60).grid(row=rij,column=4)
            self.labelvervoerderAPI = Label(frame2,anchor='w',text=self.Vervoerder, fg="white",bg=kleur, width=18).grid(row=rij,column=5)
            self.labelritnummerAPI = Label(frame2,anchor='w',text=self.Ritnummer, fg="white",bg=kleur, width=15).grid(row=rij,column=6)
            self.labeltreinsoortAPI = Label(frame2,anchor='w',text=self.Treinsoort, fg="white",bg=kleur, width=15).grid(row=rij,column=7)

        aantaltreinen +=6
        extra_treinen +=1

        if extra_treinen == 2:
            self.buttonMeerResultaten = Button(text='Meer \n treinen', state=DISABLED, fg="white",bg="#01236A",width=19,height=3, font=("arial",15), command=self.meerResult).place(relx=0.5, rely=0.5,y=-363,x=450)



    def refresh(self):
        frame2.destroy()
        Treinen(window)

    def update_timeText(self):
        current = time.strftime("%H:%M:%S")
        self.labelCurTime.configure(text=current)
        time.sleep(60)
        self.update_timeText()
        return current

    def terug(self):
        global aantaltreinen
        global extra_treinen
        aantaltreinen = 16
        frame2.destroy()
        Beginscherm(window)
        extra_treinen = 0


try:
    window= Tk()

    url = 'http://webservices.ns.nl/ns-api-avt?station=ut'
    user = 'dennis-strik@hotmail.com'
    passw = 'Bmz5NUzoLz3GLtbRrbwIznZUdHs_5pqL5Yv-6dMrW5V_lknjcVqStg'
    #response = requests.get(url, auth=(user, passw))
    #xmldi = xmltodict.parse(response.text)
    hoeveelstetrein = 0
    aantaltreinen = 16
    extra_treinen = 0

    photo1 = ImageTk.PhotoImage(Image.open ("ovkaart.jpg"))
    photo2 = ImageTk.PhotoImage(Image.open ("taalenopties.jpg"))

    Beginscherm(window)


    window.mainloop()
except SyntaxError as error_info:
    print("er gaat wat fout",error_info)
