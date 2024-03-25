import json

# Path per il database della risoluzione problemi
PATH_ERRORS = r"Data\risoluzione_problemi.json"


# funzione di salvataggio per sovrascrivere i dati relativi alla risoluzione problemi
def salva_elenco_problemi(data):
    with open(PATH_ERRORS, "w") as file:
        json.dump(data, file, indent=4)


# funzione per il caricamento dei dati relativi alla risoluzione problemi
def carica_elenco_problemi() -> dict:
    file = open(PATH_ERRORS, "r")
    data = json.load(file)
    return data


# funzione che mostra a scherzo la soluzione se il problema viene trovato nel database
def risolvi_problema(problema):
    frase = ""
    for nome_problema in risoluzione_problemi:
        if nome_problema == problema:
            frase: str = f"""
[Nome_problema]:

{problema}
            
[Tipologia_problema]:

{risoluzione_problemi[nome_problema]["tipologia_problema"]}
            
[Descrizione_problema]:

{risoluzione_problemi[nome_problema]["descrizione_problema"]}
            
[Soluzione_problema]:

{risoluzione_problemi[nome_problema]["soluzione_problema"]}"""
    if frase:
        print(frase)
    else:
        print("Nome problema non trovato nel database.\nSpiacenti, la soluzione non può essere fornita.")


risoluzione_problemi = carica_elenco_problemi()
print("\033c", end="")
