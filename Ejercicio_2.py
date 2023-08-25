def main():
    salir=False
    while salir==False:
        opcion=int(input("Ingresa algun de las siguientes opciones\n\n1.)Conversion de kilometros a millas\n2.)Conversion de millas a kilometros\n3.)Conversion de kilogramos a libras\n4.)Conversion de celcius a fahrenheit\n5.)Conversion de Fahrenheit a celcius\n6.)Salir del programa\n\nElija una opcion: "))
        if opcion==1:
            kilometros=float(input("\nIngrese el valor en kilometros: "))
            millas=kilometros*0.621371
            print(f"la conversion a millas es: {millas}")
        if opcion==2:
            millas=float(input("\nIngrese el valor en millas: "))
            kilometros=millas*1.60934
            print(f"la conversion a kilometros es: {kilometros}")
        if opcion==3:
            kilogramos=float(input("\nIngrese el valor en kilogramos: "))
            libras=kilogramos*2.20462
            print(f"la conversion a libras es: {libras}")
        if opcion==4:
            libras=float(input("\nIngrese el valor en libras: "))
            kilogramos=libras*0.453592
            print(f"la conversion a kilogramos es: {kilogramos}")
        if opcion==5:
            celcius=float(input("\nIngrese el valor en celcius: "))
            fahrenheit=(celcius*(9/5)+32)
            print(f"la conversion a fahrenheit es: {fahrenheit}")
        if opcion==6:
            fahrenheit=float(input("\nIngrese el valor en fahrenheit: "))
            celcius=(fahrenheit-32)*(5/9)
            print(f"la conversion a celcius es: {celcius}")
        if opcion==7:
            salir=True
if __name__ == "__main__":
    main()

