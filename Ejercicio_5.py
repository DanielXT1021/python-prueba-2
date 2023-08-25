def main():
    palabra=input("Ingrese una palabra: ")
    letra=input("Ingrese una letra a contar: ")
    largo=len(palabra)
    contador=0
    for i in range (0,largo):
       if palabra[i]==letra:
          contador+=1
    print(f"la letra {letra} aparece {contador} veces")
if __name__=="__main__":
 main()