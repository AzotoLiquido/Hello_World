from logo import logo,logo_attrezzaggio,logo_risol_problemi,logo_admin,logo_bondioli,logo_calcola_quota# Importo i loghi dal file logo
from attrezzaggio import carica_torretta_mazak,carica_mandrino_mazak,attrezzaggio_forcella,attrez_mandrino_hd1,attrez_mandrino_hd2,attrez_torretta_hd1,attrez_torretta_hd2,attrez_robot_mazak,torretta_mazak,mandrino_mazak
from PIL import Image
from risoluzione_problemi import risoluzione_problemi, risoluzione_problema, carica_risoluzione_problemi
from admin_commands import carica_lista_admin,lista_admin,verification_login,formatta_comandi
from aggiusta_quote import *
import os
import sys
import time

def loading_bar(causale, esito):
    timer = 0
    loading = f"{causale}: [--------]"
    backtrack = '\b'*len(loading)

    while timer < 8:
        sys.stdout.write(backtrack + loading)
        sys.stdout.flush()
        loading = loading.replace("-","»",1)
        time.sleep(0.5)
        timer += 1
    time.sleep(0.5)
    sys.stdout.write(backtrack)
    print (loading + esito)

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
ciclo = 0


while acceso:
    ciclo+=1
    print("\033c",end="")
    print(f"{"\033[0;33m"}{logo}{"\033[0m"}")
    if ciclo == 1:
        loading_bar("Caricamento Mazak_Helper in corso","Apertura Mazak_Helper")
    print(f"Benvenuto nel Mazak_Helper.\nQui sotto troverai una serie di comandi utili per poter utilizzare il programma in maniera corretta.\n")

    commands=["Attrezzaggio_macchina","Risoluzione_Problemi","Aggiusta_Quota","Comandi_Amministratore","About","Exit"] # Lista comandi principali
    for i in range(len(commands)): # Printo la lista comandi formattata 
        i+=1
        x = f"[{i}]{commands[i-1]}\n"
        print(x)
    print("Seleziona un opzione:\n")
    selezione=str(input(f"{"\033[0;33m"}>>> ")) # Chiedo all'utente quale comando vuole usare
    print(f"\033[0m")
    if selezione == "1":
        print("\033c",end="")
        print(f"{"\033[0;33m"}{logo_attrezzaggio}{"\033[0m"}")
        print(" [ATTREZZAGGIO_MACCHINA]\n\n") 
        codice_forcella = str(input(f"Inserisci il codice della forcella:\n{"\033[0;33m"}>>> ")).upper() # Chiedo all'utente il codice della forcella
        print("\033[0m")
        for i in codici_forcelle: # Itero per ogni elemento nella lista dei codici delle forcelle
            lista_opzioni = ["[Mandrino_HD1]", "[Torretta_HD1]", "[Mandrino_HD2]", "[Torretta_HD2]", "Robot_Trasportatore","[Attrezzaggio_completo]"]
            numero = 0
            if codice_forcella == codice_G.codice_materiale: # Controllo se il codice dell'utente corrisponde a quello della tipologia "G"
                print(codice_G.show_details()) # Mostro i dettagli della forcella da lavorare
                img_forcella1 = Image.open("forcella_lato1_G.jpg")
                img_forcella2 = Image.open("forcella_lato2_G.jpg")
                img_forcella1.show()
                img_forcella2.show()
                for i in lista_opzioni: #Creo un menu, dove chiedo all'utente quale parte dell'attrezzaggio visualizzare 
                    numero += 1
                    print(f"[{numero}] {i}")
                print("\nCosa desideri visualizzare?\n")
                selezione = input(f"{"\033[0;33m"}>>> ")
                print("\033[0m")
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
                img_forcella1 = Image.open("forcella_lato1_L.jpg")
                img_forcella2 = Image.open("forcella_lato2_L.jpg")
                img_forcella1.show()
                img_forcella2.show()
                for i in lista_opzioni:
                    numero += 1
                    print(f"[{numero}] {i}")
                selezione = input(f"\n{"\033[0;33m"}Cosa desideri visualizzare?\n>>> ")
                print("\033[0m")
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
                input(f"Codice {codice_forcella} non Trovato\n>>> ")  
                break
    elif selezione == "2":
        print("\033c",end="[RISOLUZIONE_PROBLEMI]\n\n")
        print(f"{"\033[0;33m"}{logo_risol_problemi}{"\033[0m"}")
        errori=["Relè termico","Malfunz. Controller Robot","Sovraccarico","Door or fence open"]
        n=0
        for i in errori:
            n +=1
            x = f"[{n}] Errore: {i}" 
            print(x)
        problema = input(f"\nSeleziona il problema.\n{"\033[0;33m"}>>> ")
        print("\033[0m")
        if problema == "1":
            problema = "rele_termico"
            risoluzione_problema(problema)
            input(">")
        if problema == "2":
            problema = "malfunz_controller_robot"
            risoluzione_problema(problema)
            input(">")
        if problema == "3":
            problema = "sovraccarico"
            risoluzione_problema(problema)
            input(">")
        if problema == "4":
            problema = "door_or_fence_open"
            risoluzione_problema(problema)
            input(">")
    elif selezione == "3":
        print("\033c",end="[AGGIUSTA_QUOTE]")
        print("\033[0;33m"+logo_calcola_quota+"\033[0m")
        quote = ["codice_materiale(non modificabile)","altezza_totale","centro_sfera","centro_occhi","sottoponte","distanza_canaline","diametro_occhi","diametro_canaline","diametro_flangia_interno","diametro_flangia esterno","diametro_sfera","quota_G"]
        codice_forcella = str(input(f"inserisci il codice della forcella.{"\033[0;33m"}\n>>> "))
        print("\033[0m")
        for i in range(len(quote)):
            print(f"[{i+1}] {quote[i]}")
        # loading_bar(f"Caricamento misure forcella {codice_forcella}","Caricamento completato")
        for i in codici_forcelle:
            if i == codice_forcella:
                quota = input(f"\nQuale quota desideri sistemare?\n{"\033[0;33m"}>>> ")
                print("\033[0m")
                if quota == "1":
                    print("Non è possibile modificare il codice materiale da questa funzione.")
                if quota == "2":
                    h_tot_attuale = float(input(f"Inserisci l'altezza totale.\n{"\033[0;33m"}>>> "))
                    print("\33[0m")
                    calcola_h_tot(codice_forcella,h_tot_attuale)
                if quota == "3":
                    centro_sfera_attuale = float(input(f"Inserisci la misura del centro sfera.\n{"\033[0;33m"}>>> "))
                    print("\33[0m")
                    calcola_centro_sfera(codice_forcella,centro_sfera_attuale)
                if quota == "4":
                    centro_occhi_attuale = float(input(f"Inserisci la misura del centro occhi.\n{"\033[0;33m"}>>> "))
                    print("\33[0m")
                    calcola_centro_occhi(codice_forcella,centro_occhi_attuale)
                if quota == "5":
                    sottoponte_attuale = float(input(f"Inserisci la misura del sottoponte.\n{"\033[0;33m"}>>> "))
                    print("\33[0m")
                    calcola_sottoponte(codice_forcella,sottoponte_attuale)
                if quota == "6":
                    dist_canaline_attuale = float(input(f"Inserisci la distanza delle canaline.\n{"\033[0;33m"}>>> "))
                    print("\33[0m")
                    calcola_dist_canaline(codice_forcella,dist_canaline_attuale)
                if quota == "7":
                    diam_occhi_attuale = float(input(f"Inserisci il diametro degli occhi.\n{"\033[0;33m"}>>> "))
                    print("\33[0m")
                    calcola_diam_occhi(codice_forcella,diam_occhi_attuale)
                if quota == "8":
                    diam_canaline_attuale = float(input(f"Inserisci il diametro delle canaline.\n{"\033[0;33m"}>>> "))
                    print("\33[0m")
                    calcola_diam_canaline(codice_forcella,diam_canaline_attuale)
                if quota == "9":
                    diam_flangia_int_attuale = float(input(f"Inserisci il diametro interno della flangia.\n{"\033[0;33m"}>>> "))
                    print("\33[0m")
                    calcola_diam_flangia_int(codice_forcella,diam_flangia_int_attuale)
                if quota == "10":
                    diam_flangia_est_attuale = float(input(f"Inserisci il diametro esterno della flangia.\n{"\033[0;33m"}>>> "))
                    print("\33[0m")
                    calcola_diam_flangia_est(codice_forcella,diam_flangia_est_attuale)
                if quota == "11":
                    diam_sfera_attuale = float(input(f"Inserisci il diametro della sfera.\n{"\033[0;33m"}>>> "))
                    print("\33[0m")
                    calcola_diam_sfera(codice_forcella,diam_sfera_attuale)
                if quota == "12":
                    quota_g_attuale = float(input(f"Inserisci il valore della quota G.\n{"\033[0;33m"}>>> "))
                    print("\33[0m")
        input(">")
    elif selezione == "4":
        print("\033c",end="")
        print("\033[0;33m"+logo_admin+"\033[0m")
        login_id = input(f"Inserisci l'admin_ID\n{"\033[0;33m"}>>> ")
        print("\033[0m")              
        login_password = input(f"Inserisci l'admin_password\n{"\033[0;33m"}>>> ")
        print("\033[0m")
        loading_bar("Caricamento lista_admin", "Caricamento dati completato")
        if verification_login(lista_admin,login_id,login_password) == False:
            print("Accesso_Negato.")
        else:
            lista_comandi = ["Aggiungi_forcella","Modifica_forcella","Rimuovi_forcella","Aggiungi_problema","Modifica_problema","Elimina_problema"]
            print("Accesso_Confermato.")
            formatta_comandi(lista_comandi)
            comando = input("\n Seleziona un comando\n>>> ")
            if comando == "1":
                print("\033c",end="")
                print("[Aggiungi_Forcella]")
            if comando == "2":
                print("\033c",end="")
                print("[Modifica_Forcella]")
            if comando == "3":
                print("\033c",end="")
                print("[Rimuovi_Forcella]")
            if comando == "4":
                print("\033c",end="")
                print("[Aggiungi_Problema]")
            if comando == "5":
                print("\033c",end="")
                print("[Modifica_Problema]")
            if comando == "6":
                print("\033c",end="")
                print("[Elimina_Problema]")
        input(">")
    elif selezione == "5":
        print("\033c",end="[_ABOUT_]\n\n")
        print(f"Salve,\nsono Jacopo Diana, sono un ragazzo di 25 anni, recentemente ho cominciato un nuovo percorso sulle macchine a cointrollo numerico,\ncome molti operatori alle prime armi incorro in molti problemi e al contrario di un operatore esperto ci impiego più tempo a risolverli.\nCosi ho pensato che sarebbe stato utile avere uno strumento a disposizione che mi aiuti nei momenti critici,\na tale scopo ho ideato il 'Mazak_Helper'.\n\nE' un programma in grado di aiutare l'operatore in molteplici scenari:\n\n-Attrezzaggio: Aiuta l'operatore elencando tutti i codici necessari all'attrezzaggio di ogni componente del Mazak, mostra il disegno della\n\t{" "*7}forcella da lavorare,elenca tutte le caratteristiche della forcella e da indicazioni precise su questa fase.\n\n-Risoluz Problemi: Aiuta l'operatore in difficoltà elencando vari possibili problemi/guasti della macchina,l'operatore può selezionare\n\t{" "*7}il problema che sta riscontrando e il programma fornirà un analisi dettagliata del problema dando una o più soluzioni.\n\n-Calcola quote: Aiuta l'operatore nel momento in cui necessita di variare qualche quota (X,Y,Z) per poter portare i valori nelle loro quote nominali.")
        print("<Work in progress>")
        input(">")
    elif selezione == "6":
        print("\033c",end="[_EXIT_]\n\nArrivederci\n\n")
        acceso = False




