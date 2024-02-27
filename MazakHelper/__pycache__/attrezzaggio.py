import json

def carica_torretta_mazak(torretta_mazak):
    file = open("torretta_mazak.json","r")
    torretta_mazak = json.load(file)
    return torretta_mazak

def carica_mandrino_mazak(mandrino_mazak):
    file = open("mandrino_mazak.json","r")
    mandrino_mazak = json.load(file)
    return mandrino_mazak

def attrez_torretta_hd1():
    for i in torretta_mazak["hd1"]:
        x = f"| [{i}]:  {torretta_mazak["hd1"][i]} |"
        if i == "T1":
            x = f"{separatore}\n| [{i}]:  {torretta_mazak["hd1"][i]} |"
        elif len(x) > 74:
            x = f"| [{i}]: {torretta_mazak["hd1"][i]} |"
            if i == "T12":
                x = f"| [{i}]: {torretta_mazak["hd1"][i]} |\n{separatore}"
        print(x)
        

def attrez_torretta_hd2():
    for i in torretta_mazak["hd2"]:
        x = f"| [{i}]:  {torretta_mazak["hd2"][i]} |"
        if i == "T1":
            x = f"{separatore}\n| [{i}]:  {torretta_mazak["hd2"][i]} |"
        elif len(x) > 74:
            x = f"| [{i}]: {torretta_mazak["hd2"][i]} |"
            if i == "T12":
                x = f"| [{i}]: {torretta_mazak["hd1"][i]} |\n{separatore}"
        print(x)

def attrez_mandrino_hd1():
    for i in mandrino_mazak["hd1"]:
        x = f"| [{i}]: {mandrino_mazak["hd1"][i]}|"
        if i == "codice_morsa_A":
            x = f"{separatore}\n| [{i}]: {mandrino_mazak["hd1"][i]:>52} |\n|{"|":>73}"
        elif i == "codice_morsa_B":
            x = f"| [{i}]: {mandrino_mazak["hd1"][i]:>52} |\n{separatore}"
        elif i == "codice_appoggio":
            x = f"| [{i}]: {mandrino_mazak["hd1"][i]:>51} |\n|{"|":>73}"
        elif i == "codice_centraggio_sfera":
            x = f"| [{i}]: {mandrino_mazak["hd1"][i]:>43} |\n{separatore}"
        print(x)

def attrez_mandrino_hd2():
    for i in mandrino_mazak["hd2"]:
        x = f"| [{i}]: {mandrino_mazak["hd2"][i]}|"
        if i == "codice_staffe":
            x = f"{separatore}\n| [{i}]: {mandrino_mazak["hd2"][i]:>53} |"
        elif i == "codice_appoggio":
            x = f"| [{i}]: {mandrino_mazak["hd2"][i]:>51} |"
        elif i == "codice_cono_centr":
            x = f"| [{i}]: {mandrino_mazak["hd2"][i]:>49} |\n{separatore}"
        print(x)


def attrezzaggio_forcella():
    print(f"\n{separatore}\n|{"[Torretta_Mazak]:HD1-HD2":^72}|\n{separatore}\n|{"[HD1]":^72}|\n{separatore}")
    attrez_torretta_hd1()
    print(f"{separatore}\n|{"[HD2]":^72}|\n{separatore}")
    attrez_torretta_hd2()
    print(f"{separatore}\n|{"[Mandrino_Mazak]:HD1-HD2":^72}|\n{separatore}")
    print(f"| {"HD1":^71}|\n{separatore}")
    attrez_mandrino_hd1()
    print(f"{separatore}\n| {"HD2":^71}|\n{separatore}")
    attrez_mandrino_hd2()


separatore = "-"*74
mandrino_mazak = {}
mandrino_mazak = carica_mandrino_mazak(mandrino_mazak)
torretta_mazak = {}
torretta_mazak = carica_torretta_mazak(torretta_mazak)

attrezzaggio_forcella()
# attrez_torretta_hd1()
# attrez_mandrino_hd2()