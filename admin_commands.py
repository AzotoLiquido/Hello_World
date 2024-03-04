import json

def carica_lista_admin(lista_admin):
    file = open("lista_admin.json","r")
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
        
lista_admin = {}
lista_admin = carica_lista_admin(lista_admin)

login_password = "12304"
login_id = "12304"
