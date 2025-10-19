import os 

contador = 0 

for i in range(0, 101):
    if contador == 0:
        print("CONVERSAO METRO - PES")
        print("METRO   PES")
        print('-' * 15)
        
    metros = i
    pes = metros / 0.3048
    print(f'{metros}m = {pes:.2f}ft')
    
    contador += 1
    if contador % 20 == 0 and i != 100:
        input("\nENTER para continuar...")
        os.system('cls')
        contador = 0  
