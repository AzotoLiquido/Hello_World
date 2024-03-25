from Tools.logo import *# Importo i loghi dal file logo
from Tools.attrezzaggio import *
from PIL import Image
from Tools.risoluzione_problemi import risoluzione_problemi, risolvi_problema, carica_elenco_problemi
from Tools.admin_commands import *
from Tools.aggiusta_quote import *
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
    print (loading +" "+ esito)

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
        testo_formattato = f'''
        [Dettagli Forcella]
        
        - Codice_Materiale: {self.codice_materiale}
        - Altezza_totale: {self.h_tot}
        - Centro_Sfera: {self.centro_sfera}
        - Centro_occhi: {self.centro_occhi}
        - Sottoponte: {self.sottoponte}
        - Distanza_canaline: {self.dist_canaline}
        - Diametro_occhi: {self.diam_occhi}
        - Diametro_canaline: {self.diam_canaline}
        - Diametro_interno_flangia: {self.diam_flangia_int}
        - Diametro_esterno_flangia: {self.diam_flangia_est}
        - Diametro_sfera: {self.diam_sfera}
        - Quota_'G': {self.quota_g}'''
        delimitatore = "_"*50
        return f"\n{delimitatore}\n{testo_formattato}\n{delimitatore}\n"
    
# #Creo degli oggetti Forcella d'esempio.
codice_G = Forcella(codice_materiale="2150G0042",h_tot=118.000,centro_sfera=107.860,centro_occhi=65.500,sottoponte=81.000,dist_canaline=102.860,diam_occhi=27.000,diam_canaline=29.800,diam_flangia_int=63.000,diam_flangia_est=75.000,diam_sfera=28.000,quota_g=17.100)
codice_L = Forcella(codice_materiale="2150L0046",h_tot=129.800,centro_sfera=117.500,centro_occhi=73.000,sottoponte=88.500,dist_canaline=109.850,diam_occhi=30.200,diam_canaline=33.000,diam_flangia_int=63.000,diam_flangia_est=80.000,diam_sfera=34.000,quota_g=17.100)   

risoluzione_problemi = carica_elenco_problemi()
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
            lista_opzioni = ["[Mandrino HD1-HD2]", "[Torretta_HD1-HD2]", "Robot_Trasportatore","[Attrezzaggio_completo]"]
            lista_display = [display_mandrino,display_torretta,display_robot,display_forcella]
            if codice_forcella == codice_G.codice_materiale: # Controllo se il codice dell'utente corrisponde a quello della tipologia "G"
                display_dimensioni(codice_forcella)# Mostro i dettagli della forcella da lavorare
                img_forcella1 = Image.open(r"Media\forcella_lato1_G.jpg")
                img_forcella2 = Image.open(r"Media\forcella_lato2_G.jpg")
                img_forcella1.show()
                img_forcella2.show()
                for i in enumerate(lista_opzioni): #Creo un menu, dove chiedo all'utente quale parte dell'attrezzaggio visualizzare 
                    print(f"[{i[0]+1}] {i[1]}")
                print("\nCosa desideri visualizzare?\n")
                selezione = lista_display[int(input(f"{"\033[0;33m"}>>> "))-1](codice_forcella)
                print("\033[0m")
                input(">")
                break   
            elif codice_forcella == codice_L.codice_materiale:
                display_dimensioni(codice_forcella)
                img_forcella1 = Image.open("forcella_lato1_L.jpg")
                img_forcella2 = Image.open("forcella_lato2_L.jpg")
                img_forcella1.show()
                img_forcella2.show()
                for i in enumerate(lista_opzioni):
                    print(f"[{i[0]+1}] {i[1]}")
                selezione = lista_display[int(input(f"\n{"\033[0;33m"}Cosa desideri visualizzare?\n>>> "))-1]
                print("\033[0m")
                input(">")
            else:
                input(f"Codice {codice_forcella} non Trovato\n>>> ")  
                break
    elif selezione == "2":
        print("\033c",end="")
        print(f"{"\033[0;33m"}{logo_risol_problemi}{"\033[0m"}")
        problemi=[]
        for i in enumerate(risoluzione_problemi):
            print(f"[{i[0]+1}] Errore: {i[1]}") 
            problemi.append(i[1])
        problema = problemi[int(input(f"\nSeleziona il problema.\n{"\033[0;33m"}>>> "))-1]
        print("\033[0m")
        risolvi_problema(problema)
        input(">")
    elif selezione == "3":
        print("\033c",end="[CALCOLA_CORREZIONE]")
        print("\033[0;33m"+logo_calcola_quota+"\033[0m")
        quote = {
            "Altezza Totale" : "h_tot",
            "Centro Sfera": "centro_sfera",
            "Centro Occhi": "centro_occhi",
            "Sottoponte": "sottoponte",
            "Distanza Canaline": "dist_canaline",
            "Diametro Occhi": "diam_occhi",
            "Diametro Canaline": "diam_canaline",
            "Diametro Flangia Interno": "diam_flangia_int",
            "Diametro Flangia Esterno": "diam_flangia est",
            "Diametro Sfera": "diam_sfera",
            "Quota G": "quota_g"
        }
        lista_quote = ["Altezza Totale", "Centro Sfera", "Centro Occhi", "Sottoponte", "Distanza Canaline", "Diametro Occhi", "Diametro Canaline", "Diametro Flangia Interno", "Diametro Flangia Esterno", "Diametro Sfera", "Quota G"]
        codice_forcella = str(input(f"inserisci il codice della forcella.{"\033[0;33m"}\n>>> "))
        print("\033[0m")
        forcelle = json.load(open(r"Data\forcelle.json","r"))
        forcella = forcelle[codice_forcella]
        for i in range(len(lista_quote)):
            print(f"[{i+1}] {lista_quote[i]}")
        # loading_bar(f"Caricamento misure forcella {codice_forcella}","Caricamento completato")
        quota = int(input(f"\nQuale quota desideri sistemare?\n{"\033[0;33m"}>>> ")) - 1
        print("\033[0m")
        dimensione_scelta = quote[lista_quote[quota]]
        misura_attuale = float(input(f"Inserisci misura attuale di {lista_quote[quota]}\n{"\033[0;33m"}>>> "))
        print("\033[0m")
        calcola_correzione(forcella, dimensione_scelta, misura_attuale)   
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
            print("Accesso_Confermato.")
            richiama_comandi()
        input(">")
    elif selezione == "5":
        print("\033c",end="[_ABOUT_]\n\n")
        print("W.I.P")
        # print(f"Salve,\nsono Jacopo Diana, sono un ragazzo di 25 anni, recentemente ho cominciato un nuovo percorso sulle macchine a cointrollo numerico,\ncome molti operatori alle prime armi incorro in molti problemi e al contrario di un operatore esperto ci impiego più tempo a risolverli.\nCosi ho pensato che sarebbe stato utile avere uno strumento a disposizione che mi aiuti nei momenti critici,\na tale scopo ho ideato il 'Mazak_Helper'.\n\nE' un programma in grado di aiutare l'operatore in molteplici scenari:\n\n-Attrezzaggio: Aiuta l'operatore elencando tutti i codici necessari all'attrezzaggio di ogni componente del Mazak, mostra il disegno della\n\t{" "*7}forcella da lavorare,elenca tutte le caratteristiche della forcella e da indicazioni precise su questa fase.\n\n-Risoluz Problemi: Aiuta l'operatore in difficoltà elencando vari possibili problemi/guasti della macchina,l'operatore può selezionare\n\t{" "*7}il problema che sta riscontrando e il programma fornirà un analisi dettagliata del problema dando una o più soluzioni.\n\n-Calcola quote: Aiuta l'operatore nel momento in cui necessita di variare qualche quota (X,Y,Z) per poter portare i valori nelle loro quote nominali.")
        input(">")  
    elif selezione == "6":
        print("\033c",end="")
        print(logo_chiusura)
        acceso = False




