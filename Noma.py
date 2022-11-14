import itertools
import datetime
from datetime import time
from datetime import datetime
from re import X
import PySimpleGUI as sg


sg.theme('DarkGrey13')

class Klients:
    produkta_kategorija=None
    produkta_nosaukums=None
    nomas_cena_diena=None
    produkts_pieejams=None
    vards=None
    uzvards=None
    numurs=None

    def __init__(self, produkta_kategorija=None , produkta_nosaukums=None, nomas_cena_diena=None, produkts_pieejams=None,vards=None , uzvards=None, numurs=None):
        self.produkta_kategorija=produkta_kategorija
        self.produkta_nosaukums=produkta_nosaukums
        self.nomas_cena_diena=nomas_cena_diena
        self.produkts_pieejams=produkts_pieejams
        self.vards=vards
        self.uzvards=uzvards
        self.numurs=numurs

    def set_data(self, produkta_kategorija=None , produkta_nosaukums=None, nomas_cena_diena=None, produkts_pieejams=None,vards=None , uzvards=None, numurs=None):
        self.produkta_kategorija=produkta_kategorija
        self.produkta_nosaukums=produkta_nosaukums
        self.nomas_cena_diena=nomas_cena_diena
        self.produkts_pieejams=produkts_pieejams
        self.vards=vards
        self.uzvards=uzvards
        self.numurs=numurs

    def get_data(self):
        print('Vārds: ', self.vards)
        print('Uzvārds: ', self.uzvards)
        print('Telefona numurs: ',self.numurs)
        print('Produkta kategorija: ',self.produkta_kategorija)
        print('Produkta nosaukums: ',self.produkta_nosaukums)
        print('Nomas cena dienā: ',self.nomas_cena_diena)
        print('Produkts pieejams: ',self.produkts_pieejams)

class laiks:
    pakalpojuma_sakums=0
    pakalpojuma_beigas=0


    def __init__(self, pakalpojuma_sakums=None, pakalpojuma_beigas=None):
        self.pakalpojuma_sakums=pakalpojuma_sakums
        self.pakalpojuma_beigas=pakalpojuma_beigas
        self.pakalpojuma_atlikusais_laiks=self.pakalpojuma_sakums-self.pakalpojuma_beigas
        self.pakalpojuma_dienas=self.pakalpojuma_beigas-self.pakalpojuma_sakums
        self.laiks_info()
    
    def laiks_info(self):
        print('Pakalpojums sākuma laiks: '+ str(self.pakalpojuma_sakums))
        print('Pakalpojums beigu laiks: '+ str(self.pakalpojuma_beigas))
        print('Pakalpojuma palikušais laiks: '+ str(self.pakalpojuma_atlikusais_laiks))
        print('Cena: '+ str(self.nomas_cena_diena) * str(self.pakalpojuma_dienas))

file=open('Klienta_info.txt')


class logwindow:
    layout=[[sg.T('Klients')]],
        [sg.T('Vards'), sg.I(key='vards')],
        [sg.T('Uzvards'), sg.I(key='uzvards')],
        [sg.T('Produkta_nosaukums'), sg.I(key='produkta_nosaukums')],
        [sg.T('Produkta_kategorija'), sg.I(key='produkta_kategorija')],
        [sg.T('Produkts_pieejams'), sg.I(key='produkts_pieejams')],
        [sg.T('Nomas_cena_diena'), sg.I(key='nomas_cena_diena')],
        [sg.T(key='-OUT-')],
        [sg.B('Saglabat'), sg.B('Izvadit uz ekrana'), sg.B('Saglabat teksta formata'), sg.Exit()]]  

    window=sg.Window('klienta dati', layout)
    

        while True:
        event, values=window.read()


        if event==sg.WIN_CLOSED or event == 'Exit':
            break

        elif event=='Saglabat':
          klients1=laiks(values['vards'], values['uzvards'], values['produkta_nosaukums'], values['produkta_kategorija']), values['produkts_pieejams']), values['nomas_cena_diena'])

        elif event=="Izvadit uz ekrana":
          klients1=laiks(values['vards'], values['uzvards'], values['produkta_nosaukums'], values['produkta_kategorija']), values['produkts_pieejams']), values['nomas_cena_diena'])
          klients1.get_data()

        elif event=="Saglabat teksta formata":
            file=open("Klienta_info.txt", 'a')
            file.write(str(klients1.klienta_info()))
            file.write("\n")
            file.close()
    window.close()



now = datetime.now()

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("laiks un datums=", dt_string)	
