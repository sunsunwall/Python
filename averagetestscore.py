#Räkna ut medelvärdet av provpoäng på Python provets 3 delar
#Skrivet av Sunny Vanderwall 2024-03
#time modulen importeras för att skapa ett trevligare avslut av programmet
import time

print("\n\nRäkna ut medelvärdet av poäng på Pythonprovets tre delar. \n\n=====================\n")

#Nestat i en while loop for att kunna räkna flera olika provresultat
while True:
    #summa måste börja med ett 0 värde för att kunna iterras i for loopen
    summa = 0 
    for i in range(1,4):
        #while true + try används för hantera om användaren matar in något som inte är ett heltal mellan 0 - 100
        while True:
            try:
                prov = int(input(f"\nAnge poäng på del {i} (0-100): "))                
                if 0 <= prov <= 100:
                    break
                #om användadaren anger ett negativt heltal eller ett heltal större än 100 loopas användaren tillbaka för att ange ett korrekt heltal.
                else:
                    print("\n\nFelaktigt värde! Ange poäng mellan 0 och 100.")
            #om användaren matar in något som inte är ett heltal loopas användaren tillbaka för att ange korrekt värde.
            except ValueError:
                print("\n\nFelaktigt värde. Ange ett heltal.")
        #om användaren anger ett korrekt värde läggs värdet till variabeln "summa" tills iterationen har körs 3 gånger
        summa += prov
    #när iterationen körts 3 gånger räknas medelvärdet ut och sparas i variablen "medel" 
    medel = summa/3
    print("\n\n==========================\n\n")
    print(f"Totalt {summa} poäng.\nMedelvärdet är {medel:.2f}.\n")
    if medel > 90:
        print("Bra jobbat!!!")
    #Användaren ges möjlighet att göra om uträkningen ifall de har flera provresultat att räkna ut medelvärdet för
    igen = input("\nVill du räkna ut ett till medelvärde? (j/n): ").lower()
    if igen != "j":
        print("Programmet avslutas.")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)
        print("Hej då!")
        time.sleep(0.5)
        print("...")
        break