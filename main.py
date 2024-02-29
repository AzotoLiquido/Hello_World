from logo import logo,logo_attrezzaggio # Importo i loghi dal file logo
import os # Importo la libreria os
from attrezzaggio import carica_torretta_mazak,carica_mandrino_mazak,attrezzaggio_forcella,attrez_mandrino_hd1,attrez_mandrino_hd2,attrez_torretta_hd1,attrez_torretta_hd2,attrez_robot_mazak,torretta_mazak,mandrino_mazak
from colorama import Fore, Back, Style
from PIL import Image

#creo e descrivo gli attributi dell'oggetto forcella
class Forcella:
    def __init__(self,codice_materiale,h_tot,centro_sfera,centro_occhi,sottoponte,dist_canaline,diam_occhi,diam_canaline,diam_flangia_int,diam_flangia_est,diam_sfera,quota_g):
        self.codice_materiale=str(codice_materiale)
        self.h_tot=round(float(h_tot),3)
        self.centro_sfera=round(float(centro_sfera),3)
        self.centro_occhi=round(float(centro_occhi),3)
        self.sottoponte=round(float(sottoponte),3)
        self.dist_canaline=round(float(dist_canaline),3)
        self.diam_occhi=round(float(diam_occhi),3)
        self.diam_canaline=round(float(diam_canaline),3)
        self.diam_flangia_int=round(float(diam_flangia_int),3)
        self.diam_flangia_est=round(float(diam_flangia_est),3)
        self.diam_sfera=round(float(diam_sfera),3)
        self.quota_g=round(float(quota_g),3)

    # Creo una funzione che mi printa a schermo tutti gli attributi della forcella
    def show_details(self):
        testo_formattato = f"\n[Dettagli Forcella]\n\n[1] Codice_Materiale: {self.codice_materiale}\n[2] Altezza_totale: {self.h_tot}\n[3] Centro_Sfera: {self.centro_sfera}\n[4] Centro_occhi: {self.centro_occhi}\n[5] Sottoponte: {self.sottoponte}\n[6] Distanza_canaline: {self.dist_canaline}\n[7] Diametro_occhi: {self.diam_occhi}\n[8] Diametro_canaline: {self.diam_canaline}\n[9] Diametro_interno_flangia: {self.diam_flangia_int}\n[10] Diametro_esterno_flangia: {self.diam_flangia_est}\n[11] Diametro_sfera: {self.diam_sfera}\n[12] Quota_'G': {self.quota_g}"
        delimitatore = "_"*50
        return f"\n{delimitatore}\n{testo_formattato}\n{delimitatore}\n"
    
# #Creo degli oggetti Forcella d'esempio.
codice_G = Forcella(codice_materiale="2150G0042",h_tot=118.000,centro_sfera=107.860,centro_occhi=65.500,sottoponte=81.000,dist_canaline=102.860,diam_occhi=27.000,diam_canaline=29.800,diam_flangia_int=63.000,diam_flangia_est=75.000,diam_sfera=28.000,quota_g=17.100)
codice_L = Forcella(codice_materiale="2150L0046",h_tot=129.800,centro_sfera=117.500,centro_occhi=73.000,sottoponte=88.500,dist_canaline=109.850,diam_occhi=30.200,diam_canaline=33.000,diam_flangia_int=63.000,diam_flangia_est=80.000,diam_sfera=34.000,quota_g=17.100)   
    

# Creo una lista dove verranno aggiunti i codici materiale delle forcelle
codici_forcelle = [codice_G.codice_materiale, codice_L.codice_materiale]
acceso = True

while acceso:
    print("\033c",end="")
    print(Fore.GREEN+logo)
    print(Style.RESET_ALL)
    print("Benvenuto nel Mazak_Helper.\nQui sotto troverai una serie di comandi utili per poter utilizzare lo script in maniera corretta.\n")

    commands=["Attrezzaggio_macchina","Risoluzione Problemi","Comandi_Amministratore","About","Exit"] # Lista comandi principali
    for i in range(len(commands)): # Printo la lista comandi formattata 
        i+=1
        print(f"[{i}]{commands[i-1]}\n")
    print("Seleziona un opzione:\n")
    selezione=str(input(Fore.YELLOW+">>> ")) # Chiedo all'utente quale comando vuole usare
    if selezione == "1":
        print("\033c",end="")
        print(Fore.LIGHTRED_EX+logo_attrezzaggio)
        print(Style.RESET_ALL)
        print(" [ATTREZZAGGIO_MACCHINA]\n\n") 
        print("Inserisci il codice della forcella:\n")
        codice_forcella = str(input(Fore.RED+">>> ")).upper() # Chiedo all'utente il codice della forcella
        print(Fore.RESET)
        for i in codici_forcelle: # Itero per ogni elemento nella lista dei codici delle forcelle
            lista_opzioni = ["[Mandrino_HD1]", "[Torretta_HD1]", "[Mandrino_HD2]", "[Torretta_HD2]", "Robot_Trasportatore","[Attrezzaggio_completo]"]
            numero = 0
            if codice_forcella == codice_G.codice_materiale: # Controllo se il codice dell'utente corrisponde a quello della tipologia "G"
                print(codice_G.show_details()) # Mostro i dettagli della forcella da lavorare
                img_forcella1 = Image.open("forcella_lato1.jpg")
                img_forcella2 = Image.open("forcella_lato2.jpg")
                img_forcella1.show()
                img_forcella2.show()
                for i in lista_opzioni: #Creo un menu, dove chiedo all'utente quale parte dell'attrezzaggio visualizzare 
                    numero += 1
                    print(f"[{numero}] {i}")
                print("\nCosa desideri visualizzare?\n")
                selezione = input(Fore.RED+">>> ")
                print(Fore.RESET)
                if selezione == "1": # se l'utente ha selezionato 1 mostrerò l'attrezzaggio del mandrino hd1
                    attrez_mandrino_hd1(codice_forcella)
                    input(">")
                elif selezione == "2":# se l'utente seleziona 2 mostrerò l'attrezzaggio della torretta hd1
                    attrez_torretta_hd1(codice_forcella)
                    input(">")
                elif selezione == "3":# se l'utente seleziona 3 mostrerò l'attrezzaggio del mandrino hd2
                    attrez_mandrino_hd2(codice_forcella)
                    input(">")
                elif selezione == "4":# se l'utente seleziona 4 mostrerò l'attrezzaggio della torretta hd2
                    attrez_torretta_hd2(codice_forcella)
                    input(">")
                elif selezione == "5":# se l'utente seleziona 5 mostrerò l'attrezzaggio completo del mazak
                    print("\033c",end="")
                    attrez_robot_mazak(codice_forcella)
                    input(">")
                elif selezione == "6":
                    print("\033c",end="")
                    attrezzaggio_forcella(codice_forcella)
                    input(">")
                else:# altrimenti dirò all'utente che il comando non esiste e cesserò il programma
                    print("Comando Inesistente.")
                    input(">")
                break
                    
            elif codice_forcella == codice_L.codice_materiale:
                print(codice_L.show_details())
                for i in lista_opzioni:
                    numero += 1
                    print(f"[{numero}] {i}")
                selezione = input("\nCosa desideri visualizzare?\n>>> ")
                if selezione == "1":
                    attrez_mandrino_hd1(codice_forcella)
                    input(">")
                elif selezione == "2":
                    attrez_torretta_hd1(codice_forcella)
                    input(">")
                elif selezione == "3":
                    attrez_mandrino_hd2(codice_forcella)
                    input(">")
                elif selezione == "4":
                    attrez_torretta_hd2(codice_forcella)
                    input(">")
                elif selezione == "5":
                    print("\033c",end="")
                    attrez_mandrino_hd1(codice_forcella)
                    input(">")
                elif selezione == "6":
                    print("\033c",end="")
                    attrezzaggio_forcella(codice_forcella)
                    input(">")
                else:
                    print(f"Codice {codice_forcella} non Trovato")
                break
        print(Fore.RESET)
    elif selezione == "2":
        print("\033c",end="[RISOLUZIONE_PROBLEMI]\n\n")
        errori=["Relè termico","Malfunz. Controller Robot","Sovraccarico","Door or fence open"]
        tipologia_errore=["Meccanico","Operatore",""]
        n=0
        for i in errori:
            n +=1
            x = f"[{n}] Errore: {i}" 
            print(x)
        problema = input("\nSeleziona il problema.\n>>> ")
        if problema == "1":
            print("")
            pass
        if problema == "2":
            pass
        if problema == "3":
            pass
        if problema == "4":
            pass
    elif selezione == "3":
        print("\033c",end="[COMANDI_AMMINISTRATORE]")
    elif selezione == "4":
        print("\033c",end="[_ABOUT_]\n\n")
    elif selezione == "5":
        print("\033c",end="[_EXIT_]\n\nArrivederci\n\n")
        acceso = False




