
def main():
    #Escribe tu código debajo de esta línea
    Tuedad=int(input("Ingresa tu edad: "))
    if Tuedad<=0: 
        print ("Respuesta incorrecta")
    elif Tuedad<18:
        print ("No cumples requisitos")
    elif Tuedad>=18:
        id=str(input("¿Tienes identificación oficial? (s/n): "))
        if id=="s":
            print ("Trámite de licencia concedido")
        elif id=="n":
            print ("No cumples requisitos")
        else: 
            print ("Respuesta incorrecta")
    pass

if __name__ == '__main__':
    main()
