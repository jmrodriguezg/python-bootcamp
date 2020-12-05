exit = False
while not exit :
    print ("Bienvenido al Generador de Nombres.")
    cityName = input ("Cual es el Nombre de la Ciudad donde vivias cuando eras niño? \n")
    petName = input ("Nombre de tu Mascota? \n")

    print ("El nombre pudiera ser: " + cityName + " " + petName)

    print("\n")
    resp = input("Desea intentar otra nombre? (s/n) ")
    if resp.upper() == "N" :
        exit = True
    


