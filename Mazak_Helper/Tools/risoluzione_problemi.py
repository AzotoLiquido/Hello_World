import json

PATH_ERRORS = r"Data\risoluzione_problemi.json"

def salva_risoluzione_problemi(risoluzione_problemi, file_path=PATH_ERRORS):
        with open(file_path, "w") as file:
            json.dump(risoluzione_problemi, file, indent=4)
    
def carica_risoluzione_problemi():
    file = open(PATH_ERRORS,"r")
    risoluzione_problemi = {}
    risoluzione_problemi = json.load(file)
    return risoluzione_problemi

def risoluzione_problema(problema):
    for i in risoluzione_problemi:
        if i == problema:
            print(f"[Nome_problema]: {problema}\n\n[Tipologia_problema]: \n\n{risoluzione_problemi[i]["tipologia_problema"]}\n\n[Descrizione_problema]: \n\n{risoluzione_problemi[i]["descrizione_problema"]}\n\n[Soluzione_problema]: \n\n{risoluzione_problemi[i]["soluzione_problema"]}")

# def aggiungi_errore(risoluzione_problemi,nome_problema,causa_problema,soluzione_problema):
#     risoluzione_problemi["problemi"]["tipologia_problema"]
#     print(risoluzione_problemi)
    

risoluzione_problemi = carica_risoluzione_problemi()
print("\033c",end="")
# carica_risoluzione_problemi(risoluzione_problemi)
# problema = "rele_termico"
# print(risoluzione_problemi["problemi"]["rele_termico"]["tipologia_problema"])
# print(risoluzione_problemi["problemi"]["rele_termico"]["descrizione_problema"])
# print(risoluzione_problemi["problemi"]["rele_termico"]["soluzione_problema"])
# risoluzione_problema(problema)
# salva_risoluzione_problemi()