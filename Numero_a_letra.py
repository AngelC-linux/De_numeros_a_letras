# Convertir numeros a letras
# José Ángel Cardona García
# De numeros a letras

UNIDADES = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve"]
DECENAS = ["diez", "once", "doce", "trece", "catorce", "quince", "dieciseis", "diecisiete", "dieciocho", "diecinueve"]
DIEZ_EN_DIEZ = ["cero","diez","veinte", "treinta", "cuarenta", "cincuenta", "sesenta", "setenta", "ochenta", "noventa"]
CENTENAS = ["", "cien", "doscientos", "trescientos", "cuatrocientos", "quinientos", "seiscientos", "setecientos", "ochocientos", "novecientos"]
MILLAR = ["mil"]
MILLONES = ["un millón", "millones"]
BILLONES = ["un billón", "billones"]
teclado = 0

def show_decenas(entrada):

    if(entrada < 10):
        return UNIDADES[entrada]
    
    decena, unidad = divmod(entrada, 10)
    if(entrada >= 10) and (entrada <= 19):
        return DECENAS[unidad]
    
    elif (entrada > 19) and (entrada <= 29):
        if(entrada == 20):
            return "veinte"
        else:
            return 'veinti%s' % UNIDADES[unidad]
    
    elif (entrada > 29) and (entrada <= 99):
        resultado = DIEZ_EN_DIEZ[decena]
          
        #if(entrada < 99) and (entrada > 29):
        if(unidad > 0):
            resultado = "%s y %s" % (resultado, UNIDADES[unidad])
        return resultado
        
    
    
def show_centenas(entrada):
    centena, decena = divmod(entrada, 100)
    if(entrada == 100):
        return "cien"
    
    elif(entrada > 100) and (entrada < 200):
        resultado = '%s %s' % ("ciento", show_decenas(decena))
        return resultado
        
    elif(entrada != 0):
        resultado = CENTENAS[centena]
        
        if(decena > 0):
            resultado = '%s %s' % (resultado, show_decenas(decena))
            return resultado
        else:
            resultado = CENTENAS[centena]
            return resultado
           
           
def show_millares(entrada):
    millar, centena = divmod(entrada, 1000)
    if(millar == 1):
        if(entrada > 1000) and (entrada < 2000):
            resultado = 'mil %s' % (show_centenas(centena))
            return resultado
        else:
            resultado = "mil"
            return resultado
        
    elif(millar >= 2) and (millar <= 9):
        resultado = (UNIDADES[millar])
        
        if(centena > 0):
            resultado = '%s mil %s' % (resultado, show_centenas(centena))
            return resultado
        else:
            resultado = '%s %s' % (UNIDADES[millar], MILLAR[0])
            return resultado
        
    elif(millar >= 10) and (millar <= 99):
        resultado = show_decenas(millar)
        
        if(centena > 0):
            resultado = '%s mil %s' % (resultado, show_centenas(centena))
            return resultado
        else:
            resultado = '%s %s' % (show_decenas(millar), MILLAR[0])
            return resultado
            
    elif(millar >= 100) and (millar <= 999):
        resultado = show_centenas(millar)
        
        if(centena > 0):
            resultado = "%s mil %s" % (resultado,  show_centenas(centena))
            return resultado
        else:
            resultado = '%s %s' % (show_centenas(millar), MILLAR[0])
            return resultado
        
        

def show_millones(entrada):
    millon, millar = divmod(entrada, 1000000)
    if(millon == 1):
        if(entrada > 1000000) and (entrada < 1001000):
            resultado = '%s %s' % (MILLONES[0], show_centenas(millar))
            return resultado
        elif(entrada >= 1001000) and (entrada < 2000000):
            resultado = '%s %s' % (MILLONES[0], show_millares(millar))
            return resultado
        else:
            resultado = '%s' % (MILLONES[0])
            return resultado
    
    elif(millon >= 2) and (millon <= 9):
        resultado = (UNIDADES[millon])
        
        if(millar > 0):
            resultado = "%s %s %s" % (resultado, MILLONES[1], show_millares(millar))
            return resultado
        else:
            resultado = '%s %s' % (UNIDADES[millon], MILLONES[1])
            return resultado
        
    elif(millon >= 10) and (millon < 100):
        resultado = show_decenas(millon)
        
        if(millar > 0):
            resultado = '%s %s %s' % (resultado, MILLONES[1], show_millares(millar))
            return resultado
        else:
            resultado = '%s %s' % (show_decenas(millon), MILLONES[1])
            return resultado
        
    elif(millon >= 100) and (millon <= 999):
        resultado = show_centenas(millon)
        
        if(millar > 0):
            resultado = '%s %s %s' % (show_centenas(millon), MILLONES[1], show_millares(millar))
            return resultado
        else:
            resultado = '%s %s' % (show_centenas(millon), MILLONES[1])
            return resultado
        
    elif(millon >= 1000) and (millon <= 999999):
        resultado = show_millares(millar)
        
        if(millar > 0):
            resultado = '%s %s %s' % (show_millares(millon), MILLONES[1], show_millares(millar))
            return resultado
        else:
            resultado = '%s %s' % (show_millares(millon), MILLONES[1])
            return resultado
    
def show_billones(entrada):
    billon, millon = divmod(entrada, 1000000000000)
    if(billon == 1):
        if(entrada > 1000000000000) and (entrada <= 1000000000999):
            resultado = '%s %s' % (BILLONES[0], show_centenas(millon))
            return resultado
        elif(entrada >= 1000000001000) and (entrada < 1000001000000):
            resultado = '%s %s' % (BILLONES[0], show_millares(millon))
            return resultado
        elif(entrada >= 1000001000000) and (entrada < 2000000000000):
            resultado = '%s %s' % (BILLONES[0], show_millones(millon))
            return resultado
        else:
            resultado = '%s' % (BILLONES[0])
            return resultado
    
    elif(billon >= 2) and (billon <= 9):
        resultado = (UNIDADES[billon])
        
        if(millon > 0):
            resultado = '%s %s %s' % (resultado, BILLONES[1], show_millones(millon))
            return resultado
        else:
            resultado = '%s %s' % (UNIDADES[billon], BILLONES[1])
            return resultado
    
    elif(billon >= 10) and (billon < 100 ):
        resultado = show_decenas(billon)
        
        if(millon > 0):
            resultado = "%s %s %s" % (resultado, BILLONES[1], show_millones(millon))
            return resultado
        else:
            resultado = '%s %s' % (UNIDADES[billon], BILLONES[1])
            return resultado
        
    elif(billon >= 100) and (billon <= 999):
        resultado = show_centenas(billon)
        
        if(millon > 0):
            resultado = '%s %s %s' % (show_centenas(billon), BILLONES[1], show_millones(millon))
            return resultado
        else:
            resultado = '%s %s' % (show_centenas(billon), BILLONES[1])
            return resultado
        
    elif(billon >= 1000) and (billon <= 999999):
        resultado = show_millares(billon)
        
        if(millon > 0):
            resultado = '%s %s %s' % (show_millares(billon), BILLONES[1], show_millones(millon))
            return resultado
        else:
            resultado = '%s %s' % (show_millares(billon), BILLONES[1])
            return resultado



'''teclado = int(input("Ingrese el numero: "))

if(teclado < 100):
    print(teclado, show_decenas(teclado))

elif(teclado >= 100) and (teclado < 1000):
    print(teclado, show_centenas(teclado))
    
elif(teclado >= 1000) and (teclado <= 999999):
    print(teclado, show_millares(teclado))
    
elif(teclado >= 1000000) and (teclado < 1000000000):
    print(teclado, show_millones(teclado))

elif(teclado >= 1000000000000) and (teclado < 999999999999999999):
    print(teclado, show_billones(teclado))'''

#print(show_decenas(50))
#print(show_centenas(101))
#print(show_millares(1001))
print(show_millones(1000001))
print(show_billones(2000000000000))
