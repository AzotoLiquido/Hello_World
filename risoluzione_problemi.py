import json 

def carica_risoluzione_problemi(risoluzione_problemi):
    file = open("risoluzione_problemi.json","r")
    risoluzione_problemi = json.load(file)
    return risoluzione_problemi

def risoluzione_problema(problema):
    for i in risoluzione_problemi["problemi"]:
        if i == problema:
            print(f"[Nome_problema]: {problema}\n\n[Tipologia_problema]: \n\n{risoluzione_problemi["problemi"][i]["tipologia_problema"]}\n\n[Descrizione_problema]: \n\n{risoluzione_problemi["problemi"][i]["descrizione_problema"]}\n\n[Soluzione_problema]: \n\n{risoluzione_problemi["problemi"][i]["soluzione_problema"]}")
        


risoluzione_problemi={}
risoluzione_problemi=carica_risoluzione_problemi(risoluzione_problemi)

print("\033c",end="")
# problema = "rele_termico"
# print(risoluzione_problemi["problemi"]["rele_termico"]["tipologia_problema"])
# print(risoluzione_problemi["problemi"]["rele_termico"]["descrizione_problema"])
# print(risoluzione_problemi["problemi"]["rele_termico"]["soluzione_problema"])
# risoluzione_problema(problema)