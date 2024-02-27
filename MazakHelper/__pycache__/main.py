from logo import logo # Importo il logo dal file logo
import os # Importo la libreria os
from attrezzaggio import carica_torretta_mazak,carica_mandrino_mazak,attrezzaggio_forcella,attrez_mandrino_hd1,attrez_mandrino_hd2,attrez_torretta_hd1,attrez_torretta_hd2

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
torretta_mazak = {}
torretta_mazak = carica_torretta_mazak(torretta_mazak)
mandrino_mazak = {}
mandrino_mazak = carica_mandrino_mazak(mandrino_mazak)

print("\033c",end="")
print(logo)
print("Benvenuto nel Mazak_Helper.\nQui sotto troverai una serie di comandi utili per poter utilizzare lo script in maniera corretta.")

commands=["Attrezzaggio_macchina","Risoluzione Problemi","Admin_Commands","About","Exit"] # Lista comandi principali
for i in range(len(commands)): # Printo la lista comandi formattata 
    i+=1
    print(f"[{i}]{commands[i-1]}")
selezione=str(input("Seleziona un numero:\n>>> ")) # Chiedo all'utente quale comando vuole usare
if selezione == "1":
    os.system("cls")
    print(" [ATTREZZAGGIO_MACCHINA]\n\n") 
    codice_forcella = str(input("Inserisci il codice della forcella:\n>>> ")) # Chiedo all'utente il codice della forcella
    # codice_forcella = "2150G0042" #codice debugging(da cancellare)
    for i in codici_forcelle:
        print("\033c",end="")
        if codice_forcella == i:
            print("Trovato.")
            if i == codice_G.codice_materiale:
                print(codice_G.show_details())
                lista_opzioni = ["[Mandrino_HD1]", "[Torretta_HD1]", "[Mandrino_HD2]", "[Torretta_HD2]", "[Attrezzaggio_completo]"]
                numero = 0
                for i in lista_opzioni:
                    numero += 1
                    print(f"[{numero}] {i}")
                selezione = input("\nCosa desideri visualiizare?\n>>> ")
                if selezione == "1":
                    attrez_mandrino_hd1()
                elif selezione == "2":
                    attrez_torretta_hd1()
                elif selezione == "3":
                    attrez_mandrino_hd2()
                elif selezione == "4":
                    attrez_torretta_hd2()
                elif selezione == "5":
                    attrezzaggio_forcella()
                else:
                    print("Comando Inesistente.")
                    break
            elif i == codice_L.codice_materiale:
                print(codice_L.show_details())
            break 
        else:
            print("Non Trovato")
    pass
elif selezione == "2":
    os.system("cls")
    print("[RISOLUZIONE_PROBLEMI]\n\n")
    problema = input("Inserisci il testo del problema.\n>>> ")
    pass
elif selezione == "3":
    os.system("cls")
    print("[ADMIN'S_CONTROL_PANEL]")
elif selezione == "4":
    os.system("cls")
    print("[_ABOUT_]\n\n")
    print()
    pass
elif selezione == "5":
    os.system("cls")
    print("[_EXIT_]\n\nArrivederci\n\n")
    os.system("exit")
    pass