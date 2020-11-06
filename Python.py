contador=2

def juego(contador):

    entrada = input("\n¿Cuál es el color de la fruta en la que pienso?: \n")
    if str(entrada) != "naranja" :
        if contador>0:
            contador = contador-1
            print("\n te equivocaste te quedan "+ str(contador+1)+" intentos.\n Prueba otra vez:")
            juego(contador)
        else:
            print("\n GAME OVER ya no tienes mas intentos \n")
    elif str(entrada) =="naranja" :
        
        print(" \n¡Felicidades adivinaste el color!\n ")     
       
juego(contador)