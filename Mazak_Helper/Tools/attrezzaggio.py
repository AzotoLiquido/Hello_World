import json
import rich
from rich.table import Table
from rich.style import Style
import os

# MODULO PER LA PRESENTAZIONE A VIDEO


# Facoltativo:
os.system('cls')

# traduzione da dicitura a frase per utente
dizionario = {
    "h_tot": "Altezza",
    "centro_sfera": "Centro Sfera",
    "centro_occhi": "Centro Occhi",
    "sottoponte": "Sottoponte",
    "dist_canaline": "Distanza Canaline",
    "diam_occhi": "Diametro Occhi",
    "diam_canaline": "Diametro Canaline",
    "diam_flangia_int": "Diametro Flangia Interno",
    "diam_flangia_est": "Diametro Flangia Esterno",
    "diam_sfera": "Diametro Sfera",
    "quota_g": "Quota G",
    "morsa_A": "Morsa A",
    "morsa_B": "Morsa B",
    "appoggio": "Appoggio",
    "centraggio_sfera": "Centraggio Sfera",
    "staffe": "Staffe",
    "cono_centr": "Cono Centrale",
    "setup_n": "Setup n°",
    "programma_n": "Programma n°",
}

forcelle = json.load(open(r"Data/forcelle.json", "r"))

# definisco lo stile per i titoli delle tabelle
stile_titolo = Style(bold=True, color="grey0", bgcolor="green3")


def display_dimensioni(codice_forcella):
    forcella = forcelle[codice_forcella]

    table = Table(title="Dimensioni", title_style=stile_titolo)
    table.add_column("Dimensione", style="bold green", no_wrap=True)
    table.add_column("MIN", justify="right")
    table.add_column("MAX", justify="right")
    for dimensione in forcella["dimensioni"]:
        dim = forcella["dimensioni"][dimensione]
        table.add_row(dizionario[dimensione], f"{dim['min']:.3f}", f"{dim['max']:.3f}")
    rich.print(table)

def display_torretta(codice_forcella: str):
    forcella = forcelle[codice_forcella]
    torretta = forcella["codici"]["torretta"]
    table = Table(title="Torretta", title_style=stile_titolo, show_header=False)
    table.add_column()
    table.add_column(justify="center")
    for hd in torretta:
        table.add_section()
        table.add_row("", hd.upper(), "", style="bold yellow", end_section=True)
        table.add_row("Torretta", "Utensile", "Inserto", style="bold yellow", end_section=True)
        for t in torretta[hd]:
            utensile = torretta[hd][t]["utensile"]
            inserto = torretta[hd][t]["inserto"]
            row = [f"[{t.upper()}]", f"{utensile}", f"{inserto}"]
            table.add_row(*row)
    rich.print(table)

def display_mandrino(codice_forcella: str):
    forcella = forcelle[codice_forcella]
    mandrino = forcella["codici"]["mandrino"]
    table = Table(title="Mandrino", title_style=stile_titolo, show_header=False)
    for hd in mandrino:
        table.add_section()
        table.add_row("", hd.upper(),"", style="bold yellow")
        table.add_section()
        for chiave in mandrino[hd]:
            table.add_row(dizionario[chiave], "", mandrino[hd][chiave])
    rich.print(table)

def display_robot(codice_forcella: str):
    forcella = forcelle[codice_forcella]
    robot = forcella["codici"]["robot"]
    table = Table(title="Robot", title_style=stile_titolo, show_header=False)
    for chiave in robot:
        if chiave != "morse_bloccaggio":
            chiav = dizionario.get(chiave)
            if not chiav:
                chiav = chiave.title()
            table.add_row(chiav, "", robot[chiave])
        else:
            for morse in robot["morse_bloccaggio"]:
                table.add_row(morse.title(), "", robot[chiave][morse])
    rich.print(table)

def display_tempra(codice_forcella: str):
    forcella = forcelle[codice_forcella]
    tempra = forcella["codici"]["tempra"]
    table = Table(title="Tempra", title_style=stile_titolo, show_header=False)
    for chiave in tempra:
        table.add_row(chiave.title(),"",tempra[chiave])
    rich.print(table)

def display_nastro_caricatore(codice_forcella: str):
    forcella = forcelle[codice_forcella]
    nastro = forcella["codici"]["nastro_caricatore"]
    table = Table(title="Nastro_Caricatore",title_style=stile_titolo,show_header=False)
    for chiave in nastro:
        table.add_row(chiave.title(),"",nastro[chiave])
    rich.print(table)

def display_forcella(codice_forcella):
    display_dimensioni(codice_forcella)
    display_torretta(codice_forcella)
    display_mandrino(codice_forcella)
    display_robot(codice_forcella)
    display_tempra(codice_forcella)
    display_nastro_caricatore(codice_forcella)


# --- DEBUG ----
# display_forcella("2150L0046")


# Funzioni per mostrare i menù
# def mostra_menu_principale():
#     pass


# def mostra_menu_admin():
#     pass


# def mostra_menu_attrezzaggio():
#     pass


# def mostra_menu_errori():
    # pass
