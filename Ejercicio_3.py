def verificarpalindromo(oracion):
    reves=oracion[::-1]
  
    if oracion==reves:
        return True
    else:
        return False
def main():
    correcto=False
    while correcto==False:
        oracion=input("Ingrese una oracion: ")
        oracion=oracion.replace(" ","")
        if len(oracion)>=3:
            valor=verificarpalindromo(oracion)
            if valor==True:
                print("es palindromo")
            else:
                print("no es palindromo")
            correcto=True


if __name__=="__main__":
    main()