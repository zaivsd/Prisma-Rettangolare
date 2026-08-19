import math

while True:

    print("Inserire \"exit\" per fermare il programma")

    # input ---

    while True:
        
        lato1 = input("Lunghezza di un lato della base: ")
        
        if lato1.lower() == "exit":
            break
        elif lato1.isdecimal():
            break
        else:
            print("Input non valido")
            
    if lato1.lower() == "exit":
        break
        
    lato1 = int(lato1)

    
    while True:
        
        lato2 = input("Lunghezza dell'altro lato della base: ")
        
        if lato2.isdecimal():
            break
        else:
            print("Input non valido")
            
    lato2 = int(lato2)

    
    while True:
        
        altezza = input("Altezza del prisma: ")
        
        if altezza.isdecimal():
            break
        else:
            print("Input non valido")
            
    altezza = int(altezza)

    # ---

    # calcolo ---

    perimetro_base = 2 * (lato1 + lato2)

    area_base = lato1 * lato2

    area_laterale = perimetro_base * altezza

    area_totale = (2 * area_base) + area_laterale

    volume = lato1 * lato2 * altezza

    diagonale = math.sqrt((lato1 ** 2) + (lato2 ** 2) + (altezza ** 2))

    # ---

    # output ---

    print(f"""
           @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  
         @@                                         @@@ 
       @@ @                                        @@ @ 
      @@  @                                      @@   @ 
     @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    @ 
     @    @                                      @    @ 
     @    @                                      @    @ 
     @    @                                      @    @ 
     @    @                                      @    @ 
     @    @                                      @    @ 
     @    @                                      @    @ 
     @    @                                      @    @ 
     @    @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
     @   @@                                      @  @@  
     @ @@                                        @ @@   
     @@@                                         @@     
      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@       
    
    Lato1 = {lato1}
    Lato2 = {lato2}
    Altezza = {altezza}
    
    Perimetro base:
    2 * ({lato1} + {lato2}) = {perimetro_base}
    
    Area base:
    {lato1} * {lato2} = {area_base}
    
    Area laterale:
    {perimetro_base} * {altezza} = {area_laterale}
    
    Area totale:
    (2 * {area_base}) + {area_laterale} = {area_totale}
    
    Volume:
    {lato1} * {lato2} * {altezza} = {volume}
    
    Diagonale:
    √({lato1}^2 + {lato2}^2 + {altezza}^2) = {diagonale}
""")

    # ---
