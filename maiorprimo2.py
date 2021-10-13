def maior_primo(numero):
   
    primo = True
    x = 2
    
    while (primo == True and x < numero) or x == 2:
        if (numero/x)%1 != 0:
            primo = True
            x = x+1

        else:
            primo = False
            numero = numero - 1
            x = 2
                

        
    
    return numero

