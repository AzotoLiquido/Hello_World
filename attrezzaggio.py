import json

def carica_torretta_mazak(torretta_mazak): #carico i dati dal file 'torretta_mazak.json'
    file = open("torretta_mazak.json","r")
    torretta_mazak = json.load(file)
    return torretta_mazak

def carica_mandrino_mazak(mandrino_mazak): #carico i dati dal file 'mandrino_mazak.json'
    file = open("mandrino_mazak.json","r")
    mandrino_mazak = json.load(file)
    return mandrino_mazak

def carica_robot_mazak(robot_mazak): #carico i dati dal file 'robot_mazak.json'
    file = open("robot_mazak.json","r")
    robot_mazak = json.load(file)
    return robot_mazak

def attrez_torretta_hd1(codice_forcella):
    if codice_forcella == "2150G0042":
        torretta_mazak["hd1"]["T1"]["Codice_utensile"]="UTSN 065"
        torretta_mazak["hd1"]["T1"]["Codice_inserto"]="UTLI 1201"
        torretta_mazak["hd1"]["T2"]["Codice_utensile"]="--------"
        torretta_mazak["hd1"]["T2"]["Codice_inserto"]="---------"
        torretta_mazak["hd1"]["T3"]["Codice_utensile"]="UTSN 343"
        torretta_mazak["hd1"]["T3"]["Codice_inserto"]="UTLI 1198"
        torretta_mazak["hd1"]["T4"]["Codice_utensile"]="--------"
        torretta_mazak["hd1"]["T4"]["Codice_inserto"]="---------"
        torretta_mazak["hd1"]["T5"]["Codice_utensile"]="UTSN 104"
        torretta_mazak["hd1"]["T5"]["Codice_inserto"]="UTLI  526"
        torretta_mazak["hd1"]["T6"]["Codice_utensile"]="--------"
        torretta_mazak["hd1"]["T6"]["Codice_inserto"]="---------"
        torretta_mazak["hd1"]["T7"]["Codice_utensile"]="UPTI 180"
        torretta_mazak["hd1"]["T7"]["Codice_inserto"]="UTLI  221"
        torretta_mazak["hd1"]["T8"]["Codice_utensile"]="UTSN 104"
        torretta_mazak["hd1"]["T8"]["Codice_inserto"]="UTLI 1198"
        torretta_mazak["hd1"]["T9"]["Codice_utensile"]="UTSN 065"
        torretta_mazak["hd1"]["T9"]["Codice_inserto"]="UTLI 1201"
        torretta_mazak["hd1"]["T10"]["Codice_utensile"]="UTSN 065"
        torretta_mazak["hd1"]["T10"]["Codice_inserto"]="UTLI  526"
        torretta_mazak["hd1"]["T11"]["Codice_utensile"]="UPTI 180"
        torretta_mazak["hd1"]["T11"]["Codice_inserto"]="UTLI  219"
        torretta_mazak["hd1"]["T12"]["Codice_utensile"]="UPTI 180"
        torretta_mazak["hd1"]["T12"]["Codice_inserto"]="UTLI  219"
        for i in torretta_mazak['hd1']:
            x = f"| [{i}]:  {torretta_mazak['hd1'][i]}  |"
            if i == "T1":
                x = f"{separatore}\n| [{i}]:  {torretta_mazak['hd1'][i]}  |"
            elif len(x) > 74:
                x = f"| [{i}]: {torretta_mazak['hd1'][i]}  |"
                if i == "T12":
                    x = f"| [{i}]: {torretta_mazak['hd1'][i]}  |\n{separatore}"
            print(x)
    elif codice_forcella == "2150L0046":        
        torretta_mazak["hd1"]["T1"]["Codice_utensile"]="UTSN 06x"
        torretta_mazak["hd1"]["T1"]["Codice_inserto"]="UTLI 120x"
        torretta_mazak["hd1"]["T2"]["Codice_utensile"]="-------x"
        torretta_mazak["hd1"]["T2"]["Codice_inserto"]="--------x"
        torretta_mazak["hd1"]["T3"]["Codice_utensile"]="UTSN 34x"
        torretta_mazak["hd1"]["T3"]["Codice_inserto"]="UTLI 119x"
        torretta_mazak["hd1"]["T4"]["Codice_utensile"]="-------x"
        torretta_mazak["hd1"]["T4"]["Codice_inserto"]="--------x"
        torretta_mazak["hd1"]["T5"]["Codice_utensile"]="UTSN 10x"
        torretta_mazak["hd1"]["T5"]["Codice_inserto"]="UTLI  52x"
        torretta_mazak["hd1"]["T6"]["Codice_utensile"]="-------x"
        torretta_mazak["hd1"]["T6"]["Codice_inserto"]="--------x"
        torretta_mazak["hd1"]["T7"]["Codice_utensile"]="UPTI 18x"
        torretta_mazak["hd1"]["T7"]["Codice_inserto"]="UTLI  22x"
        torretta_mazak["hd1"]["T8"]["Codice_utensile"]="UTSN 10x"
        torretta_mazak["hd1"]["T8"]["Codice_inserto"]="UTLI 119x"
        torretta_mazak["hd1"]["T9"]["Codice_utensile"]="UTSN 06x"
        torretta_mazak["hd1"]["T9"]["Codice_inserto"]="UTLI 120x"
        torretta_mazak["hd1"]["T10"]["Codice_utensile"]="UTSN 05x"
        torretta_mazak["hd1"]["T10"]["Codice_inserto"]="UTLI  52x"
        torretta_mazak["hd1"]["T11"]["Codice_utensile"]="UPTI 18x"
        torretta_mazak["hd1"]["T11"]["Codice_inserto"]="UTLI  21x"
        torretta_mazak["hd1"]["T12"]["Codice_utensile"]="UPTI 18x"
        torretta_mazak["hd1"]["T12"]["Codice_inserto"]="UTLI  21x"
        for i in torretta_mazak['hd1']:
            x = f"| [{i}]:  {torretta_mazak['hd1'][i]}  |"
            if i == "T1":
                x = f"{separatore}\n| [{i}]:  {torretta_mazak['hd1'][i]}  |"
            elif len(x) > 74:
                x = f"| [{i}]: {torretta_mazak['hd1'][i]}  |"
                if i == "T12":
                    x = f"| [{i}]: {torretta_mazak['hd1'][i]}  |\n{separatore}"
            print(x)
    else:
        print(f"Codice [{codice_forcella}] non trovato.\n")
        
def attrez_torretta_hd2(codice_forcella):
    if codice_forcella == "2150G0042":
        torretta_mazak["hd2"]["T1"]["Codice_utensile"]="UTSN 064"
        torretta_mazak["hd2"]["T1"]["Codice_inserto"]="UTLI 1201"
        torretta_mazak["hd2"]["T2"]["Codice_utensile"]="--------"
        torretta_mazak["hd2"]["T2"]["Codice_inserto"]="---------"
        torretta_mazak["hd2"]["T3"]["Codice_utensile"]="UTSN 214"
        torretta_mazak["hd2"]["T3"]["Codice_inserto"]="UTLI  321"
        torretta_mazak["hd2"]["T4"]["Codice_utensile"]="--------"
        torretta_mazak["hd2"]["T4"]["Codice_inserto"]="---------"
        torretta_mazak["hd2"]["T5"]["Codice_utensile"]="UTSN 214"
        torretta_mazak["hd2"]["T5"]["Codice_inserto"]="UTLI  170"
        torretta_mazak["hd2"]["T6"]["Codice_utensile"]="--------"
        torretta_mazak["hd2"]["T6"]["Codice_inserto"]="---------"
        torretta_mazak["hd2"]["T7"]["Codice_utensile"]="--------"
        torretta_mazak["hd2"]["T7"]["Codice_inserto"]="---------"
        torretta_mazak["hd2"]["T8"]["Codice_utensile"]="--------"
        torretta_mazak["hd2"]["T8"]["Codice_inserto"]="---------"
        torretta_mazak["hd2"]["T9"]["Codice_utensile"]="UTLN 694"
        torretta_mazak["hd2"]["T9"]["Codice_inserto"]="UFRZ  271"
        torretta_mazak["hd2"]["T10"]["Codice_utensile"]="UTSN 275"
        torretta_mazak["hd2"]["T10"]["Codice_inserto"]="UALC  045"
        torretta_mazak["hd2"]["T11"]["Codice_utensile"]="--------"
        torretta_mazak["hd2"]["T11"]["Codice_inserto"]="---------"
        torretta_mazak["hd2"]["T12"]["Codice_utensile"]="--------"
        torretta_mazak["hd2"]["T12"]["Codice_inserto"]="---------"
        for i in torretta_mazak['hd2']:
            x = f"| [{i}]:   {torretta_mazak['hd2'][i]} |"
            if i == "T1":
                x = f"{separatore}\n| [{i}]:   {torretta_mazak['hd2'][i]} |"
            elif len(x) > 74:
                x = f"| [{i}]:  {torretta_mazak['hd2'][i]} |"
                if i == "T12":
                    x = f"| [{i}]:  {torretta_mazak['hd2'][i]} |\n{separatore}"
            print(x)
    elif codice_forcella == "2150L0046":
        torretta_mazak["hd2"]["T1"]["Codice_utensile"]="UTSN 06x"
        torretta_mazak["hd2"]["T1"]["Codice_inserto"]="UTLI 120x"
        torretta_mazak["hd2"]["T2"]["Codice_utensile"]="-------x"
        torretta_mazak["hd2"]["T2"]["Codice_inserto"]="--------x"
        torretta_mazak["hd2"]["T3"]["Codice_utensile"]="UTSN 21x"
        torretta_mazak["hd2"]["T3"]["Codice_inserto"]="UTLI  32x"
        torretta_mazak["hd2"]["T4"]["Codice_utensile"]="-------x"
        torretta_mazak["hd2"]["T4"]["Codice_inserto"]="--------x"
        torretta_mazak["hd2"]["T5"]["Codice_utensile"]="UTSN 21x"
        torretta_mazak["hd2"]["T5"]["Codice_inserto"]="UTLI  17x"
        torretta_mazak["hd2"]["T6"]["Codice_utensile"]="-------x"
        torretta_mazak["hd2"]["T6"]["Codice_inserto"]="--------x"
        torretta_mazak["hd2"]["T7"]["Codice_utensile"]="-------x"
        torretta_mazak["hd2"]["T7"]["Codice_inserto"]="--------x"
        torretta_mazak["hd2"]["T8"]["Codice_utensile"]="-------x"
        torretta_mazak["hd2"]["T8"]["Codice_inserto"]="--------x"
        torretta_mazak["hd2"]["T9"]["Codice_utensile"]="UTLN 69x"
        torretta_mazak["hd2"]["T9"]["Codice_inserto"]="UFRZ  27x"
        torretta_mazak["hd2"]["T10"]["Codice_utensile"]="UTSN 27x"
        torretta_mazak["hd2"]["T10"]["Codice_inserto"]="UALC  04x"
        torretta_mazak["hd2"]["T11"]["Codice_utensile"]="-------x"
        torretta_mazak["hd2"]["T11"]["Codice_inserto"]="--------x"
        torretta_mazak["hd2"]["T12"]["Codice_utensile"]="-------x"
        torretta_mazak["hd2"]["T12"]["Codice_inserto"]="--------x"
        for i in torretta_mazak['hd2']:
            x = f"| [{i}]:   {torretta_mazak['hd2'][i]} |"
            if i == "T1":
                x = f"{separatore}\n| [{i}]:   {torretta_mazak['hd2'][i]} |"
            elif len(x) > 74:
                x = f"| [{i}]:  {torretta_mazak['hd2'][i]} |"
                if i == "T12":
                    x = f"| [{i}]:  {torretta_mazak['hd2'][i]} |\n{separatore}"
            print(x)
    else:
        print(f"Codice [{codice_forcella}] non trovato.\n")

def attrez_mandrino_hd1(codice_forcella):
    if codice_forcella == "2150G0042":
        mandrino_mazak["hd1"]["codice_morsa_A"]="UMOI 754 + UMOI 759" 
        mandrino_mazak["hd1"]["codice_morsa_B"]="UMOI 753 + UMOI 760"
        mandrino_mazak["hd1"]["codice_appoggio"]="UAGG 370"
        mandrino_mazak["hd1"]["codice_centraggio_sfera"]="UAGG 369"
        for i in mandrino_mazak["hd1"]:
            x = f"| [{i}]: {mandrino_mazak['hd1'][i]}|"
            if i == "codice_morsa_A":
                x = f"{separatore}\n| [{i}]: {mandrino_mazak['hd1'][i]:>52} |\n|{"|":>73}"
            elif i == "codice_morsa_B":
                x = f"| [{i}]: {mandrino_mazak['hd1'][i]:>52} |\n{separatore}"
            elif i == "codice_appoggio":
                x = f"| [{i}]: {mandrino_mazak['hd1'][i]:>51} |\n|{"|":>73}"
            elif i == "codice_centraggio_sfera":
                x = f"| [{i}]: {mandrino_mazak['hd1'][i]:>43} |\n{separatore}"
            print(x)
    elif codice_forcella == "2150L0046":
        mandrino_mazak["hd1"]["codice_morsa_A"]="UMOI 75x + UMOI 75x" 
        mandrino_mazak["hd1"]["codice_morsa_B"]="UMOI 75x + UMOI 76x"
        mandrino_mazak["hd1"]["codice_appoggio"]="UAGG 37x"
        mandrino_mazak["hd1"]["codice_centraggio_sfera"]="UAGG 36x"
        for i in mandrino_mazak["hd1"]:
            x = f"| [{i}]: {mandrino_mazak['hd1'][i]}|"
            if i == "codice_morsa_A":
                x = f"{separatore}\n| [{i}]: {mandrino_mazak['hd1'][i]:>52} |\n|{"|":>73}"
            elif i == "codice_morsa_B":
                x = f"| [{i}]: {mandrino_mazak['hd1'][i]:>52} |\n{separatore}"
            elif i == "codice_appoggio":
                x = f"| [{i}]: {mandrino_mazak['hd1'][i]:>51} |\n|{"|":>73}"
            elif i == "codice_centraggio_sfera":
                x = f"| [{i}]: {mandrino_mazak['hd1'][i]:>43} |\n{separatore}"
            print(x)
    else:
        print(f"Codice {codice_forcella} non trovato.")

def attrez_mandrino_hd2(codice_forcella):
    if codice_forcella == "2150G0042":
        mandrino_mazak["hd2"]["codice_staffe"]="UMOI 779"
        mandrino_mazak["hd2"]["codice_appoggio"]="UAGG 382"
        mandrino_mazak["hd2"]["codice_cono_centr"]="UFLA 153"
        for i in mandrino_mazak['hd2']:
            x = f"| [{i}]: {mandrino_mazak['hd2'][i]}|"
            if i == "codice_staffe":
                x = f"{separatore}\n| [{i}]: {mandrino_mazak['hd2'][i]:>53} |"
            elif i == "codice_appoggio":
                x = f"| [{i}]: {mandrino_mazak['hd2'][i]:>51} |"
            elif i == "codice_cono_centr":
                x = f"| [{i}]: {mandrino_mazak['hd2'][i]:>49} |\n{separatore}"
            print(x)
    elif codice_forcella == "2150L0046":
        mandrino_mazak["hd2"]["codice_staffe"]="UMOI 77x"
        mandrino_mazak["hd2"]["codice_appoggio"]="UAGG 38x"
        mandrino_mazak["hd2"]["codice_cono_centr"]="UFLA 15x"
        for i in mandrino_mazak['hd2']:
            x = f"| [{i}]: {mandrino_mazak['hd2'][i]}|"
            if i == "codice_staffe":
                x = f"{separatore}\n| [{i}]: {mandrino_mazak['hd2'][i]:>53} |"
            elif i == "codice_appoggio":
                x = f"| [{i}]: {mandrino_mazak['hd2'][i]:>51} |"
            elif i == "codice_cono_centr":
                x = f"| [{i}]: {mandrino_mazak['hd2'][i]:>49} |\n{separatore}"
            print(x)
    else:
        print(f"Codice {codice_forcella} non trovato.\n")

def attrez_robot_mazak(codice_forcella):
    if codice_forcella == "2150G0042":
        robot_mazak["codici_morse_bloccaggio"]["flangia"]="SERIE - E"
        robot_mazak["codici_morse_bloccaggio"]["sfera"]="UMOI 780"
        robot_mazak["setup_n"]= "5"
        robot_mazak["programma_n"]="5"
        for i in robot_mazak:
            x = f"|{"|":>76}\n| [{i}]:{"\t"*8}[{robot_mazak[i]}] |"
            if i == "codici_morse_bloccaggio":
                x = f"{separatore_tab_robot}\n| [{i}]: [{robot_mazak[i]}]|"
            if i == "programma_n":
                x = f"|{"|":>76}\n| [{i}]: {"[":>56}{robot_mazak[i]}] |\n{separatore_tab_robot}" 
            print(x)
    elif codice_forcella == "2150L0046":
        robot_mazak["codici_morse_bloccaggio"]["flangia"]="SERIE - L"
        robot_mazak["codici_morse_bloccaggio"]["sfera"]="UMOI 78x"
        robot_mazak["setup_n"]= "9"
        robot_mazak["programma_n"]="9"
        for i in robot_mazak:
            x = f"|{"|":>76}\n| [{i}]:{"\t"*8}[{robot_mazak[i]}] |"
            if i == "codici_morse_bloccaggio":
                x = f"{separatore_tab_robot}\n| [{i}]: [{robot_mazak[i]}]|"
            if i == "programma_n":
                x = f"|{"|":>76}\n| [{i}]: {"[":>56}{robot_mazak[i]}] |\n{separatore_tab_robot}" 
            print(x)
    else:
        print(f"Codice {codice_forcella} non trovato.")
def attrezzaggio_forcella(codice_forcella):
    print(f"\n{separatore}\n|{"[Torretta_Mazak]:HD1-HD2":^72}|\n{separatore}\n|{"[HD1]":^72}|\n{separatore}")
    attrez_torretta_hd1(codice_forcella)
    print(f"{separatore}\n|{"[HD2]":^72}|\n{separatore}")
    attrez_torretta_hd2(codice_forcella)
    print(f"{separatore}\n|{"[Mandrino_Mazak]:HD1-HD2":^72}|\n{separatore}")
    print(f"| {"HD1":^71}|\n{separatore}")
    attrez_mandrino_hd1(codice_forcella)
    print(f"{separatore}\n| {"HD2":^71}|\n{separatore}")
    attrez_mandrino_hd2(codice_forcella)
    print(f"{separatore_tab_robot}\n|{"[Robot_Mazak]":>45}{"\t"*4}    |\n{separatore_tab_robot}")
    attrez_robot_mazak(codice_forcella)


separatore = "-"*74
separatore_tab_robot= "-"*77
mandrino_mazak = {}
mandrino_mazak = carica_mandrino_mazak(mandrino_mazak)
torretta_mazak = {}
torretta_mazak = carica_torretta_mazak(torretta_mazak)
robot_mazak = {}
robot_mazak = carica_robot_mazak(robot_mazak)

## [DEBUG] ##
# print("\033c",end="")
# print(mandrino_mazak["hd1"]["codice_morsa_A"])
codice_forcella = "2150L0046"
attrezzaggio_forcella(codice_forcella)
# attrez_robot_mazak(codice_forcella)
# attrez_mandrino_hd1(codice_forcella)
# attrez_torretta_hd1(codice_forcella)
# attrez_torretta_hd2(codice_forcella)
# attrez_mandrino_hd2(codice_forcella)
