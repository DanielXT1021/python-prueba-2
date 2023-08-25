def Verificarprimo(x):
    veces=0
    for i in range(1,x+1):
        valor=i/2
        if (x%i)==0:
            veces+=1
        if veces>2 or x==2 or x==1:
            return True
    return False

def main():
    numero=int(input("Ingrese un numero: "))
    valor=Verificarprimo(numero)
    if valor==True:
        print("El numero es primo")
    else:
        print("El numero no es primo")
if __name__=="__main__":
    main()