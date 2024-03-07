
# MISURA

def misura_diam_sfera(codice_forcella, diam_sfera):
    if codice_forcella == "2150G0042":
        if diam_sfera >= 27.961:
            return True
        elif diam_sfera <= 27.929:
            return False
        else:
            return None
    elif codice_forcella == "2150L0046":
        if diam_sfera >= 27.961:
            return True
        elif diam_sfera <= 27.929:
            return False
        else:
            return None
        
def misura_diam_flangia_int(codice_forcella, diam_flangia_int):
    if codice_forcella == "2150G0042":    
        if diam_flangia_int >= 63.031:
            return True
        elif diam_flangia_int <= 63.000:
            return False
        else:
            return None
    elif codice_forcella == "2150L0046":
        if diam_flangia_int >= 63.031:
            return True
        elif diam_flangia_int <= 63.000:
            return False
        else:
            return None      
        
def misura_diam_flangia_est(codice_forcella, diam_flangia_est):
    if codice_forcella == "2150G0042":
        if diam_flangia_est >= 75.081:
            return True
        elif diam_flangia_est <= 75.029:
            return False
        else:
            return None
    elif codice_forcella == "2150L0046":
        if diam_flangia_est >= 75.081:
            return True
        elif diam_flangia_est <= 75.029:
            return False
        else:
            return None
        
def misura_dist_canaline(codice_forcella, dist_canaline):  
    if codice_forcella == "2150G0042":
        if dist_canaline >= 102.870:
            return True
        elif dist_canaline <= 102.759:
            return False
        else:
            return None
    elif codice_forcella == "2150L0046":
        if dist_canaline >= 102.870:
            return True
        elif dist_canaline <= 102.759:
            return False
        else:
            return None
        
def misura_h_tot(codice_forcella,h_tot):
    if codice_forcella == "2150G0042":
        if h_tot >= 118.110:
            return True
        elif h_tot <= 117.89:
            return False
        else:
            return None
    elif codice_forcella == "2150L0046":
        if h_tot >= 118.110:
            return True
        elif h_tot <= 117.89:
            return False
        else:
            return None
        
def misura_centro_sfera(codice_forcella,centro_sfera):
    if codice_forcella == "2150G0042":
        if centro_sfera >= 107.560:
            return True
        elif centro_sfera <= 107.44:
            return False
        else:
            return None
    elif codice_forcella == "2150L0046":
        if centro_sfera >= 107.560:
            return True  
        elif centro_sfera <= 107.44:
            return False
        else:    
            return None  
        
def misura_centro_occhi(codice_forcella,centro_occhi):
    if codice_forcella == "2150G0042":
        if centro_occhi >= 65.560:
            return True
        elif centro_occhi <= 65.440:
            return False
        else:
            return None
    elif codice_forcella == "2150L0046":
        if centro_occhi >= 65.560:
            return True
        elif centro_occhi <= 65.44:
            return False
        else:
            return None
         
def misura_diam_occhi(codice_forcella,diam_occhi):
    if codice_forcella == "2150G0042":
        if diam_occhi >= 27.022:
            return True
        elif diam_occhi <= 26.999:
            return False
        else:
            return None
    elif codice_forcella == "2150L0046":
        if diam_occhi >= 27.022:
            return True
        elif diam_occhi <= 26.999:
            return False
        else:
            return None
        
def misura_sottoponte(codice_forcella,sottoponte):
    if codice_forcella == "2150G0042":
        if sottoponte >= 81.501:
            return True
        if sottoponte <= 80.979:
            return False
        else:
            return None
    elif codice_forcella == "2150L0046":
        if sottoponte >= 81.51:
            return True
        if sottoponte <= 80.79:
            return False
        else:
            return None
        
def misura_diam_canaline(codice_forcella,diam_canaline):
    if codice_forcella == "2150G0042":
        if diam_canaline >= 29.051 :
            return True
        if diam_canaline <= 28.799:
            return False
        else:
            return None
    elif codice_forcella == "2150L0046":
        if diam_canaline >= 29.051 :
            return True
        if diam_canaline <= 28.800:
            return False
        else:
            return None      
   
# CORREZIONE     

def calcola_diam_sfera(codice_forcella,diam_sfera):
    if codice_forcella == "2150G0042":
        if misura_diam_sfera(codice_forcella,diam_sfera) == True:
            differenza = round(diam_sfera - 27.930,3)
            print(f"valore diametro sfera : maggiorato\nCorrezione : X -{differenza}")
        elif misura_diam_sfera(codice_forcella,diam_sfera) == False:
            differenza = round((diam_sfera-27.930)*-1,3)
            print(f"valore diametro sfera : minorato\nCorrezione : X +{differenza}")
        elif misura_diam_sfera(codice_forcella,diam_sfera) == None:
            differenza = round(diam_sfera-27.930,3)
            print(f"valore diametro sfera : nella norma\nCorrezione : X -{differenza}\nSe il valore è nella norma, la correzione è facoltativa, ma il diametro della sfera, per maggior sicurezza è consigliabile tenerlo sulla quota minima.")
    elif codice_forcella == "2150L0046":
        if misura_diam_sfera(codice_forcella,diam_sfera) == True:
            differenza = round(diam_sfera - 27.930,3)
            print(f"valore diametro sfera : maggiorato\nCorrezione : X -{differenza}")
        elif misura_diam_sfera(codice_forcella,diam_sfera) == False:
            differenza = round((diam_sfera-27.930)*-1,3)
            print(f"valore diametro sfera : minorato\nCorrezione : X +{differenza}")
        elif misura_diam_sfera(codice_forcella,diam_sfera) == None:
            differenza = round(diam_sfera-27.930,3)
            print(f"valore diametro sfera : nella norma\nCorrezione : X -{differenza}\nSe il valore è nella norma, la correzione è facoltativa, ma il diametro della sfera, per maggior sicurezza è consigliabile tenerlo sulla quota minima.")

def calcola_diam_flangia_int(codice_forcella,diam_flangia_int):
    if codice_forcella == "2150G0042":
        if misura_diam_flangia_int(codice_forcella,diam_flangia_int) == True:
            differenza = round(diam_flangia_int-63.000,3)
            print(f"valore diametro flangia interno : maggiorato\nCorrezione : X -{differenza}")
        elif misura_diam_flangia_int(codice_forcella,diam_flangia_int) == False:
            differenza = round((diam_flangia_int-63.000)*-1,3)
            print(f"valore diametro flangia interno : minorato\nCorrezione : X +{differenza}")
        elif misura_diam_flangia_int(codice_forcella,diam_flangia_int) == None:
            differenza = round(diam_flangia_int-63.000,3)
            print(f"valore diametro flangia interno : nella norma\nCorrezione : X -{differenza}")
    elif codice_forcella == "2150L0046":
        if misura_diam_flangia_int(codice_forcella,diam_flangia_int) == True:
            differenza = round(diam_flangia_int-63.000,3)
            print(f"valore diametro flangia interno : maggiorato\nCorrezione : X -{differenza}")
        elif misura_diam_flangia_int(codice_forcella,diam_flangia_int) == False:
            differenza = round((diam_flangia_int-63.000)*-1,3)
            print(f"valore diametro flangia interno : minorato\nCorrezione : X +{differenza}")
        elif misura_diam_flangia_int(codice_forcella,diam_flangia_int) == None:
            differenza = round(diam_flangia_int-63.000,3)
            print(f"valore diametro flangia interno : nella norma\nCorrezione : X -{differenza}")
            
def calcola_diam_flangia_est(codice_forcella,diam_flangia_est):
    if codice_forcella == "2150G0042":
        if misura_diam_flangia_est(codice_forcella,diam_flangia_est) == True:
            differenza = round(diam_flangia_est-75.300,3)
            print(f"valore diametro flangia esterno : maggiorato\nCorrezione : X -{differenza}")
        elif misura_diam_flangia_est(codice_forcella,diam_flangia_est) == False:
            differenza = round((diam_flangia_est-75.300)*-1,3)
            print(f"valore diametro flangia esterno : minorato\nCorrezione : X +{(differenza)}")
        elif misura_diam_flangia_est(codice_forcella,diam_flangia_est):
            differenza = round(diam_flangia_est-75.300,3)
            print(f"valore diametro flangia esterno : nella norma\nCorrezione : X -{differenza}")
    elif codice_forcella == "2150L0046":
        if misura_diam_flangia_est(codice_forcella,diam_flangia_est) == True:
            differenza = round(diam_flangia_est-75.300,3)
            print(f"valore diametro flangia esterno : maggiorato\nCorrezione : X -{differenza}")
        elif misura_diam_flangia_est(codice_forcella,diam_flangia_est) == False:
            differenza = round((diam_flangia_est-75.300)*-1,3)
            print(f"valore diametro flangia esterno : minorato\nCorrezione : X +{(differenza)}")
        elif misura_diam_flangia_est(codice_forcella,diam_flangia_est):
            differenza = round(diam_flangia_est-75.300,3)
            print(f"valore diametro flangia esterno : nella norma\nCorrezione : X -{differenza}")
            
def calcola_dist_canaline(codice_forcella,dist_canaline):
    if codice_forcella == "2150G0042":
        if misura_dist_canaline(codice_forcella,dist_canaline) == True:
            differenza = round(dist_canaline-102.760,3)
            print(f"valore distanza canaline : maggiorato\nCorrezione : X -{differenza}")
        elif misura_dist_canaline(codice_forcella,dist_canaline):
            differenza = round((dist_canaline-102.760)*-1,3)
            print(f"valore distanza canaline : minorato\nCorrezione : X +{differenza}")
        elif misura_dist_canaline(codice_forcella,dist_canaline) == None:
            differenza = round(dist_canaline-102.760,3)
            print(f"valore distanza canaline : nella norma\nCorrezione : X -{differenza}")
    elif codice_forcella == "2150L0046":
        if misura_dist_canaline(codice_forcella,dist_canaline) == True:
            differenza = round(dist_canaline-102.760,3)
            print(f"valore distanza canaline : maggiorato\nCorrezione : X -{differenza}")
        elif misura_dist_canaline(codice_forcella,dist_canaline):
            differenza = round((dist_canaline-102.760)*-1,3)
            print(f"valore distanza canaline : minorato\nCorrezione : X +{differenza}")
        elif misura_dist_canaline(codice_forcella,dist_canaline) == None:
            differenza = round(dist_canaline-102.760,3)
            print(f"valore distanza canaline : nella norma\nCorrezione : X -{differenza}")
            
def calcola_h_tot(codice_forcella,h_tot):
    if codice_forcella == "2150G0042":
        if misura_h_tot(codice_forcella,h_tot) == True:
            differenza = round(h_tot-117.900,3)
            print(f"valore altezza totale : maggiorato\nCorrezione : <Da chiedere>{differenza}")
        elif misura_h_tot(codice_forcella,h_tot) == False:
            differenza = round((h_tot-117.900)*-1,3)
            print(f"valore altezza totale : minorato\nCorrezione : <Da chiedere>{differenza}")
        elif misura_h_tot(codice_forcella,h_tot) == None:
            differenza = round(h_tot-117.900,3)   
            print(f"valore altezza totale : nella norma\nCorrezione : <Da chiedere>{differenza}")
    elif codice_forcella == "2150L0046":
        if misura_h_tot(codice_forcella,h_tot) == True:
            differenza = round(h_tot-117.900,3)
            print(f"valore altezza totale : maggiorato\nCorrezione : <Da chiedere>{differenza}")
        elif misura_h_tot(codice_forcella,h_tot) == False:
            differenza = round((h_tot-117.900)*-1,3)
            print(f"valore altezza totale : minorato\nCorrezione : <Da chiedere>{differenza}")
        elif misura_h_tot(codice_forcella,h_tot) == None:
            differenza = round(h_tot-117.900,3)   
            print(f"valore altezza totale : nella norma\nCorrezione : <Da chiedere>{differenza}")        
            
def calcola_centro_sfera(codice_forcella,centro_sfera):
    if codice_forcella == "2150G0042":
        if misura_centro_sfera(codice_forcella,centro_sfera) == True:
            differenza = round(centro_sfera-107.450,3)
            print(f"valore centro sfera : maggiorato\nCorrezione : <Da chiedere>{differenza}")
        elif misura_centro_sfera(codice_forcella,centro_sfera) == False: 
            differenza = round((centro_sfera-107.450)*-1,3)
            print(f"valore centro sfera : minorato\nCorrezione : <Da chiedere>{differenza}")
        elif misura_centro_sfera(codice_forcella,centro_sfera) == None:
            differenza = round(centro_sfera-107.450,3)
            print(f"valore centro sfera : nella norma\nCorrezione : <Da chiedere>{differenza}")
    elif codice_forcella == "2150L0046":
        if misura_centro_sfera(codice_forcella,centro_sfera) == True:
            differenza = round(centro_sfera-107.450,3)
            print(f"valore centro sfera : maggiorato\nCorrezione : <Da chiedere>{differenza}")
        elif misura_centro_sfera(codice_forcella,centro_sfera) == False: 
            differenza = round((centro_sfera-107.450)*-1,3)
            print(f"valore centro sfera : minorato\nCorrezione : <Da chiedere>{differenza}")
        elif misura_centro_sfera(codice_forcella,centro_sfera) == None:
            differenza = round(centro_sfera-107.450,3)
            print(f"valore centro sfera : nella norma\nCorrezione : <Da chiedere>{differenza}")
            
def calcola_centro_occhi(codice_forcella,centro_occhi):
    if codice_forcella == "2150G0042":
        if misura_centro_occhi(codice_forcella,centro_occhi) == True:
            differenza = round(centro_occhi-65.450,3)
            print(f"valore centro occhi : maggiorato\nCorrezione : <Da chiedere>{differenza}")
        elif misura_centro_occhi(codice_forcella,centro_occhi) == True:
            differenza = round((centro_occhi-65.450)*-1,3)
            print(f"valore centro occhi : minorato\nCorrezione : <Da chiedere>{differenza}")
        elif misura_centro_occhi(codice_forcella,centro_occhi) == True:
            differenza = round(centro_occhi-65.450,3)
            print(f"valore centro occhi : nella norma\nCorrezione : <Da chiedere>{differenza}")
    elif codice_forcella == "2150L0046":
        if misura_centro_occhi(codice_forcella,centro_occhi) == True:
            differenza = round(centro_occhi-65.450,3)
            print(f"valore centro occhi : maggiorato\nCorrezione : <Da chiedere>{differenza}")
        elif misura_centro_occhi(codice_forcella,centro_occhi) == True:
            differenza = round((centro_occhi-65.450)*-1,3)
            print(f"valore centro occhi : minorato\nCorrezione : <Da chiedere>{differenza}")
        elif misura_centro_occhi(codice_forcella,centro_occhi) == True:
            differenza = round(centro_occhi-65.450,3)
            print(f"valore centro occhi : nella norma\nCorrezione : <Da chiedere>{differenza}")
            
def calcola_diam_occhi(codice_forcella,diam_occhi):
    if codice_forcella == "2150G0042":
        if misura_diam_occhi(codice_forcella,diam_occhi) == True:
            differenza = round(diam_occhi-27.000,3)
            print(f"valore diametro occhi : maggiorato\nCorrezione : <Da chiedere>{differenza}")
        elif misura_diam_occhi(codice_forcella,diam_occhi) == False:
            differenza = round((diam_occhi-27.000)*-1,3)
            print(f"valore diametro occhi : minorato\nCorrezione : <Da chiedere>{differenza}")
        elif misura_diam_occhi(codice_forcella,diam_occhi) == None:
            differenza = round(diam_occhi-27.000,3)
            print(f"valore diametro occhi : nella norma\nCorrezione : <Da chiedere>{differenza}")
    elif codice_forcella == "2150L0046":
        if misura_diam_occhi(codice_forcella,diam_occhi) == True:
            differenza = round(diam_occhi-27.000,3)
            print(f"valore diametro occhi : maggiorato\nCorrezione : <Da chiedere>{differenza}")
        elif misura_diam_occhi(codice_forcella,diam_occhi) == False:
            differenza = round((diam_occhi-27.000)*-1,3)
            print(f"valore diametro occhi : minorato\nCorrezione : <Da chiedere>{differenza}")
        elif misura_diam_occhi(codice_forcella,diam_occhi) == None:
            differenza = round(diam_occhi-27.000,3)
            print(f"valore diametro occhi : nella norma\nCorrezione : <Da chiedere>{differenza}")
            
def calcola_sottoponte(codice_forcella,sottoponte):
    if codice_forcella == "2150G0042":
        if misura_sottoponte(codice_forcella,sottoponte) == True:
            differenza = round(sottoponte-1,3)
            print(f"valore sottoponte : maggiorato\nCorrezione : <Da chiedere>{differenza}")           
        if misura_sottoponte(codice_forcella,sottoponte) == True:
            differenza = round((sottoponte-1)*-1,3)
            print(f"valore sottoponte : minorato\nCorrezione : <Da chiedere>{differenza}")             
        if misura_sottoponte(codice_forcella,sottoponte) == True:
            differenza = round(sottoponte-1,3)
            print(f"valore sottoponte : nella norma\nCorrezione : <Da chiedere>{differenza}") 
    elif codice_forcella == "2150L0046":
        if misura_sottoponte(codice_forcella,sottoponte) == True:
            differenza = round(sottoponte-1,3)
            print(f"valore sottoponte : maggiorato\nCorrezione : <Da chiedere>{differenza}")           
        if misura_sottoponte(codice_forcella,sottoponte) == True:
            differenza = round((sottoponte-1)*-1,3)
            print(f"valore sottoponte : minorato\nCorrezione : <Da chiedere>{differenza}")             
        if misura_sottoponte(codice_forcella,sottoponte) == True:
            differenza = round(sottoponte-1,3)
            print(f"valore sottoponte : nella norma\nCorrezione : <Da chiedere>{differenza}") 
            
def calcola_diam_canaline(codice_forcella,diam_canaline):
    if codice_forcella == "2150G0042":
        if misura_diam_canaline(codice_forcella,diam_canaline) == True:
            differenza = round(diam_canaline-28.000,3)
            print(f"valore diametro canaline : maggiorato\nCorrezione : <Da chiedere>{differenza}")
        elif misura_diam_canaline(codice_forcella,diam_canaline) == False:
            differenza = round((diam_canaline-28.000)*-1,3)
            print(f"valore diametro canaline : minorato\nCorrezione : <Da chiedere>{differenza}")
        elif misura_diam_canaline(codice_forcella,diam_canaline) == None:
            differenza = round(diam_canaline-28.000,3)
            print(f"valore diametro canaline : nella norma\nCorrezione : <Da chiedere>{differenza}")
    elif codice_forcella == "2150L0046":
        if misura_diam_canaline(codice_forcella,diam_canaline) == True:
            differenza = round(diam_canaline-28.000,3)
            print(f"valore diametro canaline : maggiorato\nCorrezione : <Da chiedere>{differenza}")
        elif misura_diam_canaline(codice_forcella,diam_canaline) == False:
            differenza = round((diam_canaline-28.000)*-1,3)
            print(f"valore diametro canaline : minorato\nCorrezione : <Da chiedere>{differenza}")
        elif misura_diam_canaline(codice_forcella,diam_canaline) == None:
            differenza = round(diam_canaline-28.000,3)
            print(f"valore diametro canaline : nella norma\nCorrezione : <Da chiedere>{differenza}")       
            
            
            
# diam_sfera = float(input("Inserisci diam_sfera."))
# calcola_diam_sfera("2150G0042",diam_sfera)
# diam_canaline = 29.9
# print(misura_diam_canaline("2150G0042",diam_canaline))
