import math

def misura_diam_sfera(codice_forcella, diam_sfera):
    if codice_forcella == "2150G0042":
        if diam_sfera >= 27.961:
            return "valore diam_sfera : maggiorato"
        elif diam_sfera <= 27.929:
            return "valore diam_sfera : minorato"
        else:
            return "valore diam_sfera : nella norma"
    
def misura_diam_flangia_int(codice_forcella, diam_flangia_int):
    if codice_forcella == "2150G0042":    
        if diam_flangia_int >= 63.031:
            return "valore diam_flangia_int : maggiorato"
        elif diam_flangia_int <= 63.000:
            return "valore diam_flangia_int : minorato"
        else:
            return "valore diam_flangia_int : nella norma"
        
def misura_diam_flangia_est(codice_forcella, diam_flangia_est):
    if codice_forcella == "2150G0042":
        if diam_flangia_est >= 75.081:
            return "valore diam_flangia_est : maggiorato"
        elif diam_flangia_est <= 75.029:
            return "valore diam_flangia_est : minorato"
        else:
            return "valore diam_flangia_est : nella norma"
        
def misura_dist_canaline(codice_forcella, dist_canaline):
    if codice_forcella == "2150G0042":
        if dist_canaline >= 102.870:
            return "valore dist_canaline : maggiorato"
        elif dist_canaline <= 102.759:
            return "valore dist_canaline : minorato"
        else:
            return "Valore dist_canaline : nella norma"
        
def misura_h_tot(codice_forcella,h_tot):
    if codice_forcella == "2150G0042":
        if h_tot >= 118.110:
            return "valore h_tot : maggiorato"
        elif h_tot <= 117.89:
            return "valore h_tot : minorato"
        else:
            return "valore h_tot : nella norma"
        
def misura_centro_sfera(codice_forcella,centro_sfera):
    if codice_forcella == "2150G0042":
        if centro_sfera >= 107.560:
            return "valore centro_sfera : maggiorato"
        elif centro_sfera <= 107.44:
            return "valore centro_sfera : minorato"
        else:
            return "valore centro_sfera : nella norma"
        
def misura_centro_occhi(codice_forcella,centro_occhi):
    if codice_forcella == "2150G0042":
        if centro_occhi >= 65.560:
            return "valore centro_occhi : maggiorato"
        elif centro_occhi <= 65.44:
            return "valore centro_occhi : minorato"
        else:
            return "valore centro_occhi : nella norma"
        
def misura_diam_occhi(codice_forcella,diam_occhi):
    if codice_forcella == "2150G0042":
        if diam_occhi >= 27.022:
            return "valore diam_occhi : maggiorato"
        elif diam_occhi <= 26.999:
            return "valore diam_occhi : minorato"
        else:
            return "valore diam_occhi : nella norma"
        

        
    