# MISURA
def check_misura(forcella: dict, dimensione: str, misura: float) -> str:
    if misura > forcella["dimensioni"][dimensione]["max"]:
        return "maggiorato"
    elif misura < forcella["dimensioni"][dimensione]["min"]:
        return "minorato"
    else:
        return "conforme"


# CORREZIONE
def calcola_correzione(forcella: dict, dimensione: str, misura: float):
    differenza = forcella["dimensioni"][dimensione]["tendenza"] - misura
    diagnosi = check_misura(forcella, dimensione, misura)

    print(f"Valore {dimensione} : {diagnosi}\n"
          f"Correzione : {forcella['dimensioni'][dimensione]['asse_rif']} {differenza:+.3f}")
    if diagnosi == "conforme":
        if abs(forcella["dimensioni"][dimensione]["max"] - misura) < abs(forcella["dimensioni"][dimensione]["min"] - misura):
            print("Nonostante la conformità si consiglia la correzione.")


import json

forcelle = json.load(open(r"Data\forcelle.json", "r"))

forcella = forcelle["2150G0042"]

# calcola_correzione(forcella, "diam_sfera", 27.958)


# diam_sfera = float(input("Inserisci diam_sfera."))
# calcola_diam_sfera("2150G0042",diam_sfera)
# diam_canaline = 29.9
#1.. print(misura_diam_canaline("2150G0042",diam_canaline))