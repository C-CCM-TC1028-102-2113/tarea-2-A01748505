def main():
    # Escribe el código adecuado para completar el programa
    x = int(input("Ingresa el primer número: "))
    y = int(input("Ingresa el segundo número: "))
    z = int(input("Ingresa el tercer número: "))
    if x<=y and y<=z:
        print (x)
        print (y)
        print (z)   
    elif x<=z and z<=y:
        print (x)
        print (z)
        print (y)   
    elif y<=x and x<=z:
        print (y)
        print (x)
        print (z)  
    elif y<=z and z<=x:
        print (y)
        print (z)
        print (x)  
    elif z<=x and x<=y:
        print (z)
        print (x)
        print (y)  
    elif z<=y and y<=x:
        print (z)
        print (y)
        print (x)  
    pass


if __name__=='__main__':
    main()
