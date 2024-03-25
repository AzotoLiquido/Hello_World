import json

PATH_ADMIN = r"Data\lista_admin.json"
PATH_FORCELLE = r"Data\forcelle.json"

# def salva_dati(nome_file):          DA FARE
#     file = open(nome_file,"w")
#     json.dump

def carica_dati(nome_file):
    file = open(nome_file, "r")
    return json.load(file)

def verification_login(lista_admin,login_id,login_password):
    for i in lista_admin["admin"]["id"]:
        if login_id == lista_admin["admin"]["id"] and login_password == lista_admin["admin"]["password"]:
            print("ID trovato")
            return True
        else:
            print("ID non trovato")
            return False

def richiama_comandi():
  dict_comandi = {
    "aggiungi_forcella":aggiungi_forcella,
    "modifica_forcella":modifica_forcella,
    "elimina_forcella":elimina_forcella,
    "aggiungi_problema":"comando_4",
    "modifica_problema":"comando_5",
    "elimina_problema":"comando_6"
}
  lista_comandi = []
  # Mostra menu:
  print("Menù admin")
  for i, c in enumerate(dict_comandi):
      print( f"[{i + 1}] - {c.title()}")
      lista_comandi.append(c)
  numero_comando = int(input("Scegli il comando.\n>>>")) - 1
  chiave = lista_comandi[numero_comando]
  comando = dict_comandi[chiave]
  comando()

def aggiungi_dimensioni_forcella(): #Iteratore dimensioni forcella
    for i in forcella["dimensioni"]:
        n=0
        input_utente = input(f"Inserisci {i}:\n>>> ").upper().split("-")
        for x in forcella["dimensioni"][i]:
            forcella["dimensioni"][i][x] = input_utente[n]
            n+=1
    print(forcella["dimensioni"])

def aggiungi_codici_torretta(): # Iteratore codici torretta
    for i in forcella["codici"]["torretta"]:
        print(i)
        for x in forcella["codici"]["torretta"][i]:
            n=0
            codice = input(f"inserisci il codice relativo a {x}\n>>> ").upper().split("-")
            for y in forcella["codici"]["torretta"][i][x]:
                forcella["codici"]["torretta"][i][x][y] = codice[n]
                n+=1
    print(forcella["codici"]["torretta"])

def aggiungi_codici_mandrino(): # Iteratore codici mandrino
    for i in forcella["codici"]["mandrino"]:
        for x in forcella["codici"]["mandrino"][i]:
            codice = input(f"inserisci il codice relativo a {x}\n>>> ")
            forcella["codici"]["mandrino"][i][x] = codice
    print(forcella["codici"]["mandrino"])

def aggiungi_codici_robot_tempra_nastro(sottogruppo): # Iteratore codici robot/tempra/nastro
    for i in forcella["codici"][sottogruppo]:
        codice = input(f"inserisci il codice relativo a {i}\n>>> ")
        forcella["codici"][sottogruppo][i] = codice
    print(forcella["codici"][sottogruppo])

def aggiungi_forcella():
    aggiungi_codici_torretta()
    aggiungi_codici_mandrino()
    aggiungi_codici_robot_tempra_nastro("robot")
    aggiungi_codici_robot_tempra_nastro("tempra")
    aggiungi_codici_robot_tempra_nastro("nastro_caricatore")
    aggiungi_dimensioni_forcella()

def modifica_forcella():
    codice_forcella = input("inserisci il codice della forcella\n>>> ".capitalize()).upper()
    lista_forcelle.get(codice_forcella)
    for i in enumerate(lista_forcelle[codice_forcella]):
        print(f"[{i[0]+1}]: {i[1].title()}")
    sezione = input("seleziona la sezione da modificare\n>>> ".capitalize())
    if sezione == "1":
        macchine = []
        for i in enumerate(lista_forcelle[codice_forcella]["codici"]): #lista_forcelle = (n, i)
            print(f"[{i[0]+1}]: {i[1].title()}")
            macchine.append(i[1])
        macchina = macchine[int(input("seleziona la macchina da modificare\n>>> ".capitalize()))-1]
        gemelli = []
        for i in enumerate(lista_forcelle[codice_forcella]["codici"][macchina]):
            print(f"[{i[0]+1}]: {i[1].upper()}")
            gemelli.append(i[1])
        gemello = gemelli[int(input("quale gemello desideri modificare?\n>>> ".capitalize()))-1]
        bracci = []
        for i in enumerate(lista_forcelle[codice_forcella]["codici"][macchina][gemello]):
            print(f"[{i[0]+1}]: {i[1].upper()}")
            bracci.append(i[1])
        braccio = bracci[int(input("seleziona il braccio da modificare".capitalize()))-1]
        caratteristiche = []
        for i in enumerate(lista_forcelle[codice_forcella]["codici"][macchina][gemello][braccio]):
            print(f"[{i[0]+1}]: {i[1]}")
            caratteristiche.append(i[1])
        caratteristica = caratteristiche[int(input("seleziona la caratteristica vuoi modificare".capitalize()))-1]
        codice_caratteristica = input(f"digita il codice {caratteristica}(Ex. UTLI 1234)\n>>> ".capitalize()).upper()
        lista_forcelle[codice_forcella]["codici"][macchina][gemello][braccio][caratteristica] = codice_caratteristica
    if sezione == "2":
        dimensioni = []
        for i in enumerate(lista_forcelle[codice_forcella]["dimensioni"]):
            print(f"[{i[0]+1}]: {i[1]}")
            dimensioni.append(i[1])
        dimensione = dimensioni[int(input("seleziona la dimensione da modificare\n>>> ".capitalize()))-1]
        caratteristiche = []
        for i in enumerate(lista_forcelle[codice_forcella]["dimensioni"][dimensione]):
            print(f"[{i[0]+1}]: {i[1]}")
            caratteristiche.append(i[1])
        caratteristica = caratteristiche[int(input("seleziona la caratteristica da modificare\n>>> ".capitalize()))-1]
        print(f"Vecchio valore: {lista_forcelle[codice_forcella]["dimensioni"][dimensione][caratteristica]}")
        valore = float(input(f"digita il valore {caratteristica}\n>>> "))
        input("non è stato digitato nessun valore\n>>> ".capitalize())
        lista_forcelle[codice_forcella]["dimensioni"][dimensione][caratteristica] = valore
        print(f"Nuovo valore: {lista_forcelle[codice_forcella]["dimensioni"][dimensione][caratteristica]}")

def elimina_forcella(codice_forcella):
    lista_forcelle.pop(codice_forcella)

forcella ={
      "codici": {
        "torretta": {
          "hd1": {
            "t1": {"utensile": None, "inserto": None},
            "t2": {"utensile": None, "inserto": None},
            "t3": {"utensile": None, "inserto": None},
            "t4": {"utensile": None, "inserto": None},
            "t5": {"utensile": None, "inserto": None},
            "t6": {"utensile": None, "inserto": None},
            "t7": {"utensile": None, "inserto": None},
            "t8": {"utensile": None, "inserto": None},
            "t9": {"utensile": None, "inserto": None},
            "t10": {"utensile": None, "inserto": None},
            "t11": {"utensile": None, "inserto": None},
            "t12": {"utensile": None, "inserto": None}
          },
          "hd2": {
            "t1": {"utensile": None, "inserto": None},
            "t2": {"utensile": None, "inserto": None},
            "t3": {"utensile": None, "inserto": None},
            "t4": {"utensile": None, "inserto": None},
            "t5": {"utensile": None, "inserto": None},
            "t6": {"utensile": None, "inserto": None},
            "t7": {"utensile": None, "inserto": None},
            "t8": {"utensile": None, "inserto": None},
            "t9": {"utensile": None, "inserto": None},
            "t10": {"utensile": None, "inserto": None},
            "t11": {"utensile": None, "inserto": None},
            "t12": {"utensile": None, "inserto": None}
          }
        },
        "mandrino": {
          "hd1": {
            "morsa_A": None,
            "morsa_B": None,
            "appoggio": None,
            "centraggio_sfera": None
          },
          "hd2": {
            "staffe": None,
            "appoggio": None,
            "cono_centr": None
          }
        },
        "robot": {
          "morse_bloccaggio": {
            "flangia": None,
            "sfera": None
          },
          "setup_n": None,
          "programma_n": None
        },
        "tempra": {
          "indotto":None,
          "base_flangia":None,
          "programma_n":None
        },
        "nastro_caricatore":{
          "diam_pezzo": None,
          "arretramento": None,
          "pz_per_fila": None
        }
      },
      "dimensioni":{
        "h_tot":{
            "max": None,
            "min": None,
            "asse_rif": None,
            "tendenza": None
        
        },
        "centro_sfera": {
            "max": None,
            "min": None,
            "asse_rif": None,
            "tendenza": None
        },
        "centro_occhi":{
            "max": None,
            "min": None,
            "asse_rif": None,
            "tendenza": None
        },
        "sottoponte":{
            "max": None,
            "min": None,
            "asse_rif": None,
            "tendenza": None
        },
        "dist_canaline":{
            "max": None,
            "min": None,
            "asse_rif": None,
            "tendenza": None
        },
        "diam_occhi":{
            "max": None,
            "min": None,
            "asse_rif": None,
            "tendenza": None
        },
        "diam_canaline":{
            "max": None,
            "min": None,
            "asse_rif": None,
            "tendenza": None
        },
        "diam_flangia_int":{
            "max": None,
            "min": None,
            "asse_rif": None,
            "tendenza": None
        },
        "diam_flangia_est":{
            "max": None,
            "min": None,
            "asse_rif": None,
            "tendenza": None
        },
        "diam_sfera":{
            "max": None,
            "min": None,
            "asse_rif": None,
            "tendenza": None
        },
        "quota_g":{
            "max": None,
            "min": None,
            "asse_rif": None,
            "tendenza": None
        }
      }
    }

lista_admin = carica_dati(PATH_ADMIN)


lista_forcelle = carica_dati(PATH_FORCELLE)

# modifica_forcella("2150G0042")

# richiama_comandi()