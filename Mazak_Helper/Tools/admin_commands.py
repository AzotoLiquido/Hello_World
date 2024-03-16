import json

PATH_ADMIN = r"Data\lista_admin.json"

def carica_lista_admin():
    file = open(PATH_ADMIN,"r")
    lista_admin = json.load(file)
    return lista_admin

def verification_login(lista_admin,login_id,login_password):
    for i in lista_admin["admin"]["id"]:
        if login_id == lista_admin["admin"]["id"] and login_password == lista_admin["admin"]["password"]:
            print("ID trovato")
            return True
        else:
            print("ID non trovato")
            return False

def formatta_comandi(lista):
    n=0
    for i in lista:
        n+=1
        print(f"[{n}] {i}")

def aggiungi_forcella(codice_forcella, h_tot,centro_sfera,centro_occhi,sottoponte,dist_canaline,diam_occhi,diam_canaline,diam_flangia_int,diam_flangia_est,diam_sfera,quota_g):
    file = open(r"Data\forcelle.json","w")

lista_admin = carica_lista_admin()


# aggiungi_errore(risoluzione_problemi,"prova1")
# print(risoluzione_problemi)
# login_password = "12304"
# login_id = "12304"
